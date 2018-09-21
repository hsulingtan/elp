from django.urls import path
from elpapp import views

app_name = 'elpapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('employer/', views.Cemployer, name='Cemployer' ),
    path('student/', views.Cstudent, name='Cstudent'),
    path('eform_page/', views.Employer, name='Employer'),
    path('sform_page/', views.Student, name='Student'),
    path('eregister/', views.eregister, name='eregister'),
    path('sregister/', views.sregister, name='sregister'),
    path('user_login/',views.user_login,name='user_login'),
]
