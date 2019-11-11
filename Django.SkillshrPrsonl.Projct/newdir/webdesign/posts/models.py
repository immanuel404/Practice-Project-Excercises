from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
	user						=models.ForeignKey(User)
	title						=models.CharField(max_length=120, unique=True)
	content     				=models.TextField()
	image        				=models.TextField(null=True, blank=True, help_text='Image url')
	publish_date 				=models.DateField(default='2017-10-10')
	timestamp					=models.DateTimeField(auto_now_add=True)
	updated						=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content[:50]

	def get_absolute_url(self):
		return reverse("post_detail", kwargs={"id": self.id})

	class Meta:
		verbose_name 			= 'Blog post'
		verbose_name_plural 	= 'Blog posts'
		ordering				=['-publish_date', '-pk']
