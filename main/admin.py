from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'date', 'happy',)
    list_filter = ('date',)
    search_fields = ('details',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
