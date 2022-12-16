from django.shortcuts import render, redirect
from . forms import *

# Create your views here.
def index(request):
    return render(request, 'work/index.html')

def work(request):
    all_work_plan = work_plan.objects.all()
    form = work_plan_Forms()

    if request.method == 'POST':
        form = work_plan_Forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'all_work_plan': all_work_plan,
               'form': form,
               'title': 'Заказ',
               }
    return render(request, 'work/work.html', context)

def plan(request):
    all_work_plan = work_plan.objects.all()
    form = work_plan_Forms()

    if request.method == 'POST':
        form = work_plan_Forms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'all_work_plan': all_work_plan,
               'form': form,
               'title': 'Заказ',
               }
    return render(request, 'work/plan.html', context)