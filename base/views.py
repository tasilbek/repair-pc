from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'pages/index.html'
class NumberPageView(TemplateView):
    template_name = 'pages/404.html'
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
class BlogSinglePageView(TemplateView):
    template_name = 'pages/blog-single.html'
class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'
class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
class FAQPageView(TemplateView):
    template_name = 'pages/faq.html'
class Index2PageView(TemplateView):
    template_name = 'pages/index-2.html'
class PricePageView(TemplateView):
    template_name = 'pages/price.html'
class ProjectPageView(TemplateView):
    template_name = 'pages/project.html'
class ServicePageView(TemplateView):
    template_name = 'pages/service.html'
class SingleProjectPageView(TemplateView):
    template_name = 'pages/single-project.html'
class TeamPageView(TemplateView):
    template_name = 'pages/team.html'
