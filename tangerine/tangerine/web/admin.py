from django.contrib import admin

from .models import Product, Client, Board


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'inventory', 'detail']


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'login_id', 'login_password', 'address', 'contact', 'email', 'register_date']


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'writer', 'date', 'content', 'board_password']

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Board, BoardAdmin)
