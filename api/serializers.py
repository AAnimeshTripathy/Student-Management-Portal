# api/serializers.py
from rest_framework import serializers
from app.models import CustomUser, Admin, Student, Staff, Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedbackStudent, FeedbackStaff, NotificationStudent, NotificationStaff, StudentResult
from .models import Library, Hostel, NoDues

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = '__all__'

class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStudent
        fields = '__all__'

class LeaveReportStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStaff
        fields = '__all__'

class FeedbackStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackStudent
        fields = '__all__'

class FeedbackStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackStaff
        fields = '__all__'

class NotificationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStudent
        fields = '__all__'

class NotificationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStaff
        fields = '__all__'

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = '__all__'

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class NoDuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoDues
        fields = '__all__'
