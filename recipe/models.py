from django.db import models
from django.urls import reverse
import uuid

class Recipe(models.Model):
	id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	bemor = models.CharField(max_length=50)
	diagnoz = models.CharField(max_length=200)
	firstrec = models.CharField(max_length=100, null=True, blank=True)
	secondrec = models.CharField(max_length=100, null=True, blank=True)
	thirdrec = models.CharField(max_length=100, null=True, blank=True)
	fourthrec = models.CharField(max_length=100, null=True, blank=True)
	fifthrec = models.CharField(max_length=100, null=True, blank=True)
	sixthrec = models.CharField(max_length=100, null=True, blank=True)
	seventhrec = models.CharField(max_length=100, null=True, blank=True)
	eightthrec = models.CharField(max_length=100, null=True, blank=True)
	ninethrec = models.CharField(max_length=100, null=True, blank=True)
	tenthrec = models.CharField(max_length=100, null=True, blank=True)
	eleventhrec = models.CharField(max_length=100, null=True, blank=True)
	twelvethrec = models.CharField(max_length=100, null=True, blank=True)
	thirdteenthrec = models.CharField(max_length=100, null=True, blank=True)
	fourteenthrec = models.CharField(max_length=100, null=True, blank=True)
	fifteenthrec = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.bemor

	def get_absolute_url(self):
		return reverse('recipe_detail', args=[str(self.id)])

