import requests
from bs4 import BeautifulSoup
import argparse

def get_latest_firefox_esr_version():
    response = requests.get('https://product-details.mozilla.org/1.0/firefox_versions.json')
    firefox_versions = response.json()
    # latest_version = firefox_versions['LATEST_FIREFOX_VERSION']
    # print("Latest Firefox version: ", latest_version)
    #Latest Firefox version:  110.0.1
    latest_version = firefox_versions['FIREFOX_ESR']
    print("Latest Firefox ESR version: ", latest_version)
    return latest_version

FIREFOX_ESR_VERSION=get_latest_firefox_esr_version()
# 将版本号写入文件
with open('FIREFOX_ESR_VERSION', 'w') as f:
    f.write(f'Latest FIREFOX_ESR_VERSION={FIREFOX_ESR_VERSION}\n')

def get_latest_geckodriver_version():
    url = 'https://api.github.com/repos/mozilla/geckodriver/releases/latest'
    response = requests.get(url)
    data = response.json()
    #print(data)

    latest_version = data['tag_name']
    print("Latest geckodriver version: ",latest_version)
    return latest_version
GECKODRIVER_VERSION=get_latest_geckodriver_version()

# 将版本号写入文件
with open('GECKODRIVER_VERSION', 'w') as f:
    f.write(f'GECKODRIVER_VERSION={GECKODRIVER_VERSION}\n')

with open('FIREFOX_ESR_VERSION', 'w') as f:
    f.write(f'FIREFOX_ESR_VERSION={FIREFOX_ESR_VERSION}\n')


argparse.ArgumentParser(description='Get the latest version of the specified language')
parser = argparse.ArgumentParser()
parser.add_argument('--lang', type=str, default='python', help='language')
parser.add_argument('--tag', type=str, default='slim-buster', help='tag')
args = parser.parse_args()

def get_tag_by_lang(lang):
    #查询仓库最新版本
    response = requests.get('https://github.com/includeno/selenium_firefox_docker/tags')
    html = response.content

    soup=BeautifulSoup(html, 'html.parser')
    html = soup.prettify()
    tags=soup.select('a[href^="/includeno/selenium_firefox_docker/releases/tag/"]')
    for tag in tags:
        if(str(tag.text).startswith(lang)):
            return tag.text
    return ""

current_tag=get_tag_by_lang(args.lang)
print("Current Tag: ", current_tag)
NEW_TAG=args.lang+"_firefox_"+FIREFOX_ESR_VERSION+"_geckodriver_"+GECKODRIVER_VERSION+"_"+args.tag
with open('NEW_TAG', 'w') as f:
    f.write(f'NEW_TAG={NEW_TAG}\n')

IS_NEW=False
if(current_tag==NEW_TAG):
    IS_NEW=False
    with open('IS_NEW', 'w') as f:
        f.write(f'IS_NEW={False}\n')
else:
    IS_NEW=True
    with open('IS_NEW', 'w') as f:
        f.write(f'IS_NEW={True}\n')
print("IS_NEW:", IS_NEW)