from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ("Date information", {
            'fields': ['pub_date'], 'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    readonly_fields = ('pub_date', )

    def published_recently(self, question):
        return question.was_published_recently()
    published_recently.admin_order_field = 'pub_date'
    published_recently.boolean = True
    published_recently.short_description = "Published recently?"
admin.site.register(Question, QuestionAdmin)  # noqa: E305
