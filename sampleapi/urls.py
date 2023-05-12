from django.urls import path
from . import views
app_name = "sampleapi"
urlpatterns = [

path('load_student',views.load_student,name='l_student'),
path('add_student',views.add_student,name='a_student'),
path('update_student/<int:s_id>',views.update_student,name='u_student'),
path('delete_student/<int:s_id>',views.delete_student,name='d_student')

    
]