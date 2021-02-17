from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(extract_image)
class extract_imageAdmin(admin.ModelAdmin):
  list_display = ['due_date', 'account_no','bill_amount']
