from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    AdminLoginView,AdminDashboardView,AdminUserView,AdminUserCreate,
    DeleteUserView,AdminUserProfileView,ProductCreationView,AdminProductView,
    AdminProductById,AdminProductDeleteAndUpdateView, ToggleUserActiveStatus,
)

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='login'),
    path('dashboard/', AdminDashboardView.as_view(), name='dashboard'),
    path('users/', AdminUserView.as_view(), name='admin-user-list'),
    path('user-create/', AdminUserCreate.as_view(), name='admin-user-create'),
    path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name='delete-user'),
    path('user-profile/<int:user_id>/',AdminUserProfileView.as_view(),name='user-profile'),
    path('toggle-user-status/<int:user_id>/', ToggleUserActiveStatus.as_view(), name='toggle-user-status'),
    path('product-create/', ProductCreationView.as_view(), name='product-create'),
    path('product-view/', AdminProductView.as_view(), name='product-view'),
    path('product-by-id/<int:product_id>/', AdminProductById.as_view(), name='admin-product-by-id'),
    path('product-delete/<int:product_id>/', AdminProductDeleteAndUpdateView.as_view(), name='admin-product-delete'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
