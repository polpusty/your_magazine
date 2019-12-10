from django.contrib import admin

from magazines.models import Article, Magazine


admin.site.register(Article, admin.ModelAdmin)
admin.site.register(Magazine, admin.ModelAdmin)
