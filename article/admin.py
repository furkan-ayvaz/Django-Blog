from django.contrib import admin
from .models import Article,Comment

# Register your models here.

@admin.register(Article) 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","last_update","created_date"] 
    search_fields = ["title"] 
    list_filter = ["created_date","last_update"] 
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Article

admin.site.register(Comment)
