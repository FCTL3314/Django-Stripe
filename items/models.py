import stripe
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    stripe_price_id = models.CharField(max_length=128, null=True, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.stripe_price_id:
            self.handle_stripe_objects_creation()
        super().save(force_insert, force_update, using, update_fields)

    def handle_stripe_objects_creation(self) -> None:
        stripe_product_id = self.create_stripe_product()
        self.stripe_price_id = self.create_stripe_product_price_id(stripe_product_id)

    def create_stripe_product(self) -> str:
        product = stripe.Product.create(name=self.name)
        return product["id"]

    def create_stripe_product_price_id(self, product_id: str) -> str:
        price = stripe.Price.create(
            product=product_id,
            unit_amount=round(self.price * 100),
            currency="usd",
        )
        return price["id"]
