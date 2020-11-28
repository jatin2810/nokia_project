from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet
from main.api.serializers import ProductSerializers,ProductDeleteSerializers,ProductListSerializers,ProductDetailSerializers,ProductUpdateSerializers
from main.models import Product,ProductColor,ProductSize,ProductSizeColor
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializers

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            color_array = serializer.validated_data['color']
            small = serializer.validated_data['small']
            large = serializer.validated_data['large']
            medium = serializer.validated_data['medium']
            extralarge = serializer.validated_data['extralarge']
            colors=color_array.split(',')
            
            product=Product.objects.create(name=name)
            product.save()
            def upload_docs(request):
                try:
                    product.image = request.data['image']
                    print(product.image)
                    product.save()
                except KeyError:
                    raise ParseError('Request has no resource file attached')
            upload_docs(request)

            sizes=[]
            if small==True:
                sizes.append('small')
                size=ProductSize.objects.create(size="small",product=product,small=True)
                size.save()
                

            
            if medium==True:
                sizes.append('medium')
                size=ProductSize.objects.create(size="medium",product=product,medium=True)
                size.save()
            
            if large==True:
                sizes.append('large')
                size=ProductSize.objects.create(size="large",product=product,large=True)
                size.save()
            
            if extralarge==True:
                sizes.append('extralarge')
                size=ProductSize.objects.create(size="extralarge",product=product,extralarge=True)
                size.save()
            

            for item in colors:
                color=ProductColor.objects.create(product=product,color=item)
                color.save()

                for i in sizes:
                    size_obj=ProductSize.objects.filter(size=i,product=product)[0]
                    myProduct=ProductSizeColor.objects.create(product=product,color=color,size=size_obj)
                    myProduct.save()

            return Response({"outcome":'success'})
        
        else:
            return Response({'outcome':'fail'})
        
    def get(self,format=None):
        serializer = self.serializer_class()
        return Response({})


class ProductUpdateView(CreateAPIView):
    serializer_class = ProductUpdateSerializers

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            product_id=serializer.validated_data['product_id']
            name = serializer.validated_data['name']
            color_array = serializer.validated_data['color']
            small = serializer.validated_data['small']
            large = serializer.validated_data['large']
            medium = serializer.validated_data['medium']
            extralarge = serializer.validated_data['extralarge']
            colors=color_array.split(',')
            

            product=Product.objects.filter(product_id=product_id)[0]
           
            if name!="":
                product.name=name
                product.save()

            def upload_docs(request):
                try:
                    image = request.data['image']
                    if image!='':
                        product.image=image
                        product.save()
                except KeyError:
                    raise ParseError('Request has no resource file attached')
            upload_docs(request)


            
            color_database = ProductSize.objects.filter(product=product)
            for item in color_database:
                item.delete() 
           
            
            size_database = ProductSize.objects.filter(product=product)
            for item in size_database:
                item.delete()


            sizes=[]
            if small==True:
                sizes.append('small')
                size=ProductSize.objects.create(size="small",product=product,small=True)
                size.save()
                

            
            if medium==True:
                sizes.append('medium')
                size=ProductSize.objects.create(size="medium",product=product,medium=True)
                size.save()
            
            if large==True:
                sizes.append('large')
                size=ProductSize.objects.create(size="large",product=product,large=True)
                size.save()
            
            if extralarge==True:
                sizes.append('extralarge')
                size=ProductSize.objects.create(size="extralarge",product=product,extralarge=True)
                size.save()
            

            for item in colors:
                color=ProductColor.objects.create(product=product,color=item)
                color.save()

                for i in sizes:
                    size_obj=ProductSize.objects.filter(size=i,product=product)[0]
                    myProduct=ProductSizeColor.objects.create(product=product,color=color,size=size_obj)
                    myProduct.save()

            return Response({"outcome":'success'})
        
        else:
            return Response({'outcome':'fail'})
        
    def get(self,request,format=None):

        name=request.query_params['name']
        product=Product.objects.filter(name=name)[0]

        colors=ProductColor.objects.filter(product=product)
        sizes=ProductSize.objects.filter(product=product)
        product_list={}
        
        color=[]
        for item in colors:
            color.append(item.color)
        size=[]
        for item in sizes:
            size.append(item.size)
        url='http://127.0.0.1:8000/media/'+str(product.image)
        product_list[product.product_id]={'product_id':product.product_id,'name':product.name,'image':url,'color':color,'size':size,'Alert':'Enter Product Id as shown in Details'}
        return Response(product_list)



 
class ProductDeleteView(CreateAPIView):
    serializer_class = ProductDeleteSerializers
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            product_list=Product.objects.filter(name=name)

            for item in product_list:
                item.delete()
            
            return Response({"delete":'success'})
        else:
            return Response({'delete':'fail'})
    
    def get(self,format=None):
        serializer = self.serializer_class()
        return Response({})

class ItemsSetPagination(PageNumberPagination):
    page_size = 6

class ProductListView(ModelViewSet):
    queryset = Product.objects.get_queryset().order_by('product_id')
    serializer_class = ProductListSerializers
    pagination_class = ItemsSetPagination
    

class ProductListView1(CreateAPIView):
    serializer_class = ProductListSerializers
    def get(self,format=None):
        serializer = self.serializer_class()
        product=Product.objects.all()

        product_list={}

        for item in product:
            product_list[item.product_id]={'name':item.name}
        
        return Response(product_list)

   



class ProductDetailView(CreateAPIView):
    serializer_class = ProductDetailSerializers
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            product=Product.objects.filter(name=name)[0]

            colors=ProductColor.objects.filter(product=product)
            sizes=ProductSize.objects.filter(product=product)
            product_list={}
            
            color=[]
            for item in colors:
                color.append(item.color)
            size=[]
            for item in sizes:
                size.append(item.size)
            url='http://127.0.0.1:8000/media/'+str(product.image)
            product_list[product.product_id]={'name':product.name,'image':url,'color':color,'size':size}
            return Response(product_list)
        else:
            return Response({'detail_fetch':'fail'})
    
    def get(self,format=None):
        serializer = self.serializer_class()
        return Response({})