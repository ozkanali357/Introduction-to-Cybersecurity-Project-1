from django.contrib import admin
from .models import User, InsecureDirectObjectReference

# Optional: You can define admin classes for your models if you want custom admin behavior
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'email')
#     search_fields = ('username',)

# class InsecureDirectObjectReferenceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'document')
#     search_fields = ('user__username',)

admin.site.register(User)
admin.site.register(InsecureDirectObjectReference)