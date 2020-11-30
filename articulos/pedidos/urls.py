from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('pedidos/', login_required(PedidoList.as_view(), login_url='/accounts/login/') , name="mis_pedidos"),
    path('<int:pk>', login_required(PedidoDetail.as_view(), login_url='/accounts/login/') , name="detalle"),
    path('pedidos/create/', login_required(PedidoCreate.as_view(),login_url='accounts/login'), name="hacer_pedido"),
    path('pedidos/<int:pk>/delete/', login_required(PedidoDelete.as_view(),login_url='accounts/login/'), name="eliminar_pedido")
]
