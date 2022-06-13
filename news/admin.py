from django.contrib import admin
from .models import Tag,Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
