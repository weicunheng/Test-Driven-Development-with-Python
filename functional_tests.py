from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.assertIn("TO-DO", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual(header_text, "TO-DO")

        # 应用邀请他输入一个代办事项
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "请添加待办事项")
        # 他在一个文本框中输入了 Hello World
        inputbox.send_keys("明天加班")

        # 他按了回车键，页面进行了刷新
        inputbox.send_keys(Keys.ENTER)

        # 页面刷新，显示一个表格
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any(row.text == "1:明天加班" for row in rows))

        self.fail(msg="完成测试")  # 提醒测试执行结束


if __name__ == '__main__':
    # 程序会在文件中，自动查找测试类和方法，然后运行
    unittest.main(warnings="ignore")
