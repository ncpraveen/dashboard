from django.db import models

class metrics(models.Model):
	current_time = models.DateTimeField()
	merged_commits = models.IntegerField(default=0)
	new_commits = models.IntegerField(default=0)
	owner = models.CharField(max_length=200)


