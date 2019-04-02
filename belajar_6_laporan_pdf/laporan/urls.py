
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'siswa/',include(('siswa.urls','siswa'), namespace='siswa')),
]
