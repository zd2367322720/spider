import bs4
import requests
import re
from bs4 import BeautifulSoup

photo_dict = []
url = 'http://www.cosplay8.com/pic/chinacos/'
headers = {
    "Referer": "http://www.cosplay8.com/pic/chinacos/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
html_urls = re.findall(
    '<p class="tcenter line24 yahei font16"><a href="/pic/chinacos/(.*?).html" target="_blank" class="txtover" title="(.*?)">(.*?)</a>',
    response.text)
for html_url in html_urls:
    html_u = html_url[0]
    html_t = html_url[1]
    html_list = f"http://www.cosplay8.com/pic/chinacos/{html_u}.html"
    result = requests.get(url=html_list, headers=headers)
    result.encoding = 'utf-8'
    data = bs4.BeautifulSoup(result.text, 'html.parser')
    data_list = data.select('.pagebox span')
    page_all = data_list[0]
    pages = re.findall('共(.*?)页: ', page_all.text)
    for i in range(1, int(pages[0]) + 1):
        if i == 1:
            page_url = f"http://www.cosplay8.com/pic/chinacos/{html_u}.html"
        else:
            page_url = f"http://www.cosplay8.com/pic/chinacos/{html_u}_{i}.html"
        photos_list = requests.get(url=page_url, headers=headers)
        photos_list.encoding = 'utf-8'
