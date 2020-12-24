from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from django.views.generic.edit import DeleteView
from .models import About, Service, Project
from .forms import ProjectForm,AboutForm,ServiceForm
from django.core.mail import send_mail
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name="app/home_nav.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:4]
        context['service_list'] = Service.objects.all()
        return context     
class AboutView(ListView):
    model = About
    template_name="app/about.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['service_list'] = Service.objects.all()
        return context 

class CreateServiceView(CreateView):
    model = Service
    form_class = ServiceForm 
    template_name="app/create_services.html"

class UpdateServiceView(UpdateView):
    model = Service
    form_class = ServiceForm  
    template_name="app/update_service.html" 

class ProjectView(ListView):
    model = Project
    template_name="app/portfolio.html"
    context_object_name = 'projects'
    

    
class DetailProjectView(DetailView):
    model = Project
    template_name="app/project_detail.html"
    context_object_name = 'details'
    
class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectForm 
    template_name="app/create_project.html"
    def get_initial(self, *args, **kwargs):
        initial = super(CreateProjectView, self).get_initial(**kwargs)
        initial['author'] = 'author'
        return initial
class UpdateProjectView(UpdateView):
    model = Project
    form_class = ProjectForm 
    template_name="app/update_project.html"



    
class UpdateAboutView(UpdateView):
    model = About
    form_class = AboutForm 
    template_name="app/update_about.html"    


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']


        send_mail(
                message_name,
                message_email,
                message,
                ['zakaryazaim6@gmail.com'],
        )

        return render(request, 'app/contact.html', {'message_name':message_name})

    else:
        return render(request, 'app/contact.html', {})



class DeletingView(DeleteView):
    model = Project
    template_name = 'app/deleteview.html'
    success_url = reverse_lazy('home')
