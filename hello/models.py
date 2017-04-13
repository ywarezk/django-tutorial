from django.db import models
from django.utils.text import slugify

# Create your models here.
class Greeting(models.Model):
    message = models.CharField(max_length=300)
    user = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(blank=True, null=True, default=None)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.message)
        return super(Greeting, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

