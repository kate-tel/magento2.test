class MainPage(object):
    new_collection = '//span[contains(text(), "Shop New Yoga")]'
    show_cart = 'a[class="action showcart"]'
    view_cart = 'a[class="action viewcart"]'
    search_input = 'input#search.input-text'
    women = '//a[@href="https://magento2.test/women.html"]'
    women_tops = '//a[@href="https://magento2.test/women/tops-women.html"]'
    gear = '//a[@href="https://magento2.test/gear.html"]'
    watches = '//a[@href="https://magento2.test/gear/watches.html"]'
    men = '//a[@href="https://magento2.test/men.html"]'
    tops = '//a[@href="https://magento2.test/men/tops-men.html"]'
    account_menu = 'button.action.switch'


class CreateAccount(object):
    email_field = 'input#email_address'
    lastname_field = 'input#lastname'
    firstname_field = 'input#firstname'
    password_field = 'input#password'
    confirm_password = 'input#password-confirmation'
    submit_account = 'button.action.submit.primary'


class AccountPage(object):
    menu = 'div.sidebar.sidebar-main'
    order = 'td.col.id'
    ship_to = 'td.col.shipping'
    order_total = 'td.col.total>span'
    order_status = 'td.col.status'


class SignInPage(object):
    sign_in_button = 'button.action.login.primary'
    email_field = 'input#email'
    password_field = 'input#pass'
