from rest_framework.viewsets import ModelViewSet
from transactions.models import Transaction
from serializers.serializer import TransactionSerializer

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer