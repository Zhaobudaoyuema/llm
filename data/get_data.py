import os
import requests
from bs4 import BeautifulSoup

# 目标网页URL列表
urls = [
    'https://geekdaxue.co/read/alisunstar@internet_terminology/vaeic4',
    # 'https://geekdaxue.co/read/alisunstar@internet_terminology/uou8ps',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/nqky1e',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/rtdoz4',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/vfrkie',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/zlkuy5',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/ykapux',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/te3wqy',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/dmwio8',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/xnwhwx',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/qdhkgb',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/mr9g07',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/yk10aw',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/uhg9vw',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/khwuyb',
    'https://geekdaxue.co/read/alisunstar@internet_terminology/khwuyb',
    # 其他URL可以添加到这个列表中
]

# 确保processing_data目录存在
if not os.path.exists('processing_data'):
    os.makedirs('processing_data')

# 遍历URL列表
for url in urls:
    # 发送HTTP请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取并打印body标签中的所有文本行
        for element in soup.body.find_all(text=True):
            # 打印非空行
            if element.strip():
                print(element.strip())
                print("#######\n")
    else:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")