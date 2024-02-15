from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib import messages
from .models import UserProfile,Portfolio,Education,Workexperience,Certificate,Technology
from .forms import ContactForm
from django.views import generic

class  IndexView(generic.TemplateView):
    template_name = "portfolio_projects/index.html"
    def get_context_data(self, **kwargs):
        #return super().get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        certificates = Certificate.objects.filter(is_active=True)
        portfolios = Portfolio.objects.filter(is_active=True)
        education = Education.objects.filter(is_active=True)
        experience = Workexperience.objects.filter(is_active=True)
        technologies = Technology.objects.all()

        context["certificates"] = certificates
        context["portfolio"] = portfolios
        context["education"] = education
        context["experience"] = experience
        #context["technologies"] = technologies
       # print(technologies)
        return context

#class AboutmeView(generic.TemplateView):
 #   template_name = 'portfolio_projects/aboutme.html'    
    
class ContactView(generic.FormView):
    template_name = "portfolio_projects/contact.html"
    form_class = ContactForm   
    success_url= "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you')
        return super().form_valid(form)
    
class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "portfolio_projects/portfolio.html"
    paginate_by = 10

    def get_queryset(self) :
        return super().get_queryset().filter(is_active=True)
    
        
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "portfolio_projects/portfolio-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()
        technologies = portfolio.technology.all()  # Fetching related technologies
        context['technologies'] = technologies
        return context


#class EducationView(generic.DetailView):
class WorkExperineceView(generic.ListView):
    model = Workexperience
    template_name = "portfolio_projects/experience.html"
    def get_queryset(self):
        print(QuerySet)
        return super().get_queryset().filter(is_active=True)

class WorkExperienceDetailView(generic.DetailView):
    model = Workexperience
    template_name = "portfolio_projects/experience-detail.html"
