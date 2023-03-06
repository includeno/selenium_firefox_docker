from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置Chrome浏览器选项
options = webdriver.FirefoxOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')

# 创建Chrome浏览器实例
driver = webdriver.Firefox(options=options)

# 打开Google网站
driver.get('https://www.baidu.com')

# 在Google搜索框中输入关键字并搜索
search_box = driver.find_element(By.ID,'kw')
search_box.send_keys('Selenium Python')
search_box.submit()

# 输出搜索结果页面标题
print(driver.title)

# 关闭浏览器实例
driver.quit()
