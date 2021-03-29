from django.shortcuts import render
from .forms import Dorm_form_form, Dorm_final_form
from .models import Student
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import user_passes_test


def is_student(user):
    return user.groups.filter(name='student').exists()

# Create your views here.
@user_passes_test(is_student)
def profile(request):
    std = Student.objects.get(user=request.user)
    return render(request, 'student/profile.html', {"std": std})


@user_passes_test(is_student)
def in_form(request):
    error = ''
    std = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = Dorm_form_form(request.POST)
        if form.is_valid():
            if std.dorm_form is not None:
                std.dorm_form.delete()
            form.save()
            std.dorm_form = form.instance
            std.save()
            error = 'Форма успешно отправлена!'
        else:
            error = 'Ошибка заполнения!'

    if std.dorm_form is not None:
        form = Dorm_form_form(initial=model_to_dict(std.dorm_form))
    else:
        form = Dorm_form_form()

    data = {
        "form": form,
        "error": error
    }
    return render(request, 'student/in_form.html', data)


@user_passes_test(is_student)
def out_form(request):
    error = ''
    std = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = Dorm_final_form(request.POST)
        if form.is_valid():
            if std.dorm_final is not None:
                std.dorm_final.delete()
            form.save()
            std.dorm_final = form.instance
            std.save()
            error = 'Форма успешно отправлена!'
        else:
            error = 'Ошибка заполнения!'

    if std.dorm_final is not None:
        form = Dorm_final_form(initial=model_to_dict(std.dorm_final))
    else:
        form = Dorm_final_form()

    data = {
        "form": form,
        "error": error
    }
    return render(request, 'student/out_form.html', data)
