"""boutique_ado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for authentication
    path('', include('home.urls')), # Include URLs for the home app
    path('products/', include('products.urls')),  # Include URLs for the products app
    path('bag/', include('bag.urls')),  # Include URLs for the shopping bag app
    path('checkout/', include('checkout.urls')), # Include URLs for the checkout app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
