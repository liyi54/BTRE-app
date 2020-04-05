from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    # return HttpResponse('<h1>Hello World!</h1>')  Here's a test. Typically, we would like to render a template instead
    top_listings = Listing.objects.order_by('list_date').filter(is_published=True)[:3]
    context = {
        'listings': top_listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVPs
    mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)

