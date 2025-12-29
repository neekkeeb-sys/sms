from django.forms import ModelForm
from .models import Student, Attendance, Marks, Notice

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class MarksForm(ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'

class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
