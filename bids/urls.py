from django.urls import path

from bids.apps import BidsConfig
from bids.views import BidCreateAPIView, BidListAPIView, BidRetrieveAPIView, BidDestroyAPIView


app_name = BidsConfig.name

urlpatterns = [
    path('create/', BidCreateAPIView.as_view(), name='bid_create'),
    path('', BidListAPIView.as_view(), name='bid_list'),
    path('view/<int:pk>', BidRetrieveAPIView.as_view(), name='bid_view'),
    path('delete/<int:pk>', BidDestroyAPIView.as_view(), name='bid_delete'),
]