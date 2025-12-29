from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Attendance, Marks, Notice
from .forms import StudentForm, AttendanceForm, MarksForm, NoticeForm

def home(request):
    return render(request, 'students/home.html', {
        'students': Student.objects.all(),
        'attendance': Attendance.objects.all(),
        'marks': Marks.objects.all(),
        'notices': Notice.objects.all(),
    })

# ---- ADD (Create) views in same style ----
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})

def add_attendance(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Attendance'})

def add_marks(request):
    form = MarksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Marks'})

def add_notice(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Notice'})

# ---- (Optional) Edit/Delete, same pattern ----
def edit_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/form.html', {'form': form, 'title': 'Edit Student'})

def delete_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
    return render(request, 'students/confirm_delete.html', {'object': obj, 'title': 'Delete Student'})
