from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from .models import Product,ProductColor,ProductSize,ProductSizeColor
from .forms import ProductForm,ProductUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def firstView(request):
    products=Product.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(products, 8)
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        product = paginator.page(1)
    except EmptyPage:
        product = paginator.page(paginator.num_pages)
    return render(request,'main/index.html',{'product':product})





def ProductForm(request):
    if request.method=='POST':
        name=request.POST.get('name')
        color_array=request.POST.get('color')
        small=request.POST.get('small')
        medium=request.POST.get('medium')
        large=request.POST.get('large')
        extralarge=request.POST.get('extralarge')

        

        colors=color_array.split(',')
        



        product=Product.objects.create(name=name)
        product.save()

        if 'image' in request.FILES:
            product.image=request.FILES['image']
            product.save()

        sizes=[]
        if small is not None:
            sizes.append('small')
            size=ProductSize.objects.create(size="small",product=product,small=True)
            size.save()
            

        
        if medium is not None:
            sizes.append('medium')
            size=ProductSize.objects.create(size="medium",product=product,medium=True)
            size.save()
        
        if large is not None:
            sizes.append('large')
            size=ProductSize.objects.create(size="large",product=product,large=True)
            size.save()
        
        if extralarge is not None:
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
        

        return redirect('/') 

    else:
        print('here')
        return render(request,'main/product_create.html',)
  


def ProductDetail(request,pk):
    product=Product.objects.filter(product_id=pk)[0]
    colors=ProductColor.objects.filter(product=product)

    # colors=[]
    # for item in color:
    #     colors.append(item.color)
    # print(colors)
    sizes=ProductSize.objects.filter(product=product)
    return render(request,"main/product_details.html",{'product':product,'colors':colors,'sizes':sizes})



def ProductDelete(request,pk):
    if request.method=='GET':
        product=Product.objects.filter(product_id=pk)[0]
        print(product)
        return render(request,'main/product_delete_confirm.html',{'product':product})
    
    else:
        product_id=request.POST.get("product_id")
        product=Product.objects.filter(product_id=product_id)[0]
        product.delete()
        return redirect('/')


def ProductUpdate(request,pk):
    if request.method=='GET':
        product=Product.objects.filter(product_id=pk)[0]
        colors=ProductColor.objects.filter(product=product)
        color=""
        for item in colors:
            color=color+item.color+","
        
        

        sizes=ProductSize.objects.filter(product=product)
        small=False;medium=False;large=False;extralarge=False
        for item in sizes:
            if item.size=='small':
                small=True
            if item.size=='medium':
                medium=True
            if item.size=='large':
                large=True
            if item.size=='extralarge':
                extralarge=True

        return render(request,'main/product_update.html',{'product':product,'color':color,'s':small,'m':medium,'l':large,'xl':extralarge})
    
    else:
        product_id=request.POST.get('product_id')
        product=Product.objects.filter(product_id=product_id)[0]


        name=request.POST.get('name')
        color_array=request.POST.get('color')
        small=request.POST.get('small')
        medium=request.POST.get('medium')
        large=request.POST.get('large')
        extralarge=request.POST.get('extralarge')

        colors=color_array.split(',')
        


        color_database = ProductColor.objects.filter(product=product)
        for item in color_database:
            item.delete()

        size_database = ProductSize.objects.filter(product=product)
        for item in size_database:
            item.delete()


        product.name=name
        if 'image' in request.FILES:
            product.image=request.FILES['image']

        product.save()

       

        sizes=[]
        if small is not None:
            sizes.append('small')
            size=ProductSize.objects.create(size="small",product=product,small=True)
            size.save()
            

        
        if medium is not None:
            sizes.append('medium')
            size=ProductSize.objects.create(size="medium",product=product,medium=True)
            size.save()
        
        if large is not None:
            sizes.append('large')
            size=ProductSize.objects.create(size="large",product=product,large=True)
            size.save()
        
        if extralarge is not None:
            sizes.append('extralarge')
            size=ProductSize.objects.create(size="extralarge",product=product,extralarge=True)
            size.save()
        
        print(colors)
        for item in colors:
            if item!='':
                color=ProductColor.objects.create(product=product,color=item)
                color.save()
                
                for i in sizes:
                    size_obj=ProductSize.objects.filter(size=i,product=product)[0]
                    myProduct=ProductSizeColor.objects.create(product=product,color=color,size=size_obj)
                    myProduct.save()
            

        return redirect('/')

        
        