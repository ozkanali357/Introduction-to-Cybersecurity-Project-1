from django.urls import path
from . import views

urlpatterns = [
    path('insecure-direct-object-reference/', views.insecure_direct_object_reference, name='insecure_direct_object_reference'),
    path('broken-authentication/', views.broken_authentication, name='broken_authentication'),
    path('cross-site-scripting/', views.cross_site_scripting, name='cross_site_scripting'),
    path('sql-injection/', views.sql_injection, name='sql_injection'),
    path('security-misconfiguration/', views.security_misconfiguration, name='security_misconfiguration'),
    path('cryptographic-failures/', views.cryptographic_failures, name='cryptographic_failures'),
]