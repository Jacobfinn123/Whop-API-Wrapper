# Whop-API-Wrapper

A simple python API wrapper of Whop's API, documentation can be found at: https://dev.whop.com/reference/home

## Installation

To install the package, use the following command:

```shell
pip install whop-api-wrapper
```

## Usage
Initialize the Client class with your token, use any api call as a method of the client.

```py
from whop_api_wrapper import Client

client = Client("input_token_here")

products = client.list_all_products()
for product in products:
    print(product)  # Product(id=product_id, name=product_name, visibility=visible, created_at=123, experiences=[], plans=[])

customer = client.retrieve_customer("customer_id_here")
print(customer)  # Customer(id=user_id, username=whop_username, email=email, profile_pic_url=url, social_accounts=[{'service': 'discord', 'username': 'discord_name#1234', 'id': '123'}], roles=None),

promo_code = client.create_promo_code(amount_off=25, base_currency="usd", code="25off", promo_type="flat_amount")
print(promo_code)  # PromoCode(id=promo_id, created_at=123, amount_off=100.0, base_currency=usd, code=100off, expiration_datetime=None, new_users_only=True, number_of_intervals=1, plan_ids=[], promo_type=percentage, status=active, stock=6, uses=2)
```

Feel free open any issues or report them to me on discord, `jacobfinn`.