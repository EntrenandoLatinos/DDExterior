from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app_core.models import Service

class ServiceSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Service.objects.all()

    def location(self, item):
        return reverse('app_core:services_view', args=[item.pk])
    
class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['index', 'about', 'works', 'faq', 'contact', 'privacy']

    def location(self, item):
        return reverse(f'app_core:{item}')