from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Members, AdminMember
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages



class MemberListView(ListView):
    model = Members
    template_name = 'member/index.html'
    context_object_name = 'members'
    paginate_by = 4
    def get_queryset(self):
        members = Members.objects.all()
        if self.request.GET.get('name'):
            members = members.filter(full_name__icontains=self.request.GET.get('name'))
        return members
        
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['active'] = 'member'
        return data


def addmember(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member')
    else:
        form = MemberForm()
    return render(request,'member/addmember.html',{'form':form})


class UpdateMember(UpdateView):
    model = Members
    fields = ['full_name','address']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('member')


def inactive(request, pk):
    member = Members.objects.get(pk=pk)
    member.active = False
    member.save()
    return redirect('member')

class AdminMembers(ListView):
    model = AdminMember
    context_object_name = 'admin_members'
    template_name = 'home/base.html'