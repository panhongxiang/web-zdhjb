from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class IndexPage(BaseAction):

    login_link = By.CLASS_NAME, "red"

    # 1. 点击首页的 ‘登录’ 链接，进入登录页面
    def click_login_link(self):
        return self.click(self.login_link)