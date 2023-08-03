from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Months, Tasks


# Create your views here.
def todo(request):
    return render(request, 'schedule/schedule.html', {
        'months': Months.objects.all()
    })


def redirect_to(request, id):
    month = Months.objects.get(id=id)
    print(month)
    return HttpResponseRedirect(f'todo/{month.title}')


def read(request, title):
    return render(request, 'schedule/todo.html', {
        'months': Months.objects.all(),
        'tasks': Tasks.objects.filter(month=Months.objects.get(title=title)),
        'selected_month': title
    })
