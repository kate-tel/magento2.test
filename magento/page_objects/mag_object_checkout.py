class Checkout(object):
    email = 'input#customer-email.input-text'
    password = 'input#customer-password.input-text'
    shipping_address = 'div[class="shipping-address-item selected-item"]'
    shipping_method_fixed = 'input.radio[name="ko_unique_2"]'
    next_button = 'button[class="button action continue primary"]'
    place_order = 'button[class="action primary checkout"]'
    order_number_demo = 'a[class="order-number"]>strong'
    product_name = 'strong[class="product name product-item-name"]'
    order_status = 'span[class="order-status"]'
    order_total = 'tr[class="grand totals"]>td>strong>span'
    grand_total_price = 'td[data-th="Grand Total"]>strong>span'
    first_name = 'input[name="firstname"]'
    last_name = 'input[name="lastname"]'
    street_address_1st_line = 'input[name="street[0]"]'
    city = 'input[name="city"]'
    zip_code = 'input[name="postcode"]'
    country = 'select[name="country_id"]'
    flat_shipping_method = 'td#label_method_bestway_tablerate.col.col-method'
    state = 'input[name="region"]'
    phone_num = 'input[name="telephone"]'
    price = 'td.amount>span'
    order_summary = 'div[class="opc-block-summary"]'
    create_account_button = 'a[class="action primary"]'
    order_number_guest = 'div[class="checkout-success"]>p>span'
