import scrapy
from scrapy.http import FormRequest

class InstagramLoginSpider(scrapy.Spider):
    name = "instagram_login"
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    start_urls = ['https://www.instagram.com/accounts/login/']  # URL trang đăng nhập Instagram

    def parse(self, response):
        # Gửi thông tin đăng nhập qua POST request
        return FormRequest.from_response(
            response,
            url=self.login_url,
            formdata={'username': 'your_username', 'password': 'your_password'},  # Đổi username và password của bạn
            callback=self.after_login
        )

    def after_login(self, response):
        # Kiểm tra xem đăng nhập có thành công không bằng cách kiểm tra JSON phản hồi từ Instagram
        if b'authenticated": true' in response.body:
            self.log('Đăng nhập thành công!')
        else:
            self.log('Đăng nhập không thành công!')
