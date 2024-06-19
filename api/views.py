# api/views.py
from rest_framework import viewsets
from app.models import CustomUser, Admin, Student, Staff, Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedbackStudent, FeedbackStaff, NotificationStudent, NotificationStaff, StudentResult
from .models import Library, Hostel, NoDues
from .serializers import (
    CustomUserSerializer, AdminSerializer, StudentSerializer, StaffSerializer, CourseSerializer, SubjectSerializer, AttendanceSerializer, AttendanceReportSerializer,
    LeaveReportStudentSerializer, LeaveReportStaffSerializer, FeedbackStudentSerializer, FeedbackStaffSerializer, NotificationStudentSerializer, NotificationStaffSerializer,
    StudentResultSerializer, LibrarySerializer, HostelSerializer, NoDuesSerializer
)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceReportViewSet(viewsets.ModelViewSet):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer

class LeaveReportStudentViewSet(viewsets.ModelViewSet):
    queryset = LeaveReportStudent.objects.all()
    serializer_class = LeaveReportStudentSerializer

class LeaveReportStaffViewSet(viewsets.ModelViewSet):
    queryset = LeaveReportStaff.objects.all()
    serializer_class = LeaveReportStaffSerializer

class FeedbackStudentViewSet(viewsets.ModelViewSet):
    queryset = FeedbackStudent.objects.all()
    serializer_class = FeedbackStudentSerializer

class FeedbackStaffViewSet(viewsets.ModelViewSet):
    queryset = FeedbackStaff.objects.all()
    serializer_class = FeedbackStaffSerializer

class NotificationStudentViewSet(viewsets.ModelViewSet):
    queryset = NotificationStudent.objects.all()
    serializer_class = NotificationStudentSerializer

class NotificationStaffViewSet(viewsets.ModelViewSet):
    queryset = NotificationStaff.objects.all()
    serializer_class = NotificationStaffSerializer

class StudentResultViewSet(viewsets.ModelViewSet):
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class NoDuesViewSet(viewsets.ModelViewSet):
    queryset = NoDues.objects.all()
    serializer_class = NoDuesSerializer
