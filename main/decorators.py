from django.shortcuts import redirect
from .models import Farmer

def is_not_farmer(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                farmer = Farmer.objects.get(user=request.user)
                return redirect('unauthorized')
            except Farmer.DoesNotExist:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    
    return _wrapped_view
