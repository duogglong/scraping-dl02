- Install virtualenv
  ```
  Linux: sudo apt install python3-virtualenv
  CentOS: sudo yum install epel-release -y
  Windows: python3 -m venv myenv
  ```
- Activate virtualenv
  ```
  Linux: virtualenv venv && source venv/bin/activate
  CentOS: python3 -m venv myenv && source venv/bin/activate
  Windows: .\myenv\Scripts\activate
  ```
- Create project scrap
  ```
  scrapy startproject instagram_scraper
  cd instagram_scraper
  scrapy crawl instagram
  ```

  - Gen spider
  ```
  scrapy genspider books books.toscrape.com

  scrapy crawl -o ./output/info.csv books --loglevel DEBUG
  scrapy crawl -o ./output/output.json books
  ```