from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Info(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='info')
    description=models.TextField()
    age=models.PositiveIntegerField()
    nationality=models.CharField(max_length=100)
    freelance=models.BooleanField(default=True)
    adress=models.CharField(max_length=100)
    adress_point=models.CharField(max_length=500)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Language(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title

class ContactInfo(models.Model):
    logo=models.FileField(upload_to='logos')
    title=models.CharField(max_length=100)
    value=models.CharField(max_length=100)
    link=models.TextField()
    def __str__(self) -> str:
        return f'{self.title} / {self.value}'

class Skill(models.Model):
    name=models.CharField(max_length=100)
    persentage=models.PositiveIntegerField(default=50,validators=[MaxValueValidator(100),MinValueValidator(1)])
    def __str__(self) -> str:
        return f'{self.name}: {self.persentage}'

class Experience(models.Model):
    profession=models.CharField(max_length=200)
    work_place=models.CharField(max_length=300)
    description=models.TextField()
    access_time=models.DateField()
    graduate_time=models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.profession} / {self.work_place}'

class Education(models.Model):
    profession=models.CharField(max_length=200)
    education_place=models.CharField(max_length=300)
    access_time=models.DateField()
    graduate_time=models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.profession} / {self.education_place}'

class PortfolioCategory(models.Model):
    category=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.category

class Portfolio(models.Model):
    title=models.CharField(max_length=300)
    project= models.CharField(max_length=100)
    client=models.CharField(max_length=200,null=True,blank=True)
    category=models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE,related_name='portfolios')
    image=models.ImageField(upload_to='portfolios',null=True,blank=True)
    preview=models.TextField(null=True,blank=True)
    video=models.FileField(upload_to='portfolios/videos',null=True,blank=True)
    iframe_src=models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return f'{self.category} / {self.title}'

class PortfolioLanguage(models.Model):
    portfolio=models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name='languages')
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.portfolio} / {self.name}'

class Tag(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name 

class Blog(models.Model):
    title=models.CharField(max_length=300)
    tags=models.ManyToManyField(Tag,related_name='tags')
    description_part1=models.TextField()
    remember=models.TextField(null=True,blank=True)
    description_part2=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='blogs/images',null=True,blank=True)
    video=models.FileField(upload_to='blogs/videos',null=True,blank=True)
    iframe_src=models.TextField(null=True,blank=True)
    region=models.CharField(max_length=300,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return  self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self) -> str:
        return f'{self.name} / {self.email}'

class Book(models.Model):
    counter=1
    def __init__(self, name,page):
        self.name=name
        self.page=page
        self.id=Book.counter
        Book.counter+=1
    def __str__(self) -> str:
        return self.name