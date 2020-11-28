from rest_framework import serializers
from main.models import Product,ProductSize,ProductColor


    

class ProductSerializers(serializers.ModelSerializer):
    name = serializers.CharField()
    color=serializers.CharField()
    image=serializers.ImageField()
    small=serializers.BooleanField()
    medium=serializers.BooleanField()
    large=serializers.BooleanField()
    extralarge=serializers.BooleanField()

    class Meta:
        model = Product
        fields = ['name','color','image','small','medium','large','extralarge']



class ProductDeleteSerializers(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Product
        fields=['name']
    

class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=[]



class ProductDetailSerializers(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Product
        fields=['name']


class ProductUpdateSerializers(serializers.ModelSerializer):
    product_id=serializers.CharField()
    name = serializers.CharField()
    color=serializers.CharField()
    image=serializers.ImageField()
    small=serializers.BooleanField()
    medium=serializers.BooleanField()
    large=serializers.BooleanField()
    extralarge=serializers.BooleanField()

    class Meta:
        model = Product
        fields = ['product_id','name','color','image','small','medium','large','extralarge']