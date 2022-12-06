from django.urls import path
from .. import views
urlpatterns = [
    path('',views.BlogListCreateAPIView.as_view()),
    path('<int:pk>/',views.BlogDetailAPIView.as_view()),

    path('tags/',views.TagListCreateAPIView.as_view()),
    path('tags/<int:pk>/',views.TagDetailAPIView.as_view()),
]
