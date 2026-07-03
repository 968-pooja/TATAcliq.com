class BaseClass:
    def __init__(self, driver):
        self.driver=driver
    def send_keys_method(self, locator, data):
        ele=(self.driver.find_element(*locator))
        ele.clear()
        ele.send_keys(data)
    def click_method(self, locator):
        ele=self.driver.find_element(*locator)
        ele.click()

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def get_text_method(self, locator):
        ele = self.driver.find_element(*locator)
        return ele.text