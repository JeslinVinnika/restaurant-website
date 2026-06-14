from .import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('blog/', views.blog, name='blog'),
    path('booking/', views.booking, name='booking'),
    path('feature/', views.feature, name='feature'),
    path('index/', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('single/', views.single, name='single'),
    path('team/', views.team, name='team'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('cookies/', views.cookies, name='cookies'),
    path('help/', views.help_page, name='help'),
    path('faq/', views.faq, name='faq'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('news_letter/', views.news_letter, name='news_letter'),
    path('upi-payment/', views.upi_payment, name='upi_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('blog/single/', views.single_blog, name='single_blog'),
]

