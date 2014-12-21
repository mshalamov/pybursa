from django.shortcuts import render, redirect, get_object_or_404

from coaches.models import Coach, CoachForm, CoachModelForm


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/coach_list.html', {'coaches': coaches})


def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach})


def coach_edit(request, coach_id):
    title = "Edit Coach"
    coach = Coach.objects.get(id=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            coach.first_name = form.cleaned_data['first_name']
            coach.last_name = form.cleaned_data['last_name']
            coach.coach_type = form.cleaned_data['coach_type']
            coach.save()
            return redirect('coach_edit', coach_id)
    else:
        form = CoachForm(initial={'first_name': coach.first_name,
                                  'last_name': coach.last_name,
                                  'coach_type': coach.coach_type})
    return render(request,
                  'coaches/coach_edit.html',
                  {'form': form, 'title': title})


def coach_add(request):
    title = "Add Coach"
    if request.method == 'POST':
        form = CoachModelForm(request.POST)
        if form.is_valid():
            coach = form.save()
            return redirect('coach_edit', coach.id)
    else:
        form = CoachModelForm()
    return render(request,
                  'coaches/coach_edit.html',
                  {'form': form, 'title': title})
