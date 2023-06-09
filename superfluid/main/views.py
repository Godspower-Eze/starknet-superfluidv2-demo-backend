from django.shortcuts import render

from rest_framework import generics

from .serializers import PoolSerializer
from .models import Pool


class AllPools(generics.ListAPIView):

    """
    Gets all pool
    """

    serializer_class = PoolSerializer
    queryset = Pool.objects.all()


class CreatePools(generics.CreateAPIView):

    """
    Create new pool
    """

    serializer_class = PoolSerializer


class PoolsByAccount(generics.ListAPIView):

    """
    Returns all pools by an account
    """

    serializer_class = PoolSerializer

    def get_queryset(self):
        account = self.request.path.split('/')[2]
        return Pool.objects.filter(account=account)
