from django.contrib import admin
from Service.admin import user_admin_site
from product.models import *

admin.site.register(item)
admin.site.register(category)

user_admin_site.register(item)
user_admin_site.register(category)