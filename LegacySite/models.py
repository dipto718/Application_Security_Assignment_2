from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.backends import BaseBackend

from django_cryptography.fields import encrypt

from . import extras

keys = ['','','','']

try:
	secret_keys = open('remote_keys.txt', 'r')
	# if you have the remote_keys file then you
	# uncomment the following lines and put the 
        # the keys as written here corresponding to
	# their line position in the file

	# otherwise the keys are commented out
	keys[0] = b'\x8b\xdfX-\xea\xb4u\x94L\t\x9f\xa2Rq\xa0D\x81\xfd\xa8\xd3\xf4R.O\xda\xe3\xbc\xe4\xd1Fh*'
	keys[1] = b'\xce8W\x04\xb3A\x86\xe5+\x85F\xd2-8\xe3\xf2\xaa\x08x\xf4\x00\xfe\x9enC \x9d\xb1u\x8e\xae\xdb'
	keys[2] = b'\x14R\xfak\xbf\xbe\x1b\x06\xd5>\x01\xd3\x91\x9d\x03\xf1\xcf\xc3\xd1a\x9e\xbb\x83\xac5q\x1b\xa7\xfa\x10\x99?'
except IOError:
	print("The remote keys are not here so encryption can't be done")
	sys.exit()
	

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=97)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

class OurBackend(BaseBackend):
    def authenticate(self, request, username, password):
        assert(None not in [username, password])
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        pwrd_valid = extras.check_password(user, password)
        if pwrd_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50, unique=True)
    product_image_path = models.CharField(max_length=100, unique=True)
    recommended_price = models.IntegerField()
    description = models.CharField(max_length=250)

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    data = encrypt(models.BinaryField(unique=True), keys[0])
    product = models.ForeignKey('LegacySite.Product', on_delete=models.CASCADE, default=None)
    amount = encrypt(models.IntegerField(), keys[1])
    fp = encrypt(models.CharField(max_length=100, unique=True), keys[2])
    user = models.ForeignKey('LegacySite.User', on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
