from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.Index,name='Index'),
    path('confecciones',views.confecciones,name='confecciones'),
    path('estampados/',views.estampados,name='estampados'),
    path('producto/<int:pk>',views.ProdDetailView.as_view(), name='prod-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html') , name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='registration/logout.html') , name='logout'),
]


urlpatterns+=[
    path('producto/create/', views.ProdCreate.as_view(), name='prod-create'),
    path('update/<int:pk>/', views.ProdUpdate.as_view(), name='prod-update'),
    path('producto/<int:pk>/delete/', views.ProdDelete.as_view(), name='prod-delete'),
]

