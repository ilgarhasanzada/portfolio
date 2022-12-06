from django.urls import path
from .. import views
urlpatterns = [
    path('',views.AboutListCreateAPIView.as_view()),
    path('<int:pk>/',views.AboutDetailAPIView.as_view()),

    path('languages/',views.LanguageListCreateAPIView.as_view()),
    path('languages/<int:pk>/',views.LanguageDetailAPIView.as_view()),

    path('contacts/',views.ContactInfoListCreateAPIView.as_view()),
    path('contacts/<int:pk>/',views.ContactInfoDetailAPIView.as_view()),

    path('skills/',views.SkillListCreateAPIView.as_view()),
    path('skills/<int:pk>/',views.SkillDetailAPIView.as_view()),
    
    path('education/',views.EducationListCreateAPIView.as_view()),
    path('education/<int:pk>/',views.EducationDetailAPIView.as_view()),
    
    path('experience/',views.ExperienceListCreateAPIView.as_view()),
    path('experience/<int:pk>/',views.ExperienceDetailAPIView.as_view()),

]
