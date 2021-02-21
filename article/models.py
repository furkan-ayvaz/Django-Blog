from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Article(models.Model): 
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name= "Author")
    content = RichTextField(verbose_name="Content")
    title = models.CharField(max_length=50,verbose_name="Title")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
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

        