import scrapy
import json
from scrapy.http import FormRequest

class InstagramSpider(scrapy.Spider):
    name = "instagram"
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    start_urls = ['https://www.instagram.com/sontungmtp/']  # Trang bạn muốn scrape

    def parse(self, response):
        # Truyền thông tin đăng nhập vào đây
        return FormRequest.from_response(
            response,
            url=self.login_url,
            formdata={'username': 'your_username', 'password': 'your_password'},  # Đổi thành tài khoản của bạn
            callback=self.after_login
        )

    def after_login(self, response):
        # Kiểm tra xem đăng nhập có thành công hay không
        if b'authenticated": true' in response.body:
            self.log('Đăng nhập thành công!')
            # Sau khi đăng nhập thành công, thực hiện việc scrape dữ liệu
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse_data)
        else:
            self.log('Đăng nhập không thành công!')

    def parse_data(self, response):
        # Tìm dữ liệu JSON trong script tag
        script_tag = response.xpath('//script[contains(text(), "window._sharedData")]/text()').get()

        if script_tag:
            # Trích xuất JSON từ script tag
            json_data = script_tag.split('= ', 1)[1].rstrip(';')

            # Parse JSON
            data = json.loads(json_data)
            
            # Lấy dữ liệu người dùng
            user_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
            
            # Số người theo dõi
            followers_count = user_data['edge_followed_by']['count']
            print(f"Số người theo dõi: {followers_count}")
            
            # Lưu HTML vào file
            with open('./instagram/following/output/ins.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            
            # In số người theo dõi
            yield {
                'followers': followers_count
            }
