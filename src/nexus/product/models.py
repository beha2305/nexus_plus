from django.db import models
from nexus.category.models import Category
from nexus.geo.models import City
from nexus.user.models import User
class Product(models.Model):
    title= models.CharField(max_length= 200, null= False, blank= False)
    description= models.TextField()
    city= models.ForeignKey(City, on_delete=models.SET_NULL, null= True, blank=False)
    price= models.IntegerField(null=False, blank=False)
    category= models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, blank=False)
    state = models.SmallIntegerField(choices= [(1, 'New'), (2, 'Old')], null= False, blank=False)
    discount = models.SmallIntegerField(default= 0)
    address = models.CharField(max_length= 100, null= True, blank= True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null= True)
    status = models.SmallIntegerField(choices= [(1, 'Active'), (2, 'Inactive'), (3, 'Sold')], default=1)
    post_date= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image= models.FileField(upload_to= 'images', null= True, blank= True)
    product= models.ForeignKey(Product, on_delete= models.CASCADE)
    is_main = models.BooleanField(default= False)

    def __str__(self):
        return self.image