from django.contrib import admin

from .models import Product, Board, Account


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'inventory', 'detail']


class AccountAdmin(admin.ModelAdmin):
    fields = ['username','address', 'contact']


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'writer', 'date', 'content', 'board_password']

admin.site.register(Product, ProductAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Board, BoardAdmin)
