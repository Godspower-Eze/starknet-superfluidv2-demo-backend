from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from .serializers import PoolSerializer
from .models import Pool


class AllPools(generics.ListAPIView):

    """
    Gets all pool
    """

    serializer_class = PoolSerializer
    queryset = Pool.objects.all()


class CreatePool(generics.CreateAPIView):

    """
    Creates a pool
    """

    serializer_class = PoolSerializer


class DeletePool(generics.DestroyAPIView):

    """
    Deletes a pool
    """

    serializer_class = PoolSerializer
    queryset = Pool.objects.all()

    def delete(self, request, *args, **kwargs):
        pool_address = self.request.path.split('/')[2]
        pools = Pool.objects.filter(address=pool_address)
        if pools.exists():
            pools[0].delete()
        return Response(status=HTTP_204_NO_CONTENT)


class PoolsByAccount(generics.ListAPIView):

    """
    Returns all pools by an account
    """

    serializer_class = PoolSerializer

    def get_queryset(self):
        account = self.request.path.split('/')[2]
        return Pool.objects.filter(account=account)
