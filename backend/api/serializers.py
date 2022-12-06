from rest_framework import serializers

from resume.models import Book, Blog, Contact, Education, Experience, Info,Language,ContactInfo, Portfolio, PortfolioCategory, PortfolioLanguage, Skill, Tag

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields="__all__"

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields="__all__"

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactInfo
        fields="__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields="__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields="__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields="__all__"

class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioCategory
        fields="__all__"
class PortfolioLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=PortfolioLanguage
        fields="__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields="__all__"

class PortfolioSerializer(serializers.ModelSerializer):
    languages=PortfolioLanguageSerializer(many=True,read_only=True)
    category=serializers.StringRelatedField()
    class Meta:
        model=Portfolio
        fields="__all__"

class BlogSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True,read_only=True)
    class Meta:
        model= Blog
        fields="__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"