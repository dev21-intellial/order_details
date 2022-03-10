from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from customer.models import customer

from order.models import order1
from product.models import product
from order.forms import orderform
from customer.forms import customerform
from product.forms import productform
from order.models import order1



def insert(request):
    if request.method=="POST":
        
        customer_id=request.POST['first_name']
        product_id=request.POST['name']
        qty=request.POST['qty']
        unit_price=request.POST['unit_price']
        total_price=request.POST['total_price']
        data_store=order1(customer_id=customer_id,product_id=product_id,qty=qty,unit_price=unit_price,total_price=total_price)
        data_store.save()
        
        return redirect('/show')
        
    else:
        orders=order1.objects.all()
        pro=product.objects.all()
        cust=customer.objects.all()
        return render(request,'insert.html',{'order':orders,'pro':pro,'cust':cust})

def show(request):
    orders=order1.objects.all()
    
    return render(request,'show.html',{'order':orders})



def delete(request,id):
    order2=order1.objects.get(id=id)
    order2.delete()

    return redirect('/show')




def edit(request,id):
    edit1 = order1.objects.get(id=id)
    print(edit1)
    
    return render(request,'edit.html',{'edit1':edit1})

def update(request,id):
    customer_id=request.POST['first_name']
    print(customer_id)
    product_id=request.POST['name']
    qty=request.POST['qty']
    unit_price=request.POST['unit_price']
    total_price=request.POST['total_price']
    data_store=order1(id=id,customer_id=customer_id,product_id=product_id,qty=qty,unit_price=unit_price,total_price=total_price)
    data_store.save()
    return redirect('/show')
    

