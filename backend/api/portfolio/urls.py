from django.urls import path
from .. import views
urlpatterns = [
    path('',views.PortfolioListCreateAPIView.as_view()),
    path('<int:pk>/',views.PortfolioDetailAPIView.as_view()),

    path('categories/',views.PortfolioCategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/',views.PortfolioCategoryDetailAPIView.as_view()),

    path('languages/',views.PortfolioLanguageListCreateAPIView.as_view()),
    path('languages/<int:pk>/',views.PortfolioLanguageDetailAPIView.as_view()),
    path('books/',views.BookListApiView.as_view()),

]
