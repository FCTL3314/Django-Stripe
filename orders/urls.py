from django.urls import path

from orders.views import (
    SuccessOrderTemplateView,
    OrderCanceledTemplateView,
    BuyItemAPIView,
)

app_name = "orders"

urlpatterns = [
    path("order-success/", SuccessOrderTemplateView.as_view(), name="order-success"),
    path("order-canceled/", OrderCanceledTemplateView.as_view(), name="order-canceled"),
    path("buy/<int:id>/", BuyItemAPIView.as_view(), name="buy-item"),
]
