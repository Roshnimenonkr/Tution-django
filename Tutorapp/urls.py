from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin',views.log,name='log'),
    path('signup',views.reg,name='reg'),
    path('tutorsignin/',views.logtutor,name='logtutor'),
    path('studenthome',views.studentHome,name='studentHome'),
    path('viewtutor',views.ViewTutor,name='ViewTutor'),
    path('<int:tutor_id>/',views.Tutordetail,name='Tutordetail'),
    path('requestdemo',views.Requestdemo,name="Requestdemo"),
    path('classtime',views.Classtime,name='Classtime'),
    path('paidtutor',views.PaidTutor,name='PaidTutor'),
    path('studentbooks',views.StudentBooks,name='StudentBooks'),
    path('logout',views.logout,name='logout'),
    path('tutorhome',views.TutorHome,name='TutorHome'),
    path('tutorrequest',views.Tutorrequest,name='Tutorrequest'),
    path('tutorlibrary',views.TutorLibrary,name='TutorLibrary'),
    path('remove/<int:Req_id>/',views.remove,name='remove'),
    path('booktutor',views.BookTutor,name='BookTutor'),
    path('logouttutor',views.logouttutor,name='logouttutor'),
    path('democomplete',views.Democomplete,name='Democomplete')
]