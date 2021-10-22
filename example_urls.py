# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('public_site.urls')),
    path('user/', include('user_site.urls')),
    path('auth/', include('auth_app.urls')),
    path('users/', include('users.urls')),
    path('registration/', include('registration.urls')),
    path('conferences/', include('conferences.urls')),
    path('submissions/', include('submissions.urls')),
    path('chair/', include('chair.urls')),
    path('chair_mail/', include('chair_mail.urls')),
    path('review/', include('review.urls')),
    path('gears/', include('gears.urls')),
    path('proceedings/', include('proceedings.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.USE_LOCAL_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns



## ... source file continues with no further include examples...
