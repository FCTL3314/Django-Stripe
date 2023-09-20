import stripe
from django.conf import settings

from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemAPIView(APIView):
    def get(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1NsNRXDUiKPkW2SIF4B3fKQT",
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=settings.DOMAIN_NAME + "/success.html",
            cancel_url=settings.DOMAIN_NAME + "/cancel.html",
        )
