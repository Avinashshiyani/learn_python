from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mobile
from .forms import MobileForm

@login_required
def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_mobiles')
    else:
        form = MobileForm()
    return render(request, 'mobiles/add_mobile.html', {'form': form})

@login_required
def display_mobiles(request):
    query = request.GET.get('q', '')
    mobiles = Mobile.objects.filter(model__icontains=query) if query else Mobile.objects.all()
    return render(request, 'mobiles/display_mobiles.html', {'mobiles': mobiles, 'query': query, 'user': request.user})

@login_required
def delete_mobile(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    if request.method == 'POST':
        mobile.delete()
        return redirect('display_mobiles')
    return render(request, 'mobiles/confirm_delete.html', {'mobile': mobile})