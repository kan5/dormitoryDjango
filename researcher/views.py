import csv

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render

from student.models import *


def is_researcher(user):
    return user.groups.filter(name='researcher').exists()


# Create your views here.
@user_passes_test(is_researcher)
def main(request):
    return render(request, 'researcher/main.html')


@user_passes_test(is_researcher)
def csv_st(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'surname', 'patronymic', 'born', 'city_of_registration', 'group', 'course', 'room',
                     'dorm_form', 'dorm_final'])

    for member in Student.objects.all().values_list('id', 'name', 'surname', 'patronymic',
                                                    'born','city_of_registration',
                                                    'group', 'course', 'room', 'dorm_form', 'dorm_final'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="st.csv"'

    return response


@user_passes_test(is_researcher)
def csv_in(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['id', 'Friends_count', 'whats_number', 'kids_in_family', 'iq', 'psy ill',
                     'have a pet', 'get bulling in school'])

    for member in Dorm_form.objects.all().values_list('id', 'Friends_count', 'whats_number', 'kids_in_family', 'iq',
                                                      'q1', 'q2', 'q3'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="in.csv"'

    return response


@user_passes_test(is_researcher)
def csv_out(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['id', 'service_quality', 'neighborhood changes', 'is_angry', 'fighted',
                     'start smoke', 'fingers count', 'minus hair'])

    for member in Dorm_final.objects.all().values_list('id', "service_quality", "neighborhood",
                                                       "q1", "q2", "q3", "q4", "q5"):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="out.csv"'

    return response


@user_passes_test(is_researcher)
def csv_rooms(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['number', 'places'])

    for member in Rooms.objects.all().values_list('number', 'places'):
        writer.writerow(member)

    response['Content-Disposition'] = 'attachment; filename="rooms.csv"'

    return response
