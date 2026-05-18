from django.contrib import admin
from .models import LessonProgress, AssignmentSubmission

@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed', 'lesson__course')
    search_fields = ('student__name', 'lesson__title')

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'grade', 'submitted_at')
    list_filter = ('lesson__course', 'grade')
    search_fields = ('student__name', 'lesson__title')
    list_editable = ('grade',) # Permite poner la nota directamente desde la lista
    readonly_fields = ('submitted_at',)
