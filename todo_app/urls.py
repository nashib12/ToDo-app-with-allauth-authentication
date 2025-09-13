from django.urls import path

from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('details/',details,name="details"),
    
    # ------------------- Authentication Section --------------------
    path('create-user/',createUser,name="registration"),
    path('log-in/',log_in,name="log-in"),
    path('log-out/',log_out,name="log-out"),
    
    # ---------------- todo section -----------------------
    path('create--item/',addItem,name="add-item"),
    path('update--item/<int:id>/',updateItem,name="update-item"),
    path('delete--item/<int:id>/',deleteItem,name="delete-item"),
    path('recycle/',recycleItem,name="recycle"),
]
