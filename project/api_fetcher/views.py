from django.shortcuts import render , redirect
import requests
from django.contrib import messages
from .models import Item
import os
from django.conf import settings
# Create your views here.



# home page function ( show data collected from api and inserted in Database )
def home(request):
    items = Item.objects.all()
    # getting an error image from media folder
    # in order to show if images from api did not show
    path = settings.MEDIA_ROOT
    img_on_error = str(settings.MEDIA_URL + os.listdir(path)[0])
    if not items:
        messages.info(request, 'No items yet , please click on Fetch-API button')
    return render(request , 'api_fetcher/home.html' , {'items':items , 'img_on_error':img_on_error})


# fetch api and insert in database function
def fetch_api(request):
    try:
        # try to connect to api and catch errors
        response = requests.get('https://cloud.nousdigital.net/s/rNPWPNWKwK7kZcS/download')
        response.raise_for_status()
    except:
        # redirect home if any connection problems
        messages.info(request, 'Problem Connection to API')
        return redirect('home')
    try:
        # check if response content can be deserialized to python dictionary
        response_body = response.json()
    except:
        # redirect if not deserializable
        messages.info(request, 'Response Content not convered to JSON')
        return redirect('home')
    # gitting list of items
    items_list = response_body["items"]
    # check length of the list
    if items_list != None and len(items_list) != 0:
        # a temporary list to put in all objects
        all_items = []
        current_item = None
        for item in items_list:
            # create a query object for each item but don't hit database
            current_item = Item(public_id=item["id"],title=item["title"],description=item["description"],image_url=item["imageUrl"])
            # append to objects list
            all_items.append(current_item)
        # insert all objects in database in one query
        # the advantage of using bulk_create() is to hit database only one time
        try:
            #try to connect to database and insert all items once
            Item.objects.bulk_create(all_items)
        except:
            # data not inserted to database
            messages.info(request, 'Data not inserted to database')
            return redirect('home')
    else:
        #empty json
        messages.info(request , 'Call to Api returned an EMPTY list')
        return redirect('home')
    #success
    messages.info(request , "Items inserted to database successfully")
    return render(request, 'api_fetcher/fetch_api.html' , {})

