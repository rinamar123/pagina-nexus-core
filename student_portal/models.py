from django.db import models
from enrollment.models import Student, CourseContent, Course

class LessonProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now=True)
    unlocked_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        unique_together = ['student', 'lesson']

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    lesson = models.ForeignKey(CourseContent, on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='submissions/')
    comment = models.TextField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)  # Retroalimentación del docente
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega: {self.student.name} - {self.lesson.title}"

    @property
    def is_late(self):
        from datetime import timedelta
        progress = LessonProgress.objects.filter(student=self.student, lesson=self.lesson).first()
        if progress and progress.unlocked_at:
            return self.submitted_at > progress.unlocked_at + timedelta(days=7)
        return False

    @property
    def delay_days(self):
        progress = LessonProgress.objects.filter(student=self.student, lesson=self.lesson).first()
        if progress and progress.unlocked_at and self.is_late:
            diff = self.submitted_at - progress.unlocked_at
            return diff.days - 7
        return 0

class DiplomaRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En revisión'),
        ('approved', 'Aprobado'),
        ('rejected', 'Rechazado'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='diploma_requests')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='diploma_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['student', 'course']

    def __str__(self):
        return f"Diploma: {self.student.name} - {self.course.title} ({self.get_status_display()})"
