from django.contrib import admin
from app.models import * 
# Register your models here.

admin.site.register(Critic)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Review)