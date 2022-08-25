import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}

for i in range(1, 10):
    if i == 1:
        url = "http://pic.netbian.com/index.html"
        print("开始下载第1页")
    else:
        url = f"http://pic.netbian.com/index_{i}.html"
        print(f"开始下载第{i}页")
    response = requests.get(url=url, headers=headers)
    response.encoding = "gbk"
    data = BeautifulSoup(response.text, "html.parser")
    ul = data.find(class_="slist").find_all("li")
    for li in ul:
        li_data = BeautifulSoup(str(li), "html.parser")
        img_url = f'http://pic.netbian.com/{li_data.find("a")["href"]}'
        img = requests.get(url=img_url, headers=headers)
        img.encoding = "gbk"
        img_data = BeautifulSoup(img.text, "html.parser")
        img_html = img_data.find(class_="photo-pic").find("img")
        pic_urls = f"http://pic.netbian.com/{img_html['src']}"
        pic = requests.get(url=pic_urls, headers=headers)
        print(f"开始下载{img_html['title']}")
        with open(f"bs4photos/{img_html['title']}.jpg", mode="wb") as f:
            f.write(pic.content)
        print(f"{img_html['title']}下载完成")
    print(f"第{i}页下载完成")
print("下载完成")