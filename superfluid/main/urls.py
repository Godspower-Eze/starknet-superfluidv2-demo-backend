from django.urls import path

from .views import AllPools, CreatePools, PoolsByAccount

urlpatterns = [
    path('pools/', AllPools.as_view(), name="pools"),
    path('pools_by_account/<str:account>',
         PoolsByAccount.as_view(), name="pools_by_account"),
    path('create_pool/', CreatePools.as_view(), name="create_pool"),
]
