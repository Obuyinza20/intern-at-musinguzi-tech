
from django.contrib import admin
from django.urls import path , include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logged-out/', logoutPage, name= 'logout'),
    path('login/', loginPage, name= 'login'),
    # path('signup/', signUp, name= 'signup'),
    path('', home , name='home'),
    path('application/' , application, name='application'),
    path('internees/' , interneeView, name='view_internees'),
    path('internees/<str:pk>/' , singleInternee, name='singleinternee'),
    path('accepted_internee/<str:pk>/' , accept, name='accepted_internee'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
