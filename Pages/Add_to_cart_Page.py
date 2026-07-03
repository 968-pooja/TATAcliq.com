from Pages.Base_Page import BaseClass
from selenium.webdriver.common.keys import Keys
from time import sleep

# from selenium import webdriver
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('detach', True)
# opt.add_argument('--disable-notifications')
# driver=webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get("https://www.tatacliq.com/")


class AddToCart(BaseClass):

        notf = ('id', "moe-dontallow_button")
        search_bar=('id',"search-text-input")
        select_item=('css selector', 'div[class="SearchResultItem__base"]')
        item=('css selector', 'a[aria-label="Monte Carlo"]')
        #move to window next switching
        size=('id',"pdpSize-M")
        add_to_bag=('xpath', '//button[text()="Add To Bag"]')
        go_to_bag=('xpath', '//button[text()="Go To Bag"]')
        # cart_bag=('css selector', 'div[aria-label="Go to Cart  with 3 items"]')
        verify_item=('xpath', "//div[text()='Monte Carlo Women's Teal Self Design Round Neck Full Sleeve Kurti Set with Bag']")

        def add_to_bag_method(self):
            self.send_keys_method(self.search_bar, "Kurti")
            sleep(3)
            self.click_method(self.select_item)
            sleep(3)
            self.click_method(self.item)
            self.switch_to_new_window()
            sleep(2)
            self.click_method(self.size)
            sleep(2)
            self.click_method(self.add_to_bag)
            sleep(2)
            self.click_method(self.go_to_bag)

        # def verify_cart_item(self):
        #     return self.get_text_method(self.verify_item)

# obj = AddToCart(driver)
# obj.add_to_bag_method()
