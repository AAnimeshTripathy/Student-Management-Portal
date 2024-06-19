from django.db import models
from app.models import Student, Staff 

class Library(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    books_issued = models.IntegerField(default=0)
    books_returned = models.IntegerField(default=0)
    fine_due = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.admin.first_name} {self.student.admin.last_name} - Library Record"

class Hostel(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    stay_duration = models.CharField(max_length=50)
    rent_due = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.admin.first_name} {self.student.admin.last_name} - Hostel Record"

class NoDues(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    library_clearance = models.BooleanField(default=False)
    hostel_clearance = models.BooleanField(default=False)
    other_dues = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.admin.first_name} {self.student.admin.last_name} - No Dues Record"
