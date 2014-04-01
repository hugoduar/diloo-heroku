from django.contrib import admin
from dilooapp.models import *
# Register your models here.
admin.site.register(Critic)
admin.site.register(Category)

admin.site.register(Thing)
admin.site.register(Topic)

admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Note)