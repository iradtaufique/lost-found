from . import views
from django.urls import path
from.views import*

urlpatterns = [
    path('search/', views.search, name="search"),
    # path("", Home.as_view(), name="home"),
    path("", home2, name="home"),
    path('add_Item', Additem.as_view(), name="additem"),
    path('details/<int:pk>/', Detail_on_id.as_view(), name="details"),
    path('update/<int:pk>/', Updateitem.as_view(), name="updateitem"),
    path('delete/<int:pk>/', Delete.as_view(), name="delete"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(next_page='home'), name="logout"),
    path('user_registration/', Register.as_view(), name='registration'),
]
