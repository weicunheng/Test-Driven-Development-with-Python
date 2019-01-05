from selenium import webdriver


brower = webdriver.Firefox()

brower.get("http://172.16.1.61:8080")

assert 'Django' in brower.title
