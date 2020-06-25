from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
import pytest
from mag_object import MainPage, CreateAccount, AccountPage, SignInPage
from mag_object_catalog import Catalog
from mag_object_cart import Cart
from mag_object_checkout import Checkout
import random
import string


# Generate random email address for account creation
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


class MagentoTestClass(BaseCase):

    def setUp(self):
        super(MagentoTestClass, self).setUp()
        self.base_url = 'https://magento2.test'
        self.maximize_window()

    @pytest.mark.search
    def test_search_suggestions(self):
        # This test checks that:
        # search engine gives suggestions based on user input.

        self.get(self.base_url)
        self.update_text(MainPage.search_input, "backpak\n")
        self.assert_text_visible('Your search returned no results.',
                                 Catalog.suggestions)
        self.click(Catalog.suggestion)
        self.assert_exact_text("Search results for: 'backpack'", 'span.base')
        self.click_if_visible(Catalog.product_item)

    @pytest.mark.search_fail
    def test_search_fail(self):
        # This test checks that:
        # Query length less than 3 characters returns no results.

        self.get(self.base_url)
        self.update_text(MainPage.search_input, "at\n")
        self.assert_text_visible('Minimum Search query length is 3',
                                 Catalog.suggestions)
        self.assert_element_absent(Catalog.suggestion)

    @pytest.mark.wish_list
    def test_add_to_wish_list(self):
        # This test checks that:
        # - items are added to compare list;
        # - items are deleted from the compare list;
        # - items can not be added to the wish list unless signed in;
        # - items are added to the wish list after sigh in.

        # Add items to compare list
        self.get(self.base_url)
        self.update_text(MainPage.search_input, "red tee\n")
        self.click(Catalog.product_item)
        self.click(Catalog.add_to_compare)
        self.assert_element(Catalog.compare_prodcuts)
        self.go_back()
        self.go_back()
        self.click(Catalog.product_item_4th)
        self.click(Catalog.add_to_compare)
        self.click_link_text('comparison list')

        # Delete item from the list
        self.click_nth_visible_element(Cart.delete, 2)
        self.click(Cart.confirm)

        # Add item to wish list
        self.click(Catalog.add_to_wishlist)
        self.assert_text_visible('''You must login or register to add items to your wishlist.''')
        self.update_text(SignInPage.email_field, 'roni_cost@example.com\n')
        self.update_text(SignInPage.password_field, 'roni_cost3@example.com')
        self.click(SignInPage.sign_in_button)
        self.assert_text(' has been added to your Wish List.')

    @pytest.mark.cart
    def test_add_to_cart_and_delete_in_cart(self):
        # This test checks that:
        # - product is added to cart;
        # - item is updated in cart page;
        # - cart items are retained in cart after a leave;
        # - items are deleted from the cart.

        # Add product to cart
        self.get(self.base_url)
        self.click_xpath(MainPage.new_collection)
        self.click(Catalog.product_item)
        self.click(Catalog.add_to_cart)

        # Update cart
        self.click_link_text('shopping cart')
        self.click(Cart.edit)
        self.update_text(Cart.quantity_field, '2\n')

        # Leave shop
        self.open('://facebook.com')
        self.get(self.base_url)

        # View cart and delete items
        self.wait_for_element(Cart.is_upgraded)
        self.click(MainPage.show_cart)
        self.click(MainPage.view_cart)
        self.click(Cart.delete_item)
        self.assert_text_visible('You have no items in your shopping cart.')

    @pytest.mark.minicart
    def test_add_to_cart_and_delete_in_minicart(self):
        # This test checks that:
        # - product is added to cart;
        # - item is updated in minicart;
        # - items are deleted from minicart.

        # Navigate to product
        self.get(self.base_url)
        self.hover_and_click(MainPage.women, MainPage.women_tops)
        self.click_chain([Catalog.category, Catalog.jackets], spacing=0.5)
        self.click_nth_visible_element(Catalog.product_item, 3)

        # Add product to cart
        self.click_chain([Catalog.size_option_xs,
                          Catalog.color_option_first,
                          Catalog.add_to_cart],
                         spacing=0.5)

        # Inspect minicart
        self.scroll_to(MainPage.show_cart)
        self.wait_for_element(Cart.is_upgraded)
        self.click(MainPage.show_cart)
        price_one_piece = self.get_text(Cart.subtotal)

        # Update order in minicart
        self.find_element(Cart.quantity).send_keys(Keys.BACKSPACE)
        self.update_text(Cart.quantity, '2\n')
        self.click(Cart.update)
        self.wait_for_text('2', Cart.number_of_items)
        price_two_pieces = self.get_text(Cart.subtotal)

        # Assert order is updated
        self.assert_equal(
            float(price_two_pieces[1:-1]),
            float(price_one_piece[1:]) * 2)

        # Delete order
        self.click_chain([Cart.delete, Cart.confirm], spacing=0.5)
        self.assert_text_visible('You have no items in your shopping cart.')

    @pytest.mark.checkout_demo_user
    def test_checkout_demo_user(self):
        # This test checks that:
        # - item can be added to cart from catalog page;
        # - user can sign in into his account when he starts check-in process;
        # - order can be placed;
        # - placed order information corresponds expected;
        # - order info is retained after log out.

        # Navigate to catalog
        self.get(self.base_url)
        self.hover_and_click(MainPage.gear, MainPage.watches)

        # Get item name
        item_name = self.get_attribute(Catalog.luma_watch_photo, 'alt')
        self.assert_equal(item_name, 'Luma Analog Watch')

        # Add to cart
        self.hover_and_click(Catalog.luma_watch_photo,
                             Catalog.add_to_cart_button)
        self.click_link_text('shopping cart')

        # Compare item_name with item_in_cart_name
        item_in_cart_name = self.get_attribute(Cart.luma_watch_photo, 'alt')
        self.assert_equal(item_name, item_in_cart_name)
        self.click(Cart.proceed_to_checkout_button)

        # Shipping page
        self.update_text(Checkout.email, 'roni_cost@example.com\n')
        self.update_text(Checkout.password, 'roni_cost3@example.com\n')
        self.wait_for_element(Checkout.shipping_address)
        self.click(Checkout.shipping_method_fixed)
        self.click(Checkout.next_button)

        # Review & Payments page
        order_total = self.get_text(Checkout.order_total)
        self.click(Checkout.place_order)
        self.wait_for_text('Thank you for your purchase!')

        # Inspect order
        order_number = self.get_text(Checkout.order_number_demo)
        self.click(Checkout.order_number_demo)
        self.assert_equal(item_in_cart_name,
                          self.get_text(Checkout.product_name))
        self.assert_equal(self.get_text(Checkout.order_status), 'PENDING')
        self.assert_equal(order_total,
                          self.get_text(Checkout.grand_total_price))
        self.click_link_text('Print Order')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assert_title('Order # %s' % order_number)
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Sign out
        self.click(MainPage.account_menu)
        self.click_link_text('Sign Out')

        # Sign In and View order
        self.click_partial_link_text('Sign In')
        self.update_text(SignInPage.email_field, 'roni_cost@example.com\n')
        self.update_text(SignInPage.password_field, 'roni_cost3@example.com')
        self.click(SignInPage.sign_in_button)
        self.click_link_text('My Orders')
        self.assert_text(order_number)

        # Sign out
        self.click(MainPage.account_menu)
        self.click_link_text('Sign Out')

    @pytest.mark.checkout_as_guest
    def test_checkout_as_guest(self):
        # This test check that:
        # - customer can place an order as a guest with interruptions
        # (leaving the web shop and returning again to continue);
        # - customer can sign up after order has been placed;
        # - customer can view his order in his account.
        # It is preferrable to run this test method with
        # "--settings_file=<your_path_to_this_repo>/mag_tests/custom_settings.py>"
        # because page elements load time may vary.

        # Navigate to catalog
        self.get(self.base_url)
        self.hover_and_click(MainPage.men, MainPage.tops)

        # Go to product page
        self.click(Catalog.product_item_2nd)
        product_price = self.get_text(Catalog.product_price)
        # self._print(product_name)
        # self._print(product_price)
        self.click_chain([Catalog.size_option_xs,
                          Catalog.color_option_first],
                         spacing=1)
        self.click(Catalog.add_to_cart)
        self.wait_for_element(Cart.is_upgraded)
        self.click_chain([MainPage.show_cart,
                          Catalog.minicart_to_checkout],
                         spacing=1)

        # Checkout page
        email = random_char(7)+"@1secmail.net"
        self.update_text(Checkout.email, email+"\n")
        self.update_text(Checkout.first_name, 'Willem-Alexander Claus George')
        self.update_text(Checkout.last_name, 'Ferdinand')
        self.update_text(Checkout.street_address_1st_line, 'Noordeinde 64')
        self.update_text(Checkout.city, 'The Hague')
        self.update_text(Checkout.zip_code, '2514 GK')
        self.select_option_by_text(Checkout.country, 'Netherlands')
        self.wait_for_element_not_present(Checkout.flat_shipping_method)

        # Interruption
        self.open('://facebook.com')
        self.get(self.base_url)

        self.click_chain([MainPage.show_cart,
                          Catalog.minicart_to_checkout],
                         spacing=1)
        self.update_text(Checkout.state, 'South Holland')
        self.update_text(Checkout.phone_num, '+31976901561')
        self.click(Checkout.next_button)

        # Review & Payments page
        self.wait_for_text('Willem-Alexander Claus George Ferdinand')
        self.assert_equal(product_price, self.get_text(Checkout.price))
        self.assert_element(Checkout.order_summary)
        order_total = self.get_text(Checkout.order_total)
        self.click(Checkout.place_order)

        # After order page
        self.assert_text('Thank you for your purchase!')
        order_number = self.get_text(Checkout.order_number_guest)
        self.wait_for_element(Checkout.create_account_button)
        self.click(Checkout.create_account_button)

        # Account create page
        self.assert_equal(
            self.get_attribute(
                CreateAccount.email_field, 'value'),
            email)
        self.assert_equal(
            self.get_attribute(
                CreateAccount.lastname_field, 'value'),
            'Ferdinand')
        self.assert_equal(
            self.get_attribute(
                CreateAccount.firstname_field, 'value'),
            'Willem-Alexander Claus George')
        self.update_text(CreateAccount.password_field, 'kingFerdinand2020')
        self.update_text(CreateAccount.confirm_password, 'kingFerdinand2020')
        self.click(CreateAccount.submit_account)

        # View placed order
        self.assert_text('Thank you for registering with Main Website Store.')
        self.assert_element(AccountPage.menu)
        self.click_link_text('My Orders')
        self.assert_equal(self.get_text(AccountPage.order), order_number)
        self.assert_equal(
            self.get_text(
                AccountPage.ship_to),
            'Willem-Alexander Claus George Ferdinand')
        self.assert_equal(self.get_text(AccountPage.order_total), order_total)
        self.assert_equal(self.get_text(AccountPage.order_status), 'Pending')

        # Log Out
        self.click(MainPage.account_menu)
        self.click_link_text('Sign Out')

    @pytest.mark.incorrect_password
    def test_incorrect_password(self):
        # This test checks that:
        # A message is displayed upon incorrect password input when login.

        # Log in with incorrect password
        self.get(self.base_url)
        self.click_partial_link_text('Sign In')
        self.update_text(SignInPage.email_field, 'roni_cost@example.com\n')
        self.update_text(SignInPage.password_field, '12345678')
        self.click(SignInPage.sign_in_button)
        self.assert_text(
            'The account sign-in was incorrect or your account is disabled')

        # Log in with correct password
        self.update_text(SignInPage.password_field, 'roni_cost3@example.com')
        self.click(SignInPage.sign_in_button)

        # Log Out
        self.click(MainPage.account_menu)
        self.click_link_text('Sign Out')

    def tearDown(self):
        # self.addCleanup(MagentoTestClass.test_checkout_as_guest())
        super(MagentoTestClass, self).tearDown()
