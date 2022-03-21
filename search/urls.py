from django.urls import path ,include
from search.views import SearchImportKey

urlpatterns = [
    path('search/<str:query>/',SearchImportKey.as_view())
]