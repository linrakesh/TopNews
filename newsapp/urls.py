from django.urls import path
from .views import index, home
urlpatterns = [
    #path('', index(country_name='in'), name="index"),
<<<<<<< HEAD
    path('/<country_name>', index, name="index"),
=======
    path('', home, name="home"),
    path('<country_name>', index, name="index"),
>>>>>>> d28701cd4b58004f9795043b76182ee41f5e53a3
]
