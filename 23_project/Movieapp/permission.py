### PERMISSION FILE ---->>> TO WRITE CUSTOM PERISSION

from rest_framework import permissions


''' Only admin can edit, others can only view(get),
    So we are checking Admin/Staff or others'''
class IsAdminOrReadonly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        


class IsReviewUserorReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.reviewer_name == request.user


class IsReviewUserorReadOnlyorStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.reviewer_name == request.user or request.user.is_staff