from django.contrib import admin
from models import Category, SubCategory, Product, Mailinglist, Order, OrderProduct

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Mailinglist)
admin.site.register(Order)
admin.site.register(OrderProduct)