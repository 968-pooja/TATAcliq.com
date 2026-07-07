import pytest
from Pages.Add_to_cart_Page import AddToCart
from tests.conftest import fixture_func
from Pages.Wishlist_Page import WishList

def test_wishlist(fixture_func):
    obj = WishList(fixture_func)
    obj.add_to_bag_method()