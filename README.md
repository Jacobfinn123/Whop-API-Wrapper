# Whop-API-Wrapper

A simple python API wrapper of Whop's API, documentation can be found at: https://dev.whop.com/reference/home

## Installation

To install the package, use the following command:

```shell
pip install whop-api-wrapper
```

## Usage
Initialize the Client class with your token, use any api call as a method of the client.

```shell
client = Client("input_token_here")

client.list_all_products()
client.retrieve_membership("membership_id_here")
client.create_promo_code(amount_off=25, base_currency="usd", code="25off", promo_type="flat_amount")
```

Feel free open any issues or report them to me on discord, `jacobfinn`.