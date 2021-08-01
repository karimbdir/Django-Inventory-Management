from django.db import models

# Create your models here.

class Device(models.Model):
    
    choices = (
        ('Available','Item is Stock'),
        ('In_Production','Being used in Production'),
        ('Restocking','Item is being shipped')
    )
    choices_issues = (
        ('No_Issues','Product is fine'),
        ('Bad','Quality of the Product is not good'),
        ('Good','Product is good')
    )

    type = models.CharField(max_length=250,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=50,choices=choices,default='Available') #Available, Restocking, In Production
    issues = models.CharField(max_length=100,choices=choices_issues,default='No_Issues')

    class Meta:
        abstract = True
    
    def __str__(self):
        return 'Type : {} Price : {}'.format(self.type, self.price)


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass 