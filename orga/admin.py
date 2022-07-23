from django.contrib import admin

from orga.models import Blog, contactus, products ,review,Employee

# Register your models here.
admin.site.register(products)
admin.site.register(contactus)
admin.site.register(review)
admin.site.register(Employee)
@admin.register(Blog)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
