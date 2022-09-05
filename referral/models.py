from django.db import models
import uuid
from django.urls import reverse


class Referral(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	bemor = models.CharField(max_length=45)
	birthdate = models.CharField(max_length=50)
	address = models.CharField(max_length=100)
	kasalligi = models.TextField()
	qayerga = models.CharField(max_length=100)
	diagnoz = models.CharField(max_length=100)
	whereas = models.CharField(max_length=150, null=True, blank=True)

	def __str__(self):
	    return self.bemor

	def get_absolute_url(self):
		return reverse('referral_detail', args=[str(self.id)])
