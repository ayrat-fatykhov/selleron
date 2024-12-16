from rest_framework import serializers

from bids.models import Bid


class BidSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данные в битовую последовательность. Для модели Лог
    """
    class Meta:
        model = Bid
        fields = '__all__'
