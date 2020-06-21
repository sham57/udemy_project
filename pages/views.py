from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import state_choice, price_choice, bedroom_choice



def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listing':listing,
        'state_choice':state_choice,
        'price_choice':price_choice,
        'bedroom_choice':bedroom_choice
    }
    return render(request, 'pages/index.html',context)


def about(request):
    realtor=Realtor.objects.order_by('-hire_date')
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtor':realtor,
        'mvp_realtor':mvp_realtor
    }
    return render(request, 'pages/about.html',context)
    
def search(request):

    query_list=Listing.objects.order_by('-list_date')

    #get keyword

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list=query_list.filter(description__icontains=keywords)
    #get city

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    #get state

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

#get bedrroms
    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)
#get price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    context={
        'state_choice': state_choice,
        'price_choice': price_choice,
        'bedroom_choice': bedroom_choice,
        'listing':query_list,
        'values':request.GET
        
        
        }
    return render(request, 'search/search.html',context)
