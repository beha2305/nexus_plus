from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name= 'index' ),
    path("create/" , product_create, name= 'product-create'),
    path("view-detail/<int:product_id>", view_details, name= 'veiw_details' )
]