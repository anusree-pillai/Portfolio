from django.urls import path
from . import views


app_name = "portfolio_projects"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('experience/', views.WorkExperineceView.as_view(), name="experience"),
	path('experience/<slug:slug>/', views.WorkExperienceDetailView.as_view(), name="experience"),
   # path('aboutme/', views.AboutmeView.as_view(), name="aboutme"),
	]