from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('post/<int:pk>/', views.post, name='post'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('like/', views.like_post, name='like_post'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Admin Th"
