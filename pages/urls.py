from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faq, name='faq'),
    path('termsofuse', views.termsofuse, name='termsofuse'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('contact', views.contact, name='contact'),

]