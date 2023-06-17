from django.db import models
from django.utils.text import slugify 
from django.urls import reverse
from ckeditor.fields import RichTextField


from pages.models import Category
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    context = RichTextField()
    date_publish = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True,help_text="if leave it will take from title ",unique=True)


    # meta
    meta_title = models.CharField(max_length=255,null=True,blank=True,help_text="if leave it will take from title ")
    meta_description = models.CharField(max_length=255,null=True,blank=True)
    meta_keywords = models.TextField(null=True,blank=True,help_text="use comma( , ) for separation")


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug == None:

            self.slug = slugify(self.title)
        if self.meta_title == None:

            self.meta_title = self.title
        if self.meta_description == None:

            self.meta_description = self.description
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
    # u create url only here and then reference here throughout of your project
        return reverse("blog_details",args=[self.slug])
    
