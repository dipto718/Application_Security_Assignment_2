from django.test import TestCase, Client

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
		self.client = Client()
		
	def testCSRF(self):
		print()

# test that sqli is fixed
class SQLITestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		self.client = Client()
	
	def testSQLI(self):
		print()

# test that salts for passwords are different
class SALTTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		self.client = Client()
		
	def testSALT(self):
		print()
