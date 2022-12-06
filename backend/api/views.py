from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView
from api.serializers import  BookSerializer,TagSerializer, BlogSerializer, ContactInfoSerializer, ContactSerializer, EducationSerializer, ExperienceSerializer, AboutSerializer, LanguageSerializer, PortfolioCategorySerializer, PortfolioLanguageSerializer, PortfolioSerializer, SkillSerializer
from rest_framework import permissions
from resume.models import Book, Blog, Tag, Contact, ContactInfo, Education, Experience, Info, Language, Portfolio, PortfolioCategory, PortfolioLanguage, Skill
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class AboutListCreateAPIView(ListCreateAPIView):
    queryset=Info.objects.all()
    serializer_class=AboutSerializer

class AboutDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Info.objects.all()
    serializer_class=AboutSerializer

class LanguageListCreateAPIView(ListCreateAPIView):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class LanguageDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializer

class ContactInfoListCreateAPIView(ListCreateAPIView):
    queryset=ContactInfo.objects.all()
    serializer_class=ContactInfoSerializer

class ContactInfoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=ContactInfo.objects.all()
    serializer_class=ContactInfoSerializer

class SkillListCreateAPIView(ListCreateAPIView):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

class SkillDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

class ExperienceListCreateAPIView(ListCreateAPIView):
    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer

class ExperienceDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer


class EducationListCreateAPIView(ListCreateAPIView):
    queryset=Education.objects.all()
    serializer_class=EducationSerializer

class EducationDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Education.objects.all()
    serializer_class=EducationSerializer

class PortfolioListCreateAPIView(ListCreateAPIView):
    queryset=Portfolio.objects.all()
    serializer_class=PortfolioSerializer

class PortfolioDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Portfolio.objects.all()
    serializer_class=PortfolioSerializer

class PortfolioCategoryListCreateAPIView(ListCreateAPIView):
    queryset=PortfolioCategory.objects.all()
    serializer_class=PortfolioCategorySerializer

class PortfolioCategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=PortfolioCategory.objects.all()
    serializer_class=PortfolioCategorySerializer

class PortfolioLanguageListCreateAPIView(ListCreateAPIView):
    queryset=PortfolioLanguage.objects.all()
    serializer_class=PortfolioLanguageSerializer

class PortfolioLanguageDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=PortfolioLanguage.objects.all()
    serializer_class=PortfolioLanguageSerializer

class BlogListCreateAPIView(ListCreateAPIView):
    queryset=Blog.objects.all().order_by("-date")
    serializer_class=BlogSerializer
    # permission_classes=[permissions.IsAuthenticated]
class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class TagListCreateAPIView(ListCreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

class TagDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer

class ContactListCreateAPIView(ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

class BookListApiView(APIView):
    def get(self,request):     
        books=[Book('Book1',18),Book('Book2',25)]
        books.append(Book('ILgar hasanzada',60))
        send_book=[]
        for book in books:
            my_dict=dict()
            my_dict["id"]=book.id
            my_dict["name"]=book.name
            my_dict["pages"]=book.page
            send_book.append(my_dict)
        return Response(data=send_book,status=status.HTTP_200_OK)