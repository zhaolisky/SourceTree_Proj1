from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    display_button = By.XPATH, "//*[contains(@text,'显示')]"

    search_button = By.ID, "com.android.settings:id/search"

    search_edit_text = By.ID, "android:id/search_src_text"

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_search(self, text):
        self.input(self.search_edit_text, text)















    # 需求 ：
        # 第一个文件夹 新建 文件夹 新建文件
        # 第二个文件夹 新建 文件夹 新建文件

    # test_file
        # def test_first()
            # filepage . 新建文件夹
            # filepage . 新建文件
        # def test_second()
            # filepage . 新建文件
            # filepage . 新建文件夹
        # def test_second()


    # file_page
        # 点击 新建文件
            # 点击 新建文件
        # 点击 新建文件夹
            # 点击 新建文件
        # 输入 文本框内容
            # 输入 文本框内容
        # 点击 确定
            # 点击 确定
        # 点击 取消
            # 点击 取消

        # 新建文件夹
            # 点击 新建文件夹
            # 输入 文本框内容
            # 点击 确定

        # 新建文件
            # 点击 新建文件
            # 输入 文本框内容
            # 点击 确定

