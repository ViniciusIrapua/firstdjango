from django.contrib import admin
from .models import News, Contact

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('nw_id', 'nw_date', 'nw_author', 'nw_title', 'nw_status')
    search_fields = ('nw_title', 'nw_author')
    list_filter = ('nw_status', 'nw_date')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('ct_id', 'ct_date', 'ct_name', 'ct_email', 'ct_subject', 'ct_status')
    search_fields = ('ct_name', 'ct_email', 'ct_subject')
    list_filter = ('ct_status', 'ct_date')
