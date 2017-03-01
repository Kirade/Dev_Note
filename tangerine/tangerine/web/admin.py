from django.contrib import admin

from .models import Product, Client, Board


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'inventory', 'detail']


class ClientAdmin(admin.ModelAdmin):
    fields = ['user', 'address', 'contact']


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'writer', 'date', 'content', 'board_password']

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Board, BoardAdmin)
