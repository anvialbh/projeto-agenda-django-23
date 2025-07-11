from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'email',
    ordering =  '-id',
    #list_filter = 'created_date',
    search_fields = 'first_name', 'last_name','email',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'phone', 'email',
    list_display_links = 'first_name', 'last_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering =  '-id',