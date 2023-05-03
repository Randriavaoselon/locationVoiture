from django.contrib import admin

from django.urls import include, re_path
#from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('agence.urls')),
    re_path('', include('voiture.urls')),
    re_path('', include('users.urls')),
    re_path('', include('location.urls')),
    re_path('', include('paiement.urls')),
    re_path('', include('teste.urls')),
    #re_path('', include('vehicule.urls')),


    re_path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='client/loueur/login.html',
                                         authentication_form=LoginForm), name='login'),

    re_path('logout/', auth_views.LogoutView.as_view(template_name='client/loueur/logout.html'), name='logout'),

    re_path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    re_path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='client/loueur/password_reset_confirm.html'),
        name='password_reset_confirm'),

    re_path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='client/loueur/password_reset_complete.html'),
        name='password_reset_complete'),

    re_path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
