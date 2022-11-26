from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import admin

# Create your views here.
class CompanySelectionView(TemplateView):
    template_name='company_selection.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update(**admin.site.each_context(self.request))
        return ctx

    def post(self, request, *args, **kwargs):
        request.session['tenant']=request.POST['tenant']
        print('aljsdjkashdkjsa')
        return HttpResponseRedirect(reverse_lazy('admin:index'))