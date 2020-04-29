from django.urls import path
from . import views

# all urls for api_fetcher app
urlpatterns = [
    #home page to show data
    path('', views.home, name='home'),
    #fetch view to collect data and save to database
    path('fetch_api/' , views.fetch_api , name='fetch-api'),
]