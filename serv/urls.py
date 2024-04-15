from django.urls import path
from.import views
urlpatterns=[
    path('sevices/', views.services, name='services')
]