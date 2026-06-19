from django.urls import path
from . import views
urlpatterns=[
   path('',views.SRS,name='home'),
   path('SRS/', views.SRS, name='SRS'),
   path('view/',views.view_students,name='view_students'),
   path('update1/<int:id>/',views.update_student,name='update_student'),
   path('delete/<int:id>/',views.delete_student,name='delete_student'),

]
