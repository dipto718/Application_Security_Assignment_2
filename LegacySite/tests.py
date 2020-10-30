from django.test import TestCase, Client
from . import extras

# Create your tests here.

# test that xxs is fixed
class XXSTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		self.client = Client()
		
	def testXXS(self):
		response = self.client.get('/buy')
		self.assertEqual(response.status_code, 200)
		bad_script = '<p>Endorsed by <script>alert("hello")</script>!</p>'
		response = self.client.get('/buy.html?director=''<script>alert("hello")</script>''')
		#print(response.content)
		if bad_script in (response.content).decode():
			print("xxs attack works in buy\n")
		else:
			print("xxs attack failed in buy\n")
		response = self.client.get('/gift.html?director=''<script>alert("hello")</script>''')
		if bad_script in (response.content).decode():
			print("xxs attack works in gift\n")
		else:
			print("xxs attack failed in gift\n")

# test that csrf is fixed
class CSRFTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		# makes sure that the user is logged in
		# when the attacker try to make them
		# buy a giftcard
		self.client = Client()
		response = self.client.post('/login', {'uname' : 'abc123', 'pword' : 'abc123'})
		#print(response.status_code)
		if response.status_code == 200:
			print("user abc123 logged in ")
		# by default the test client disables any
		# any CSRF checks in the setting for the
		# website so this reenables them
		self.client = Client(enforce_csrf_checks=True)
		
	def testCSRF(self):
		
		response = self.client.post('/gift', {'username' : 'admin', 'amount' : 5000})
		if response.status_code == 200:
			print("and the csrf attack still works and sends a gift card to admin")
		else:
			print("and the csrf attack fails and does not sends a gift card to admin")

# test that sqli is fixed
class SQLITestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		self.client = Client()
		#response = self.client.post('/login', {'uname' : 'abc123', 'pword' : 'abc123'})
	
	def testSQLI(self):
		#with open('newcard.gftcrd') as card:
		#	card_data = card.read()
		try:
			card = open('newcard.gftcrd')
			response = self.client.post('/use', {'card_data' : card, 'card_supplied' : 'True', 'card_fname' : 'card'})
			admin_pword_hashed = "000000000000000000000000000078d2$18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3"
			#print(response.status_code)
			if admin_pword_hashed in response.content.decode():
				print("can still get admin hashed password so sqli attack still works\n")
		except:
			print("can't get admin hashed password so sqli attack fails\n")
		#print()

# test that salts for passwords are different
class SALTTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		self.client = Client()
		
	def testSALT(self):
		if extras.generate_salt(16) == extras.generate_salt(16):
			print("The salt is still weak since it is always the same\n")
		else:
			print("The salt is strong since it is now not always the same\n")
