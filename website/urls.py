
from django.urls import path , include
from website.views import index_view

#app_name='website'

urlpatterns = [
    
    path('',index_view,name='index'),
    
]
