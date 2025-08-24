from django.contrib import admin
from my_first_app.models import Topic, WebPage, AccessRecord

# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)

