from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('search.html', views.search, name='search'),
    path('Add.html', views.add, name='add'),
    path('Add/submit', views.add, name='submit'),
    path('search?search=<int:year>',views.search, name='search year'),
    path('search', views.search, name='search'),
    
]