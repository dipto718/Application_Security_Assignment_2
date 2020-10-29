from django.test import TestCase

# Create your tests here.

# test that xxs is fixed
class XXSTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		
	def testXXS(self):

# test that csrf is fixed
class CSRFTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		
	def testCSRF(self):

# test that sqli is fixed
class SQLITestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		
	def testSQLI(self):

# test that salts for passwords are different
class SALTTestCase(TestCase):
	fixtures = ['testdata.json']
	def setUp(self):
		
	def testSALT(self):
