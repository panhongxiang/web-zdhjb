from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):

    username_input = By.ID, "username"
    password_input = By.ID, "password"
    code_input = By.ID, "verify_code"
    login_btn = By.CLASS_NAME, "J-login-submit"
    msg = By.CLASS_NAME, "layui-layer-content"

    # 2. 输入用户名
    def input_username(self, username):
        return self.input(self.username_input, username)
    # 3. 输入密码
    def input_password(self, password):
        return self.input(self.password_input, password)
    # 4. 输入验证码
    def input_verify_code(self, code):
        return self.input(self.code_input, code)
    # 5. 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)
    # 6. 获取错误提示信息
    def get_msg(self):
        return self.find_el(self.msg).text
