from django.views.generic.detail import DetailView

from items.models import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"
