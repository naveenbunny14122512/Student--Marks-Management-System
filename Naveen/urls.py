from django.urls import path
from . import views
urlpatterns=[
   path('',views.login,name='login'),
   path('home/',views.SRS,name='home'),
   path('SRS/', views.SRS, name='SRS'),
   path('view/',views.view_students,name='view_students'),
   path('update1/<int:id>/',views.update_student,name='update_student'),
   path('delete/<int:id>/',views.delete_student,name='delete_student'),
   path('register/',views.register,name='register'),
   path('logout/',views.logout,name='logout'),
   path('verify/',views.verify_password,name='verify'),

]
