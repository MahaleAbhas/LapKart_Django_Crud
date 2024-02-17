from django.urls import path
from .views import Add_view,Show_View,Update_view,Delete_View,Layout
urlpatterns = [
    path('add/', Add_view),
    path('show/', Show_View),
    path('update/<i>/', Update_view),
    path('delete/<i>/', Delete_View),
    path('lay/', Layout)
]