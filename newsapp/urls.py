from django.urls import path
from .views import index
urlpatterns = [   
    #path('', index(country_name='in'), name="index"),
    path('/<country_name>', index, name="index"),
]
