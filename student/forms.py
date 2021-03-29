from .models import Dorm_form, Dorm_final
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput


class Dorm_form_form(ModelForm):
    class Meta:
        model = Dorm_form
        fields = "__all__"
        labels = {
            "q1": "Есть психические расстройства?",
            "q2": "Есть или было домашнее животное?",
            "q3": "Вас обижали в школе?",
            "iq": "Ващ IQ",
            "kids_in_family": "Сколько детей в семье?",
            "whats_number": "Какой по счету вы?",
            "Friends_count": "Сколько у вас друзей?",
        }
        widgets = {
            "iq": NumberInput(attrs={
                'class': 'form-control',

            }),
            "kids_in_family": NumberInput(attrs={
                'class': 'form-control',

            }),
            "whats_number": NumberInput(attrs={
                'class': 'form-control',

            }),
            "Friends_count": NumberInput(attrs={
                'class': 'form-control',

            }),
            "q1": CheckboxInput(attrs={
                'class': 'form-control',
            }),
            "q2": CheckboxInput(attrs={
                'class': 'form-control',
            }),
            "q3": CheckboxInput(attrs={
                'class': 'form-control',
            }),
        }


class Dorm_final_form(ModelForm):
    class Meta:
        model = Dorm_final
        fields = "__all__"
        labels = {

            "service_quality": "Оцените качество обслкживания по 10-бальной шкале",
            "neighborhood": "Сколько раз переселялись?",
            "q1": "Вас сейчас бесят соседи?",
            "q2": "Вы рались хотя бы с одним соседом?",
            "q3": "Вы начали курить на постоянной основе?",
            "q4": "Сколько у вас пальцев?",
            "q5": "Сколько волос у вас выпало?",
        }
        widgets = {
            "q1": CheckboxInput(attrs={
                'class': 'form-control',
            }),
            "q2": CheckboxInput(attrs={
                'class': 'form-control',
            }),
            "q3": CheckboxInput(attrs={
                'class': 'form-control',
            }),
            "q4": NumberInput(attrs={
                'class': 'form-control',
            }),
            "q5": NumberInput(attrs={
                'class': 'form-control',
            }),
            "service_quality": NumberInput(attrs={
                'class': 'form-control',
            }),
            "neighborhood": NumberInput(attrs={
                'class': 'form-control',
            }),
        }