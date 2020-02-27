from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(type)
admin.site.register(author)
admin.site.register(Article)
admin.site.register(User)


