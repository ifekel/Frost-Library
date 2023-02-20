from django.urls import path
from .views import BookListPageView, bookListDetailView

urlpatterns = [
    path('', BookListPageView.as_view(), name='book_list'),
    path('<uuid:pk>', bookListDetailView.as_view(), name='book_item'),
]
