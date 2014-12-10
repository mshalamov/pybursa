from django.shortcuts import render, get_object_or_404

# Create your views here.
from coaches.models import Coach


def coaches_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/coach_list.html', {'coaches': coaches})


def coach_info(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach})
