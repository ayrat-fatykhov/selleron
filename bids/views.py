from rest_framework import generics

from bids.models import Bid
from bids.serializers import BidSerializer


class BidCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание Заявки
    """
    serializer_class = BidSerializer


class BidListAPIView(generics.ListAPIView):
    """
    Отвечает за отображение списка Заявок
    """
    serializer_class = BidSerializer
    queryset = Bid.objects.all()


class BidRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за отображение Заявки
    """
    serializer_class = BidSerializer
    queryset = Bid.objects.all()


class BidDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление Заявки
    """
    queryset = Bid.objects.all()
