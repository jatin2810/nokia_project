from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='product_image',blank=True)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name



class ProductColor(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.CharField(max_length=300)

    def __str__(self):
        return self.product.name +" "+ self.color



class ProductSize(models.Model):
    size=models.CharField(max_length=300)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    small=models.BooleanField(default=False)
    medium=models.BooleanField(default=False)
    large=models.BooleanField(default=False)
    extralarge=models.BooleanField(default=False)

    def __str__(self):
        return self.size


class ProductSizeColor(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(ProductColor,on_delete=models.CASCADE)
    size=models.ForeignKey(ProductSize,on_delete=models.CASCADE)


    def __str__(self):
        return  self.product.name + " " + self.color.color+" "+self.size.size

        
        




    