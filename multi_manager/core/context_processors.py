from .models import Company
def user_company(request):
    return {
        'current_company': Company.objects.get(id=request.session['tenant'])   
    }