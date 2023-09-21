from django.views.generic import TemplateView
from rest_framework.views import APIView

from orders.services import CreateItemStripeSessionID


class SuccessOrderTemplateView(TemplateView):
    template_name = "orders/success_payment.html"


class OrderCanceledTemplateView(TemplateView):
    template_name = "orders/payment_canceled.html"


class BuyItemAPIView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        return CreateItemStripeSessionID(kwargs["id"]).execute()
