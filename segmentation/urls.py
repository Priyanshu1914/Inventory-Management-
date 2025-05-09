from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'), # Web site will always open in this place
    path('main/', views.main, name='main'),
    path('dashboard/', views.main, name='dashboard'),  # Add this line 
    path('landing/', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('StockInfo/', views.StockInfo, name='StockInfo'),
    path('navbar/', views.navbar, name='navbar'),
    path('help/', views.help, name='help'),
    path('contactus/', views.contactus, name='contactus'),
    path('TermsOfService/', views.TermsOfService, name='TermsOfService'),
    path('PrivacyPolicy/', views.PrivacyPolicy, name='PrivacyPolicy'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)