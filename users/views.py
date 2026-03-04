from django.shortcuts import render, get_object_or_404, redirect
from .models import Motamage


def motamagebis_sia(request):
    motamagebi = Motamage.objects.all()
    return render(request, 'users/user_list.html', {'motamagebi': motamagebi})


def motamage_detail(request, pk):
    motamage = get_object_or_404(Motamage, pk=pk)
    return render(request, 'users/user_detail.html', {'motamage': motamage})


def motamage_washla(request, pk):
    motamage = get_object_or_404(Motamage, pk=pk)
    if request.method == 'POST':
        motamage.delete()
        return redirect('motamagebis_sia')
    return render(request, 'users/user_confirm_delete.html', {'motamage': motamage})
