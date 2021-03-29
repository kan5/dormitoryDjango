from django.shortcuts import render, redirect


# Create your views here.
def main(request):
    if request.user.groups.filter(name='manager').exists():
        return redirect('/manager/editor')
    elif request.user.groups.filter(name='student').exists():
        return redirect('/student/profile')
    elif request.user.groups.filter(name='researcher').exists():
        return redirect('/researcher')
    else:
        return redirect('/accounts/login')
