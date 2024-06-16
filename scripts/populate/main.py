from scripts.populate.user import generate_user_app_fake_data
from scripts.populate.product import generate_product_app_fake_data
from scripts.populate.order import generate_order_app_fake_data
from scripts.populate.payment import generate_payment_app_fake_data


def populate_all_data():
    #generate_user_app_fake_data(num_users = 200, num_address = 5)
    #generate_product_app_fake_data(num_root_category = 6, num_products_per_categories =200, num_options = 20)
    #generate_order_app_fake_data(num_shopping_card_per_user = 15)
    generate_payment_app_fake_data()
