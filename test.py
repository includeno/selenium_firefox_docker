import requests

# 获取Geckodriver的最新发布版本信息
url = 'https://api.github.com/repos/mozilla/geckodriver/releases'
response = requests.get(url)
data = response.json()

# 获取倒数3个版本的版本字符串
versions = [release['tag_name'] for release in data]
latest_versions = versions[:3]
print('Latest geckodriver versions:', latest_versions)
