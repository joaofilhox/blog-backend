from django.contrib import admin
from .models import Post, Comment
from usuarios.models import Usuario

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.owner == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.owner == request.user

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return obj.user == request.user

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
