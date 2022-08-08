from django.urls import path
from brainapp import views


# TEMPLATE TAGGING
app_name = 'brainapp'

urlpatterns= [
path('relative',views.relative, name= 'relative'),
path('other',views.other, name='other')
]
