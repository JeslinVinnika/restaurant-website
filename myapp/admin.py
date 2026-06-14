from django.contrib import admin
from myapp.models import Booking
from myapp.models import Contact
from .models import Newsletter
from .models import Comment
# Register your models here.
admin.site.site_header = 'FoodZone | Admin'

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

admin.site.register(Contact)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','booking_date','booking_time']

admin.site.register(Booking)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email','created_at']
admin.site.register(Newsletter,NewsletterAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
admin.site.register(Comment,CommentAdmin)