class BaseObject:

	def to_dict(self):
		return vars(self)

	def __repr__(self):
		# Python > Other languages
		class_name = self.__class__.__name__
		attributes = ', '.join(f'{key}={value}' for key, value in vars(self).items())
		return f'{class_name}({attributes})'


class Product(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.name = json_data['name']
		self.visibility = json_data['visibility']
		self.created_at = json_data['created_at']
		self.experiences = json_data.get('experiences', None)
		self.plans = json_data.get('plans', None)


class Plan(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.product = json_data['product']
		self.plan_type = json_data['plan_type']
		self.release_method = json_data['release_method']
		self.visibility = json_data['visibility']
		self.billing_period = json_data['billing_period']
		self.internal_notes = json_data['internal_notes']
		self.metadata = json_data['metadata']
		self.direct_link = json_data['direct_link']
		self.renewal_price = json_data['renewal_price']
		self.initial_price = json_data['initial_price']
		self.base_currency = json_data['base_currency']
		self.requirements = json_data['requirements']
		self.release_method_settings = json_data['release_method_settings']
		self.accepted_payment_methods = json_data['accepted_payment_methods']
		self.stock = json_data['stock']
		self.unlimited_stock = json_data['unlimited_stock']
		self.created_at = json_data['created_at']
		self.access_pass = json_data['access_pass']
		self.card_payments = json_data['card_payments']


class Membership(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.product = json_data['product']
		self.user = json_data['user']
		self.plan = json_data['plan']
		self.promo_code = json_data.get('promo_code', None)
		self.email = json_data['email']
		self.stripe_subscription_id = json_data.get('stripe_subscription_id', None)
		self.stripe_customer_id = json_data.get('stripe_customer_id', None)
		self.status = json_data['status']
		self.valid = json_data['valid']
		self.cancel_at_period_end = json_data['cancel_at_period_end']
		self.payment_processor = json_data['payment_processor']
		self.license_key = json_data['license_key']
		self.metadata = json_data['metadata']
		self.quantity = json_data['quantity']
		self.wallet_address = json_data['wallet_address']
		self.custom_fields_responses = json_data['custom_fields_responses']

		self.discord_id = None
		self.discord_username = None
		self.discord_image_url = None

		if json_data['discord']:
			self.discord_id = json_data['discord'].get('id', None)
			self.discord_username = json_data['discord'].get('username', None)
			self.discord_image_url = json_data['discord'].get('image_url', None)
		self.expires_at = json_data['expires_at']
		self.renewal_period_start = json_data['renewal_period_start']
		self.renewal_period_end = json_data['renewal_period_end']
		self.created_at = json_data['created_at']
		self.manage_url = json_data['manage_url']
		self.affiliate_page_url = json_data['affiliate_page_url']
		self.checkout_session = json_data['checkout_session']
		self.access_pass = json_data['access_pass']
		self.telegram_account_id = json_data['telegram_account_id']


class Company(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.title = json_data['title']
		self.route = json_data['route']
		self.image_url = json_data['image_url']
		self.hostname = json_data['hostname']


class Payment(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.access_pass = json_data['access_pass']
		self.membership = json_data['membership']
		self.plan = json_data['plan']
		self.user = json_data['user']
		self.final_amount = json_data['final_amount']
		self.subtotal = json_data['subtotal']
		self.currency = json_data['currency']
		self.last4 = json_data['last4']
		self.last_payment_attempt = json_data['last_payment_attempt']
		self.next_payment_attempt = json_data['next_payment_attempt']
		self.payments_failed = json_data['payments_failed']
		self.payment_processor = json_data['payment_processor']
		self.refunded_amount = json_data.get('refunded_amount', None)
		self.refunded_at = json_data.get("refunded_at", None)
		self.status = json_data['status']
		self.wallet_address = json_data.get("wallet_address", None)


class CheckoutSession(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.redirect_url = json_data['redirect_url']
		self.affiliate_code = json_data['affiliate_code']
		self.metadata = json_data['metadata']
		self.plan_id = json_data['plan_id']
		self.purchase_url = json_data['purchase_url']


class Customer(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.username = json_data['username']
		self.email = json_data['email']
		self.profile_pic_url = json_data['profile_pic_url']
		self.social_accounts = json_data['social_accounts']
		self.roles = json_data.get("roles", None)


class PromoCode(BaseObject):
	def __init__(
		self,
		json_data: dict
	):
		self.id = json_data['id']
		self.created_at = json_data['created_at']
		self.amount_off = json_data['amount_off']
		self.base_currency = json_data['base_currency']
		self.code = json_data['code']
		self.expiration_datetime = json_data['expiration_datetime']
		self.new_users_only = json_data['new_users_only']
		self.number_of_intervals = json_data['number_of_intervals']
		self.plan_ids: list = json_data['plan_ids']
		self.promo_type = json_data['promo_type']
		self.status = json_data['status']
		self.stock = json_data['stock']
		self.uses = json_data['uses']
