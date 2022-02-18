from django.http import HttpResponse
from django.shortcuts import render,redirect
from customer.models import customer
from order.models import order1
from product.models import product
from order.forms import orderform
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
    cus=customer.objects.all()
    pro=product.objects.all()
    
    return render(request,'index.html',{'form':form,'cus':cus,'pro':pro})




def show(request):
    orders=order1.objects.all()

    return render(request,'show.html',{'order1':orders})



