import bs4
import requests
import re
from bs4 import BeautifulSoup
url = 'http://www.cosplay8.com/pic/chinacos/'
headers = {
    "Referer": "http://www.cosplay8.com/pic/chinacos/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
html_urls = re.findall('<p class="tcenter line24 yahei font16"><a href="/pic/chinacos/(.*?)" target="_blank" class="txtover" title="(.*?)">(.*?)</a>',  response.text)
for html_url in html_urls:
    html_u = html_url[0]
    html_t = html_url[1]
    html_list = f"http://www.cosplay8.com/pic/chinacos/{html_u}"
    result = requests.get(url=html_list, headers=headers)
    result.encoding = 'utf-8'
    data = bs4.BeautifulSoup(result.text, 'html.parser')
    ul = data.find(class_="pagebox").find_all("a")
    print(ul)




