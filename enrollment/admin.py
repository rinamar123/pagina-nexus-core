from django.contrib import admin
from .models import Course, Student, CourseContent, InteractiveChallenge, ChallengeAttempt

class InteractiveChallengeInline(admin.StackedInline):
    model = InteractiveChallenge
    extra = 1

@admin.register(CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'section_type', 'order')
    list_filter = ('course', 'section_type')
    inlines = [InteractiveChallengeInline]

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(ChallengeAttempt)
