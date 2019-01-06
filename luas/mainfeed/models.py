from django.db import models
from uuslug import uuslug
from django.utils import timezone

class Headline(models.Model):
    title = models.CharField(max_length=130)
    url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200)
    hit = models.IntegerField(default=0)
    genre = models.CharField(max_length=80, blank=True)

    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Headline, self).save(*args, **kwargs)

    def __str__(self):
        return self.title