import logging
import time
import pytest
from base.base_analyse import analyse
from page.index_page import IndexPage
from page.login_page import LoginPage
from utils.driver_util import DriverUtil


class TestLogin:

    def setup(self):
        self.driver = DriverUtil.get_driver()
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.driver.get("http://localhost")

    def teardown(self):
        time.sleep(3)
        DriverUtil.quit_driver()

    @pytest.mark.parametrize("params", analyse("login_data.json"))
    def test_login(self, params):
        self.index_page.click_login_link()
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.input_verify_code(params["code"])
        self.login_page.click_login_btn()
        time.sleep(3)
        logging.info("用户名: {}---密码: {}---验证码: {}---预期结果: {}".format(params["username"], params["password"], params["code"], params["msg"]))
        assert params["msg"] == self.login_page.get_msg()

