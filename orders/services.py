import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from stripe.error import StripeError

from common.services import IService
from items.models import Item


class CreateItemStripeSessionID(IService):
    def __init__(self, item_id: int):
        self.item_id = item_id
        self.item = get_object_or_404(Item, id=item_id)

    def execute(self):
        try:
            checkout_session = self.create_checkout_session()
            return self.session_id_successfully_created(checkout_session["id"])
        except StripeError:
            return self.payment_service_error_response()

    def create_checkout_session(self):
        return stripe.checkout.Session.create(
            line_items=[
                {
                    "price": self.item.stripe_price_id,
                    "quantity": 1,
                },
            ],
            metadata={"item_id": self.item_id},
            mode="payment",
            success_url=f"{settings.DOMAIN_NAME}{reverse('orders:order-success')}",
            cancel_url=f"{settings.DOMAIN_NAME}{reverse('orders:order-canceled')}",
        )

    @staticmethod
    def session_id_successfully_created(session_id: str) -> Response:
        return Response(
            data={
                "session_id": session_id,
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def payment_service_error_response() -> Response:
        return Response(
            data={
                "detail": (
                    "Error when trying to contact the payment system "
                    "server, please try again later."
                ),
            },
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
