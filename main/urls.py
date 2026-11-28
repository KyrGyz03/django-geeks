
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from blog.views import helloWorld, about_me, blogMem_view, blogMem_detail
from cars.views import car_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blogMem_view),
    path('blog/<int:id>/', blogMem_detail),
    path('cars_list/', car_list),
    path('helloWorld/', helloWorld),
    path('about_me/', about_me),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)