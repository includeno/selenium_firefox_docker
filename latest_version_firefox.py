import requests

response = requests.get('https://product-details.mozilla.org/1.0/firefox_versions.json')
firefox_versions = response.json()

latest_version = firefox_versions['LATEST_FIREFOX_VERSION']
print("Latest Firefox version: ", latest_version)
#Latest Firefox version:  110.0.1

latest_version = firefox_versions['FIREFOX_ESR']
print("Latest Firefox ESR version: ", latest_version)
# 将版本号写入文件
with open('FIREFOX_ESR_VERSION', 'w') as f:
    f.write(f'FIREFOX_ESR_VERSION={latest_version}\n')


url = 'https://api.github.com/repos/mozilla/geckodriver/releases/latest'
response = requests.get(url)
data = response.json()

latest_version = data['tag_name']
print("Latest geckodriver version: ",latest_version)

# 将版本号写入文件
with open('GECKODRIVER_VERSION', 'w') as f:
    f.write(f'GECKODRIVER_VERSION={latest_version}\n')