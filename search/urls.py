from django.urls import path ,include
from search.views import SearchImportKey , SearchPostImportKey ,GetSeller

urlpatterns = [
    path('search/',SearchImportKey.as_view()),
    # path('search/<str:query>/',SearchImportKey.as_view()),
    path('search_post/',SearchPostImportKey.as_view()),
    path('get_seller/',GetSeller.as_view())
]