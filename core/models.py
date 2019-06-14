from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class MainPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True,)
    img = models.ImageField(blank=True, null=True, upload_to='pages/img')
    pub_date = models.DateTimeField(default=timezone.now)
    extra_info = models.TextField(blank=True, null=True)
    
    # Metadata 
    class Meta: 
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Pages'
        ordering = ["-title", ]
    # Methods
    def __str__(self):
        return self.title