from django.urls import path
from . import views
from .views import Index
from .views import About

urlpatterns = [
    # Call .as_view() to convert the class into a usable view function
    path('', Index.as_view(), name='Home'),
    path('book/', views.Book, name='Book'),
    path('about/', About.as_view(), name='About'),
    path('fees/', views.Fees.as_view(), name='Fees')
]

#waitress-serve --host=10.0.0.83 --port=8000 UberSite.wsgi:application

