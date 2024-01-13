from django.contrib import admin
from core.models import *
# Register your models here.
class Product_Images_Admin(admin.TabularInline):
    model=ProductImage
class ProductAdmin(admin.ModelAdmin):
    inlines=[Product_Images_Admin]
    list_display=['user','title','product_image','feature','price','product_status']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']
class VendorAdmin(admin.ModelAdmin):
    list_display=['title','vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display=['user','price','paid_status','orderDate','product_status']
class CartOrderItemAdmin(admin.ModelAdmin):
    list_display=['order','invoice_no','product_status','item','image','qyt','price','total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display=['user','product','review','rating','date']

class WishListAdmin(admin.ModelAdmin):
    list_display=['user','product','date']

class AddressAdmin(admin.ModelAdmin):
    list_display=['user','address','status']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItem,CartOrderItemAdmin)
admin.site.register(WishList,WishListAdmin)
admin.site.register(Address,AddressAdmin)