from asyncio.windows_events import NULL
from random import choice
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .forms import GroupAdminForm

from declassified_accounts.models import User, Profile


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes
    required fields, plus asks for repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        models = User
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields
    on the user, but replaces the password field with admin's 
    password has display field."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password','username', 'is_active', 'is_admin')

    def clean_password(self):
        """Return initial value, regardless of user input
        done here because field does not have initial value"""
        return self.initial["password"]
    
class UserAdmin(BaseUserAdmin):
    # Forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    """Feilds to display User model
    Overrides the definitions on BaseUserAdmin
    that reference auth.User."""
    list_display = ('email','username','name','is_active','is_admin')
    list_filter = ('is_admin')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal_info', {'fields': ('username','name',)}),
        ('Permissions', {'fields': ('is_active','is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email', 'username', 'password1','password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Registering new UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Profile)

# getting rid of default group for custom form
admin.site.unregister(Group)

# creates custom form
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']

# makes it visibile
admin.site.register(Group, GroupAdmin)