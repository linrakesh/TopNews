from django.urls import path
from .views import index, home
urlpatterns = [
    #path('', index(country_name='in'), name="index"),
    path('', home, name="home"),
    path('<country_name>', index, name="index"),
]
