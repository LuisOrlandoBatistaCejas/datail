"""datail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView
from django.conf.urls import url, include
from rest_framework import routers
from comprobante_detalles.views import DetailsViewset
from comprobante.views import ComprobanteViewset

router = routers.DefaultRouter()
router.register(prefix='details', viewset=DetailsViewset)
router.register(prefix='comprobante', viewset=ComprobanteViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', serve, kwargs={'path': 'angular-material-flexLayout/index.html'} ),
    url(r'^rest/', include(router.urls)),
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$', RedirectView.as_view(url='/static/angular-material-flexLayout/%(path)s', permanent=False)),
]
