from student.models import *
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, Select, DateInput


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = [
            "surname",
            "name",
            "patronymic",
            "born",
            "city_of_registration",
            "group",
            "course",
            "is_need_dorm",
            "room",
            # "dorm_form",
            # "dorm_final"
        ]
        labels = {
            "surname": "Фамилия",
            "name": "Имя",
            "patronymic": "Отчество",
            "born": "Дата рождения",
            "city_of_registration": "Город прописки",
            "group": "Группа",
            "course": "Курс",
            "is_need_dorm": "Потребность в общежитии",
            "room": "Комната",
            # "dorm_form": "Наличие анкета на заселение",
            # "dorm_final": "Наличие анкета на оценки"
        }
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',

            }),
            "name": TextInput(attrs={
                'class': 'form-control',

            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',

            }),
            "born": DateInput(attrs={
                'class': 'form-control',

            }),
            "city_of_registration": TextInput(attrs={
                'class': 'form-control',

            }),
            "group": TextInput(attrs={
                'class': 'form-control',

            }),
            "course": NumberInput(attrs={
                'class': 'form-control',

            }),
            "is_need_dorm": CheckboxInput(attrs={
                'class': 'form-control',

            }),
            "room": Select(attrs={
                'class': 'form-control',

            }),
            # "dorm_form": CheckboxInput(attrs={
            #     'class': 'form-control',
            #
            # }),
            # "dorm_final": CheckboxInput(attrs={
            #     'class': 'form-control',
            #
            # })
        }


class RoomsForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ['number',
                  'places'
                  ]
        labels = {
            'number': 'Номер окомнаты',
            'places': 'Количество мест'
        }
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
            }),
            "places": NumberInput(attrs={
                'class': 'form-control',
            })
        }


