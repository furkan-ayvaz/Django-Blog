from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Article(models.Model): 
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name= "Author")
    content = RichTextField(verbose_name="Content")
    title = models.CharField(max_length=100,verbose_name="Title", unique = True)
    last_update = models.DateTimeField(auto_now = True,verbose_name = "Update date")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    slug = models.SlugField(unique = True, max_length = 100)

    def get_absolute_url_detail(self): 
	    return reverse("article:detail", kwargs = {"slug":self.slug})
    
    def get_absolute_url_update(self): 
	    return reverse("article:update",  kwargs = {"slug":self.slug})

    def get_absolute_url_delete(self): 
	    return reverse("article:delete",  kwargs = {"slug":self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"] 


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "Name")
    comment_content = models.CharField(max_length= 300, verbose_name="Comment")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="created_date")
    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ["-created_date"]

        