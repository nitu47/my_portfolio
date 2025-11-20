from django.contrib import admin
from .models import Project, Message, Photo, Certificate

admin.site.register(Project)
admin.site.register(Message)
admin.site.register(Photo)
admin.site.register(Certificate)
