from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from .views import (
#     AdminLoginView
# )

urlpatterns = [
    # path('login/', AdminLoginView.as_view(), name='login'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
