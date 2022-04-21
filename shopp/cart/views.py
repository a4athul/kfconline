from django.shortcuts import render,redirect,get_object_or_404
from shopapp.models import *
from django.core.exceptions import ObjectDoesNotExist
from . models import *
def cartdetails(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.pro.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return  render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})
def c_id(request):
    ctid=request.session.session_key
    if not ctid:
        ctid=request.session.create()
    return ctid
def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
       ct=cartlist.objects.create(cart_id=c_id(request))
       ct.save()
    try:
        c_items=items.objects.get(pro=prod,cart=ct)
        if c_items.quan <c_items.pro.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(pro=prod,cart=ct,quan=1)
        c_items.save()
    return redirect('cartdetails')
def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    proo=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(pro=proo,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    proo = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(pro=proo, cart=ct)
    c_items.delete()
    return redirect('cartdetails')