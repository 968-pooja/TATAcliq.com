import pytest
from Pages.Add_to_cart_Page import AddToCart
from tests.conftest import fixture_func


def test_Addtocart(fixture_func):
    obj = AddToCart(fixture_func)
    obj.add_to_bag_method()

# def test_verifycart(fixture_func):
#     obj = AddToCart(fixture_func)
#     obj.add_to_bag_method()
#     actual = obj.verify_cart_item()
#     assert actual == "Monte Carlo Women's Teal Self Design Round Neck Full Sleeve Kurti Set with Bag"