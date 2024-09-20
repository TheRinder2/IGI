from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users.views import register, profile, profileedit, profiledelete

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration', register, name='registration'),
    path('profile', profile, name='profile'),
    path('profileedit', profileedit, name='profileedit'),
    path('profiledelete', profiledelete, name='profiledelete'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main.html'), name='logout'),

    path('news', views.news, name='news'),
    path('faq', views.faq, name='faq'),
    path('contacts', views.contacts, name='contacts'),
    path('policy', views.policy, name='policy'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('feedback', views.feedback, name='feedback'),
    path('discounts', views.discount, name='discounts'),
    path('requestImm', views.offersImm, name='requestImm'),
    path('requestRent', views.offersRent, name='requestRent'),
    path('time', views.userTime, name='time'),
    path('employee', views.employee, name='employee'),
]
