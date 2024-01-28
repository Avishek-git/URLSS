from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.CharField(max_length=500,primary_key=True)
    short_url = models.CharField(max_length=500,unique=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_url