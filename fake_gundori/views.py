from django.urls import reverse_lazy
from django.views import generic
from .forms import SoldierCreateForm, SoldierUpdateForm, SoldierDeleteForm
from .models import Soldier

# CRUD with Django built-in class-based generic views

# Generic Display View
class SoldierListView(generic.ListView):
    context_object_name = 'soldier_list'
    template_name = 'soldier_list.html'
    paginate_by = 7

    def get_queryset(self):
        return Soldier.objects.all().order_by('enter_date')

class SoldierDetailView(generic.DetailView):
    model = Soldier
    template_name = 'soldier_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SoldierDetailView, self).get_context_data(*args, **kwargs)
        myobject = self.object

        context['pct'] = myobject.percent
        return context


# Generic Edit View
class SoldierCreateView(generic.CreateView):
    form_class = SoldierCreateForm
    template_name = 'soldier_form.html'
    success_url = reverse_lazy('soldier-list')

class SoldierUpdateView(generic.UpdateView):
    model = Soldier
    form_class = SoldierUpdateForm
    template_name = 'soldier_update.html'
    success_url = reverse_lazy('soldier-list')

class SoldierDeleteView(generic.DeleteView):
    model = Soldier
    form_class = SoldierDeleteForm
    template_name = 'soldier_delete.html'
    success_url = reverse_lazy('soldier-list')