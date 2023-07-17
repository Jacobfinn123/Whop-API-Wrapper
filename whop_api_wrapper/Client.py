import requests
from typing import List
from Objects import Product, Plan, Membership, Company, Payment, CheckoutSession, Customer, PromoCode
from Endpoints import Endpoints


# TODO: Expand does nothing ATM (has different options for each object)

class Client:
	def __init__(
		self,
		token: str,
		api_version: str = "v2"
	):
		self.token = token.replace("Bearer ", "")
		self.headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
		self.base_url = "https://api.whop.com/api/"
		self.api_version = api_version

		# Test token
		self._test_token()

	def _test_token(self):
		url = f"{self.base_url}{self.api_version}"
		response = requests.get(url, headers=self.headers)
		status_code = response.status_code

		if status_code == 401:
			raise Exception("Invalid token. Refer to https://dev.whop.com/reference/authentication", status_code)

	def _make_request(
		self,
		endpoint: str,
		request_method=requests.get,
		**kwargs
	) -> dict:

		url = f"{self.base_url}{self.api_version}{endpoint}"
		# Ensures at least authentication is being sent
		headers = kwargs.get('headers') or self.headers
		kwargs['headers'] = headers
		response = request_method(url, **kwargs)

		status_code = response.status_code
		if status_code == 400:
			raise Exception("Invalid parameters.", status_code)
		if status_code == 401:
			raise Exception("Invalid token. Refer to https://dev.whop.com/reference/authentication", status_code)
		elif status_code == 403:
			raise Exception("Forbidden.", status_code)
		elif status_code == 404:
			raise Exception("Endpoint or resource ID invalid.", status_code)
		elif status_code == 500:
			raise Exception("Internal sever error.")
		response_json = response.json()
		return response_json

	def _generate_params(
		self,
		**kwargs
	) -> dict:
		return self._generate_payload(**kwargs)

	@staticmethod
	def _generate_payload(
			**kwargs
	) -> dict:
		"""
		Generates a payload (or params) from a dict of the parameters in any given function
		:return:
		"""
		return {key: value for key, value in kwargs.items() if value is not None}

	def _list_all(
		self,
		endpoint: str,
		class_type,
		params: dict,
		start_page: int = None,
		stop_page: int = None
	):
		"""
		:param class_type: The object your are listing IE "Product" for listing all products
		:param params: The query/params sent with the request
		:return: List[class_type]
		"""
		current_page = start_page or 1
		end_page = stop_page or 1e9
		all_data = []

		while current_page < end_page:
			# Ensures pagination is included with params.
			params['page'] = current_page
			params['per'] = 50
			response_json = self._make_request(endpoint, params=params)
			current_page = response_json['pagination']['current_page']
			end_page = response_json['pagination']['total_page']
			for data in response_json['data']:
				all_data.append(class_type(data))

			current_page += 1

		return all_data

	# < --------- PRODUCTS ---------- >

	def list_all_products(
		self,
		visibility: str = None,
		expand: bool = False,
		start_page: int = None,
		stop_page: int = None
	) -> List[Product]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.PRODUCTS, Product, params, start_page, stop_page)

	def retrieve_product(
		self,
		product_id: str,
		expand: bool = False
	) -> Product:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.PRODUCTS + product_id, params=params)
		return Product(response_json)

	def update_product(
		self,
		product_id: str,
		name: str = None,
		one_per_user: bool = None,
		visibility: str = None,
		shuffleable: bool = None,
	) -> Product:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.PRODUCTS + product_id, request_method=requests.post, json=payload)
		return Product(response_json)

	# < --------- PRODUCTS ---------- >

	# < --------- PLANS ---------- >
	def list_all_plans(
		self,
		visibility: str = None,
		product_id: str = None,
		expand: bool = False,
		start_page: int = None,
		stop_page: int = None
	) -> List[Plan]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.PLANS, Plan, params, start_page, stop_page)

	def create_plan(
		self,
		product_id: str = None,
		plan_type: str = None,
		allow_multiple_quantity: bool = None,
		base_currency: str = None,
		billing_period: int = None,
		coinbase_commerce_accepted: bool = None,
		custom_fields: list = None,
		expiration_days: int = None,
		grace_period_days: int = None,
		initial_price: float = None,
		internal_notes: str = None,
		one_per_user: bool = None,
		pegged_currencies: list = None,
		release_method: bool = None,
		release_method_settings: dict = None,
		renewal_price: bool = None,
		requirements: dict = None,
		short_link: str = None,
		stock: str = None,
		trial_period_days: str = None,
		unlimited_stock: bool = None,
		visibility: str = None,
		metadata: dict = None,
	) -> Plan:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.PLANS, request_method=requests.post, json=payload)
		return Plan(response_json)

	def retrieve_plan(
		self,
		plan_id: str,
		expand: bool = False
	) -> Plan:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.PRODUCTS + plan_id, params=params)
		return Plan(response_json)

	def create_quick_link(
		self,
		plan_id: str,
		expand: bool = False,
		internal_notes: str = None,
		short_link: str = None,
		custom_password: str = None,
		stock: int = None,
		trial_period_days: int = None,
		metadata: dict = None,
		requirements: dict = None,
	) -> Plan:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.PLANS, request_method=requests.post, json=payload)
		return Plan(response_json)

	# < --------- PLANS ---------- >

	# < --------- MEMBERSHIPS ---------- >

	def list_all_memberships(
		self,
		status: str = None,
		plan_id: str = None,
		product_id: str = None,
		user_id: str = None,
		discord_id: str = None,
		wallet_address: str = None,
		valid: bool = None,
		hide_metadata: bool = None,
		expand: bool = False,
		start_page: int = None,
		stop_page: int = None
	) -> List[Membership]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.MEMBERSHIPS, Membership, params, start_page, stop_page)

	def retrieve_membership(
		self,
		membership_id: str,
		expand: bool = False
	) -> Membership:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, params=params)
		return Membership(response_json)

	def update_membership(
		self,
		membership_id: str,
		metadata: dict,
		expand: bool = None
	) -> Membership:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, request_method=requests.post, json=payload)
		return Membership(response_json)

	def add_days_to_membership(
		self,
		membership_id: str,
		days: int,
		expand: bool = None
	) -> Membership:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, request_method=requests.post, json=payload)
		return Membership(response_json)

	def terminate_membership(
		self,
		membership_id: str,
		expand: bool = None
	) -> Membership:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, request_method=requests.post, json=payload)
		return Membership(response_json)

	def cancel_membership(
		self,
		membership_id: str,
		expand: bool = None
	) -> Membership:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, request_method=requests.post, json=payload)
		return Membership(response_json)

	def validate_license(
		self,
		membership_id: str,
		metadata: dict,
		expand: bool = None
	) -> Membership:
		"""
		:param membership_id: mem_id or License
		:param metadata: A polymorphic object containing information that can be user defined
		:param expand: Whether or not to expand the User, Plan, Product, or Promo Code on the returned Membership(s). Pass an array with each object(s) you want to expand, e.g. [product, plan, user, promo_code]
		:return: Membership object
		"""
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.MEMBERSHIPS + membership_id, request_method=requests.post, json=payload)
		return Membership(response_json)

	# < --------- MEMBERSHIPS ---------- >

	# < --------- COMPANIES ---------- >

	def retrieve_company(
		self,
	) -> Company:
		response_json = self._make_request(Endpoints.COMPANIES)
		return Company(response_json)

	# < --------- COMPANIES ---------- >

	# < --------- PAYMENTS ---------- >

	def list_all_payments(
		self,
		status: str = None,
		membership_id: str = None,
		expand: bool = None,
		start_page: int = None,
		stop_page: int = None
	) -> List[Payment]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.PAYMENTS, Payment, params, start_page, stop_page)

	def retrieve_payment(
		self,
		payment_id: str,
		expand: bool = False
	) -> Payment:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.PAYMENTS + payment_id, params=params)
		return Payment(response_json)

	# < --------- PAYMENTS ---------- >

	# < --------- CHECKOUT SESSIONS ---------- >

	def list_all_checkout_sessions(
		self,
		status: str = None,
		membership_id: str = None,
		expand: bool = None,
		start_page: int = None,
		stop_page: int = None
	) -> List[CheckoutSession]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.CHECKOUT_SESSION, CheckoutSession, params, start_page, stop_page)

	def create_checkout_session(
		self,
		plan_id: str,
		affiliate_code: str = None,
		redirect_url: str = None,
		metadata: dict = None
	) -> CheckoutSession:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.CHECKOUT_SESSION, request_method=requests.post, json=payload)
		return CheckoutSession(response_json)

	def retrieve_checkout_session(
		self,
		checkout_session_id: str
	) -> CheckoutSession:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.CHECKOUT_SESSION + checkout_session_id, params=params)
		return CheckoutSession(response_json)

	def delete_checkout_session(
		self,
		checkout_session_id: str
	) -> CheckoutSession:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.CHECKOUT_SESSION + checkout_session_id, request_method=requests.delete, params=params)
		return CheckoutSession(response_json)

	# < --------- CHECKOUT SESSIONS ---------- >

	# < --------- CUSTOMERS ---------- >

	def list_all_customers(
		self,
		start_page: int = None,
		stop_page: int = None
	) -> List[Customer]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.CUSTOMERS, Customer, params, start_page, stop_page)

	def retrieve_customer(
		self,
		customer_id: str
	) -> Customer:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.CUSTOMERS + customer_id, params=params)
		return Customer(response_json)

	# < --------- CUSTOMERS ---------- >

	# < --------- PROMO CODES ---------- >

	def list_all_promo_codes(
		self,
		status: str = None,
		expand: bool = None,
		start_page: int = None,
		stop_page: int = None
	) -> List[PromoCode]:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		return self._list_all(Endpoints.PROMO_CODES, PromoCode, params, start_page, stop_page)

	def create_promo_code(
		self,
		amount_off: float,
		base_currency: str,
		code: str,
		promo_type: str,
		expiration_date: int = None,
		new_users_only: bool = None,
		number_of_intervals: int = None,
		plan_ids: list = None,
		stock: int = None,
		unlimited_stock: bool = None,
		metadata: dict = None
	) -> PromoCode:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.PROMO_CODES, request_method=requests.post, json=payload)
		return PromoCode(response_json)

	def retrieve_promo_code(
		self,
		promo_code_id: str,
		expand: bool = None
	) -> PromoCode:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.PROMO_CODES + promo_code_id, params=params)
		return PromoCode(response_json)

	def update_promo_code(
		self,
		promo_code_id: str,
		plan_ids: list = None,
		stock: int = None,
		unlimited_stock: bool = None,
		metadata: dict = None,
		expand: bool = None
	) -> PromoCode:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		payload = self._generate_payload(**parameters)
		response_json = self._make_request(Endpoints.PROMO_CODES + promo_code_id, request_method=requests.post, json=payload)
		return PromoCode(response_json)

	def delete_promo_code(
		self,
		promo_code_id: str,
	) -> PromoCode:
		parameters = {name: value for name, value in locals().items() if name != 'self'}
		params = self._generate_params(**parameters)
		response_json = self._make_request(Endpoints.PROMO_CODES + promo_code_id, request_method=requests.delete, params=params)
		return PromoCode(response_json)
	# < --------- PROMO CODES ---------- >
