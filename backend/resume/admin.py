from django.contrib import admin
from .models import Info, ContactInfo , Language, PortfolioLanguage, Skill, Experience, Education, PortfolioCategory, Portfolio, Blog, Contact, Tag
# Register your models here.
admin.site.register(Info)
admin.site.register(ContactInfo)
admin.site.register(Language)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(PortfolioLanguage)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Contact)