from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('display_laptops',views.display_laptops,name="display_laptops"),
    path('display_desktops',views.display_desktops,name="display_desktops"),
    path('display_mobiles',views.display_mobiles,name="display_mobiles"),
    path('add_laptop',views.add_laptop,name="add_laptop"),
    path('add_desktop',views.add_desktop,name="add_desktop"),
    path('add_mobile',views.add_mobile,name="add_mobile"),
    path('edit_laptop/<int:pk>/',views.edit_laptop,name="edit_laptop"),
    path('edit_desktop/<int:pk>/',views.edit_desktop,name="edit_desktop"),
    path('edit_mobile/<int:pk>/',views.edit_mobile,name="edit_mobile"),
    path('delete_laptop/<int:pk>/',views.delete_laptop,name="delete_laptop"),
    path('delete_desktop/<int:pk>',views.delete_desktop,name="delete_desktop"),
    path('delete_mobile',views.delete_mobile,name="delete_mobile"),
]
