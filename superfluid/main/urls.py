from django.urls import path

from .views import AllPools, CreatePool, DeletePool, PoolsByAccount

urlpatterns = [
    path('pools/', AllPools.as_view(), name="pools"),
    path('pools_by_account/<str:account>',
         PoolsByAccount.as_view(), name="pools_by_account"),
    path('delete_pool/<str:address>/',
         DeletePool.as_view(), name="delete_pool"),
    path('create_pool/', CreatePool.as_view(), name="create_pool"),
]
