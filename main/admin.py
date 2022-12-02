from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Region)
admin.site.register(User)
admin.site.register(Views)
admin.site.register(Like)
admin.site.register(News,NewsAdmin)
