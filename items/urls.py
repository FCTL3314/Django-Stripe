from django.urls import path

from items.views import ItemDetailView

app_name = "items"

urlpatterns = [
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
]
