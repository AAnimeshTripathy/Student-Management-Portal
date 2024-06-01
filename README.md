# Student Management Portal

This is a robust Student Management Portal developed using Django. It provides a comprehensive solution for managing students, staff, courses, and attendance. The system is designed to be user-friendly and efficient, making it easy for administrators, teachers, and students to access and manage information.

## Ongoing Development
Currently working on REST APIs to provide data to other systems like library management, hostel management, No dues management, etc.

[Front-end Template](http://adminlte.io "Admin LTE.io")

## Passport/Images
Images are from [Unsplash](https://unsplash.com)
## Features of this Project

### A. Capabilities for Admin Users
1. Access comprehensive summary charts showcasing student performance, staff performance, course statistics, subject details, leave records, and more.
2. Handle staff management tasks, including adding, updating, and removing staff members.
3. Oversee student management by adding, updating, and deleting student records.
4. Administer courses with options to add, update, and delete courses.
5. Manage subjects by adding, updating, and deleting subject information.
6. Supervise session management, including the ability to add, update, and delete sessions.
7. Monitor student attendance records.
8. Review and respond to feedback from students and staff.
9. Approve or reject leave applications submitted by students and staff.

### B. Capabilities for Staff/Teachers
1. Access summary charts that provide insights into their students' performance, subjects, and leave status.
2. Record and update student attendance.
3. Enter and modify student results.
4. Submit leave applications.
5. Send feedback to the Head of Department (HOD).

### C. Capabilities for Students
1. View summary charts related to their attendance, subjects, and leave status.
2. Check their attendance records.
3. Access their academic results.
4. Apply for leave.
5. Send feedback to the Head of Department (HOD).

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
2. Install Python Latest Version
3. Install Pip (Package Manager)

### Installation
1. **Create a Folder where you want to save the project**

2. **Create a Virtual Environment and Activate**

   Install Virtual Environment First
   ```
   $  pip install virtualenv
   ```

   Create Virtual Environment
   ```
   $  python -m venv venv
   ```

   Activate Virtual Environment
   ```
   $  source venv/bin/activate
   ```

3. **Clone this project**
   ```
   $  git clone https://github.com/AAnimeshTripathy/Student-Management-Portal.git
   ```

   Then, Enter the project
   ```
   $  cd student-management-using-django
   ```

4. **Install Requirements from 'requirements.txt'**
   ```python
   $  pip3 install -r requirements.txt
   ```

5. **Add the hosts**
   - Go to settings.py file 
   - On allowed hosts, Use **[]** as your host.
   ```python
   ALLOWED_HOSTS = []
   ```

6. **Run Server**

   ```
   $ python manage.py runserver
   ```

7. **Login Credentials**

   Create Super User (HOD)
   ```
   $  python manage.py createsuperuser
   ```

   Then Add Email and Password


