from django.urls import path
from . import views
urlpatterns=[
    path('',views.Index,name='Index'),
    path('confecciones/',views.confecciones,name='confecciones'),
    path('estampados/',views.estampados,name='estampados'),
    path('producto/<int:pk>',views.ProdDetailView.as_view(), name='prod_detail'),
]

urlpatterns+=[
    path('producto/create/', views.ProdCreate.as_view(), name='prod_create'),
    path('producto/<int:pk>/update/', views.ProdUpdate.as_view(), name='prod_update'),
    path('producto/<int:pk>/delete/', views.ProdDelete.as_view(), name='prod_delete'),
]

