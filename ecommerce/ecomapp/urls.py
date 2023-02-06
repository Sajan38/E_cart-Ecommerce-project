from django.urls import path
from .views import *


urlpatterns=[

    # user

    path('',index),
    path('register/',registerview),
    path('login/',loginview),
    path('user/',userview),
    path('addcart/<int:id>',addcart),
    path('cartdisplay/',cartdisplay),
    path('cartremove/<int:id>',cartremove),
    path('cartbuy/<int:id>',cartbuy),



# ------------------------------------------------------------------------------------
#     shop

    path('shop/',shopregview),
    path('shopregedit/<int:id>',shopregedit),
    path('shoplogin/',shoploginview),
    path('shopprofile/',shopprofile),
    path('upload/',shopupload),
    path('viewproduct/',viewproduct),
    path('productedit/<int:id>',productedit),
    path('productdelete/<int:id>',productdelete),



# -----------------------------------------------------------------------------------------
# Email verify


    path('register/',regis),
    path('verify/<auth_token>',verify)

]
