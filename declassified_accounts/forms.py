from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group


User = get_user_model()


# custom model from that allows us to add permissions and users from the admin page
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # can add users to the group
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        #initialize the form
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # populate the group with its data if it exists
        if self.instance.pk:
            # populates user choices with the entire set
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # save data
        instance = super(GroupAdminForm, self).save()
        # save many-to-many data
        self.save_m2m()
        return instance