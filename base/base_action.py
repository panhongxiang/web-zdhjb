class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(feature[0], feature[1])

    def find_els(self, feature):
        return self.driver.find_elements(feature[0], feature[1])

    def click(self, feature):
        return self.find_el(feature).click()

    def clear(self, feature):
        return self.find_el(feature).clear()

    def input(self, feature, content):
        return self.find_el(feature).send_keys(content)