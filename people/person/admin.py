from django.contrib import admin

# Register your models here.
from .models import Person, Education, Jharsewa, Identy,Parent

admin.site.register([Person,Education,Jharsewa,Identy,Parent])
