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
        form=orderform (request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    form=orderform()
    return render(request,'index.html',{'form':form})


def show(request):
    orders=order1.objects.all()
    
    return render(request,'show.html',{'order':orders})



def delete(request,id):
    order2=order1.objects.get(id=id)
    order2.delete()

    return redirect('/show')