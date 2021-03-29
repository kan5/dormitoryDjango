from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from student.models import *
from .forms import StudentForm, RoomsForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User, Group


def is_manager(user):
    return user.groups.filter(name='manager').exists()


def transliterate(name):
    """
    Автор: LarsKort
    Дата: 16/07/2011; 1:05 GMT-4;
    Не претендую на "хорошесть" словарика. В моем случае и такой пойдет,
    вы всегда сможете добавить свои символы и даже слова. Только
    это нужно делать в обоих списках, иначе будет ошибка.
    """
    # Слоаврь с заменами
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name

# Create your views here.
@user_passes_test(is_manager)
def editor(request):
    students = Student.objects.all()
    data = {
        "students": students
    }
    return render(request, 'manager/editor.html', data)


@user_passes_test(is_manager)
def new_student(request):
    error = ''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            inst = form.instance
            username = transliterate(f'{inst.surname[0].lower()}{inst.patronymic[0].lower()}{inst.name.lower()}')
            password = User.objects.make_random_password()
            c = 1
            while User.objects.filter(username=username).exists():
                username = username[:-1] + str(c)
                c += 1
            user = User.objects.create_user(username=username, password=password)
            user.save()
            my_group = Group.objects.get(name='student')
            my_group.user_set.add(user)
            my_group.save()
            inst.user = user
            form.save()
            return render(request, 'manager/new_student_success.html', {"form": form,
                                                                        "username": username,
                                                                        "password": password})
            error = 'Форма успешно отправлена!'

        error = 'Ошибка заполнения!'

    form = StudentForm()

    data = {
        "form": form,
        "error": error,
    }
    return render(request, 'manager/new_student.html', data)


@user_passes_test(is_manager)
def rooms(request):
    roomses = Rooms.objects.order_by('number')
    data = {
        "rooms": roomses,
    }
    return render(request, 'manager/rooms.html', data)


class StudentView(UpdateView):
    model = Student
    template_name = "manager/form.html"
    success_url = "/manager/editor"
    form_class = StudentForm

    @method_decorator(user_passes_test(lambda u: is_manager(u)))
    def dispatch(self, *args, **kwargs):
        return super(StudentView, self).dispatch(*args, **kwargs)


class StudentDelete(DeleteView):
    model = User
    template_name = "manager/student_delete.html"
    success_url = '/manager/editor'

    @method_decorator(user_passes_test(lambda u: is_manager(u)))
    def dispatch(self, *args, **kwargs):
        return super(StudentDelete, self).dispatch(*args, **kwargs)


class RoomsView(UpdateView):
    model = Rooms
    template_name = "manager/room_form.html"
    success_url = "/manager/rooms"
    form_class = RoomsForm

    @method_decorator(user_passes_test(lambda u: is_manager(u)))
    def dispatch(self, *args, **kwargs):
        return super(RoomsView, self).dispatch(*args, **kwargs)


class RoomsCreate(CreateView):
    model = Rooms
    form_class = RoomsForm
    template_name = "manager/room_add.html"
    success_url = '/manager/rooms'

    @method_decorator(user_passes_test(lambda u: is_manager(u)))
    def dispatch(self, *args, **kwargs):
        return super(RoomsCreate, self).dispatch(*args, **kwargs)


class RoomsDelete(DeleteView):
    model = Rooms
    template_name = "manager/room_delete.html"
    success_url = '/manager/rooms'

    @method_decorator(user_passes_test(lambda u: is_manager(u)))
    def dispatch(self, *args, **kwargs):
        return super(RoomsDelete, self).dispatch(*args, **kwargs)
