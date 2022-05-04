from django.contrib import admin

from .models import Feedback, Inputclas


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'date', 'happy',)
    list_filter = ('date',)
    search_fields = ('details',)

    class Meta:
        model = Feedback
        
class InputAdmin(admin.ModelAdmin):
    list_display = ('inputmsg',)
    class Meta:
        model = Inputclas

admin.site.register(Feedback, FeedbackAdmin,)
admin.site.register(Inputclas, InputAdmin,)
