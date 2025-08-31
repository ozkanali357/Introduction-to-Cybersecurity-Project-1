from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    # Fix Flaw 4: A02:2021-Cryptographic Failures
    # use Django set_password and check_password methods
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

class InsecureDirectObjectReference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')

class BrokenAuthentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)

class CrossSiteScripting(models.Model):
    content = models.TextField()

class SQLInjection(models.Model):
    query = models.TextField()

class SecurityMisconfiguration(models.Model):
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField()