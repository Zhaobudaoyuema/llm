import requests
from bs4 import BeautifulSoup
import re

# 目标网页URL
url = 'https://geekdaxue.co/read/alisunstar@internet_terminology/ghgfbg'

# 发送HTTP请求，获取网页内容
response = requests.get(url)
web_content = response.text

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(web_content, 'html.parser')

# 找到包含术语解释的段落，假设术语列表在无序列表<ul>中，每个术语是一个<li>元素
list_items = soup.select('ul li')

# 用于存储和组织输出的字典
terminology_dict = {}

# 遍历列表项，提取术语编号和解释
for item in list_items:
    # 提取术语编号，假设编号格式为"1."、"2."等
    match = re.search(r'^(\d+[.、])\s', item.get_text())
    if match:
        term_number = match.group(1)
        # 提取术语解释，去除编号和可能的图片链接
        explanation = re.sub(r'^(\d+[.、]\s)|!\[.*?\]\(.*?\)', '', item.get_text())
        terminology_dict[term_number] = explanation.strip()

# 打印输出结果
for term_number, explanation in terminology_dict.items():
    print(f"{term_number} **{explanation}**")
