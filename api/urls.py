from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserViewSet, AdminViewSet, StudentViewSet, StaffViewSet, CourseViewSet, SubjectViewSet, AttendanceViewSet, AttendanceReportViewSet,
    LeaveReportStudentViewSet, LeaveReportStaffViewSet, FeedbackStudentViewSet, FeedbackStaffViewSet, NotificationStudentViewSet, NotificationStaffViewSet,
    StudentResultViewSet, LibraryViewSet, HostelViewSet, NoDuesViewSet
)

router = DefaultRouter()
router.register(r'customuser', CustomUserViewSet)
router.register(r'admin', AdminViewSet)
router.register(r'student', StudentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'course', CourseViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'attendance-report', AttendanceReportViewSet)
router.register(r'leave-report-student', LeaveReportStudentViewSet)
router.register(r'leave-report-staff', LeaveReportStaffViewSet)
router.register(r'feedback-student', FeedbackStudentViewSet)
router.register(r'feedback-staff', FeedbackStaffViewSet)
router.register(r'notification-student', NotificationStudentViewSet)
router.register(r'notification-staff', NotificationStaffViewSet)
router.register(r'student-result', StudentResultViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'hostel', HostelViewSet)
router.register(r'no-dues', NoDuesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
