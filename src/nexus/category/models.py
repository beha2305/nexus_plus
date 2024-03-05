from django.db import models

class Category(models.Model):
    name= models.CharField(max_length= 30, null= False, blank= False)
    icon=models.CharField(max_length= 20, null= True, blank= True)
    main_icon= models.ImageField(upload_to= 'images/', null= True, blank= True)
    parent= models.ForeignKey('self', on_delete= models.CASCADE, null= True, blank=True)
    sorting= models.SmallIntegerField(null=True, blank= True)

    def __str__(self):
        return self.name
