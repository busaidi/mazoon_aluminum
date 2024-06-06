from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('i18n/', include('django.conf.urls.i18n')),  # Add this line
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('users.urls')),
    path('blog/', include('blog.urls')),
)
