from selenium import webdriver
import unittest


class NewVisitTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 首先，需要访问TO-DO首页
        self.browser.get("http://192.168.159.133:8080")

        # 查看网站标题中是否包含"TO-DO"
        self.assertIn("TO-DO",self.browser.title)

        self.fail(msg="完成测试")  # 提醒测试执行结束


if __name__ == '__main__':
    # 程序会在文件中，自动查找测试类和方法，然后运行
    unittest.main(warnings="ignore")
