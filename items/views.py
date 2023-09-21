from django.conf import settings
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from items.models import Item


class ItemListView(ListView):
    queryset = Item.objects.all()
    template_name = "items/items.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["STRIPE_API_KEY"] = settings.STRIPE_PUBLIC_KEY
        return context
