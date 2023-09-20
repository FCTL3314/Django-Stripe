from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")
    ordering = ("name",)
    readonly_fields = ("stripe_price_id",)
