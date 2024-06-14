from django.db import models

# Create your models here.
class EmailOTP(models.Model) :
	username = models.CharField(max_length=60)
	otp = models.IntegerField()

	def __self__(self) :
		return self.username