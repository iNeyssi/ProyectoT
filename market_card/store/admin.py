from django.contrib import admin
from store.models import Product 

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['image_path', 'title', 'description', 'price']
    list_editable = ['price']
    list_filter = ['price']
class Meta:
    model = Product
admin.site.register(Product, ProductAdmin)

