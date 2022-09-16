"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from service_order.views import RegisterAccount, AccountDetails, LoginAccount, ContactView, CategoryView, ShopView, ProductInfoView, BasketView, OrderView, PartnerOrders, PartnerState, PartnerUpdate

app_name = 'service_order'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    ]
