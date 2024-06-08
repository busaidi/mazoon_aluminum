from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from users.views import SignUpView, CustomLoginView  # Import the custom login view and sign-up view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use the custom login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),  # Use the sign-up view
    path('accounts/', include('users.urls')),
    path('blog/', include('blog.urls')),
)
