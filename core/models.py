from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import *
from taggit.managers import TaggableManager
# Create your models here.

Status_Choice=(
   
   ('Processing','Processing'),
   ('shiped','shipped'),
   ('deliverd','delivered'),
)
Status=(
   ('draft','draft'),
   ('disabled','disabled'),
   ('rejected','rejected'),
   ('in_review','in_review'),
   ('published','published'),
)
Ratings=(
   (1,'⭐☆☆☆☆'),
   (2,'⭐⭐☆☆☆'),
   (3,'⭐⭐⭐☆☆'),
   (4,'⭐⭐⭐⭐☆'),
   (5,'⭐⭐⭐⭐⭐'),
)
def user_directory_path(instance,filename):
   return 'user_{0}/{1}'.format(instance.user.id,filename)
class Category(models.Model):
    cid=ShortUUIDField(unique=True,length=10,max_length=20,prefix='cat',alphabet="abcdef1245")
    title=models.CharField(max_length=200,default='food')
    image=models.ImageField(upload_to='category',default='category.jpg')

    class Meta:
        verbose_name_plural='Categories'
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' %(self.image.url))
    def __str__(self):
        return self.title
    
class Vendor(models.Model):
 vid=ShortUUIDField(unique=True,length=10,max_length=20,prefix='ven',alphabet="abcdef1234566")
 title=models.CharField(max_length=200,default='Nasty')
 image=models.ImageField(upload_to=user_directory_path)
 description=models.TextField(max_length=200,default='i am a great vendor')
 address=models.CharField(max_length=200,default='kumagaya')
 contact=models.CharField(max_length=200,default='123456')
 chat_resp_time=models.CharField(max_length=200,default='123456')
 shipping_on_time=models.CharField(max_length=200,default='123456')
 authentic_rating=models.CharField(max_length=200,default='123456')
 days_return=models.CharField(max_length=200,default='123456')
 warranty_peroid=models.CharField(max_length=200,default='123456')

 user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)


 class Meta:
   verbose_name_plural='Vendors'
 def vendor_image(self):
    return mark_safe('<img src="%s" width="50" height="50"/>' %(self.image.url))
 def __str__(self):
    return self.title
 
class Product(models.Model):
   pid=ShortUUIDField(unique=True,length=10,max_length=20,prefix='pro',alphabet='abcdef123456')
   user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='category')
   vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,related_name='product')

   title=models.CharField(max_length=200,default="apple")
   image=models.ImageField(upload_to=user_directory_path,default='product.jpg')
   description=models.TextField(max_length=200,default='this is a product')
   tags=TaggableManager(blank=True)
   price=models.IntegerField()
   specification=models.TextField(max_length=200,null=True,blank=True)
   
   product_status=models.CharField(choices=Status,max_length=200,default='in review')
   status=models.BooleanField(default=True)
   in_stock=models.BooleanField(default=True)
   feature=models.BooleanField(default=False)
   digital=models.BooleanField(default=True)
   
   sku=ShortUUIDField(unique=True,length=10,max_length=20,prefix='sku',alphabet='abcdef12345')
   date=models.DateField(auto_now_add=True)
   update=models.DateTimeField(null=True,blank=True)

   class Meta:
      verbose_name_plural='Products'
    
   def product_image(self):
      return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
   def __str__(self):
      return self.title
#    def get_percentage(self):
#       new_price=(self.price/self.)
class ProductImage(models.Model):
   image=models.ImageField(upload_to='product_img',default='product.jpg')
   product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='p_image')
   date=models.DateField(auto_now_add=True)

   class Meta:
      verbose_name_plural='Product Image'


class CartOrder(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   price=models.IntegerField()
   paid_status=models.BooleanField(default=False)
   orderDate=models.DateField(auto_now_add=True)
   product_status=models.CharField(choices=Status,max_length=200,default='processing')

   class Meta:
      verbose_name_plural='Cart Order'

class CartOrderItem(models.Model):
   order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
   invoice_no=models.CharField(max_length=200)
   product_status=models.CharField(max_length=200)
   item=models.CharField(max_length=200)
   image=models.CharField(max_length=200)
   qyt=models.IntegerField(default=0)
   price=models.IntegerField()
   total=models.IntegerField()

   class Meta:
      verbose_name_plural='Cart Order Item'
    
   def cart_img(self):
      return mark_safe('<img src="/media/%s" width="50" height="50" />' %(self.image))
   
class ProductReview(models.Model):
   user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name='reviews')

   review=models.TextField()
   rating=models.IntegerField(choices=Ratings,default=None)
   date=models.DateField(auto_now_add=True)

   class Meta:
      verbose_name_plural='Product Review'

   def __str__(self):
      return self.product.title
   def get_rating(self):
      return self.rating
   
class WishList(models.Model):
   user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)


   date=models.DateField(auto_now_add=True)

   class Meta:
      verbose_name_plural='wishlist'

   def __str__(self):
      return self.product.title

class Address(models.Model):
   user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   address=models.CharField(max_length=200,null=True)
   status=models.BooleanField(default=False)

   class Meta:
      verbose_name_plural='address'

   

