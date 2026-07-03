from Pages.Base_Page import BaseClass
from selenium.webdriver.common.keys import Keys
from time import sleep

class WishList(BaseClass):
    notf = ('id', "moe-dontallow_button")
    search_bar = ('id', "search-text-input")
    select_item = ('css selector', 'div[class="SearchResultItem__base"]')
    item = ('css selector', 'a[aria-label="Monte Carlo"]')
    # move to window next switching
    size = ('id', "pdpSize-M")
    wishlist_btn = ('xpath', '(//div[@class="Icon__image"])[11]')
    mobile_no=('id',"mobileNumber")
    continue_btn=('id',"continueBtn")
    go_to_wishlist = ('xpath', '(//div[@role="button"])[10]')

    # verify_item = ('xpath',
    #                "//div[text()='Monte Carlo Women's Teal Self Design Round Neck Full Sleeve Kurti Set with Bag']")

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
        self.click_method(self.wishlist_btn)
        sleep(2)
        # self.send_keys_method(self.mobile_no, "9686864732")
        # sleep(2)
        # self.click_method(self.continue_btn)
        # sleep(5)
        # #Otp Enter-manually
        # self.click_method(self.go_to_wishlist)
        # sleep(2)