"""portfolio URL Configuration


    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',jobs.views.home,name='home'),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
