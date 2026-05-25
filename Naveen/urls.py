from django.urls import path
from . import views
urlpatterns=[
   path('',views.SRS,name='home'),
   path('SRS/', views.SRS, name='SRS'),
]