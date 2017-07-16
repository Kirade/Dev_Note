from django.contrib import admin

from .models import Product, Board


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'inventory', 'detail']


# class UserAdmin(admin.ModelAdmin):
#     fields = ['address', 'contact']


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'writer', 'date', 'content', 'board_password']

admin.site.register(Product, ProductAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(Board, BoardAdmin)
