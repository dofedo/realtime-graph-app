from django.urls import path

from graph.consumers import GraphConsumers

ws_urlpatterns = [
    path('ws/graph/', GraphConsumers.as_asgi()),
]