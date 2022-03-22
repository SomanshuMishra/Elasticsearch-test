from django.urls import path ,include
from search.views import SearchImportKey , SearchPostImportKey

urlpatterns = [
    path('search/<str:query>/',SearchImportKey.as_view()),
    path('search_post/',SearchPostImportKey.as_view())
]