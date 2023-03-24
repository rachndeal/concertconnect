from django import forms
from concertconnect_app.models import Page, Category
from django.contrib.auth.models import User
from concertconnect_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_superuser',)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('concerts', 'picture',)


# Earlier Chapters

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,
    help_text="Please enter the Venue's name.")
    venue_info= forms.CharField(max_length = Category.REVIEW_MAX_LENGTH, required=False, help_text = "Please Enter Venue info -- include Location")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    # An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH,help_text="Please enter the name of Event.")
    
    url = forms.URLField(max_length=Page.URL_MAX_LENGTH,help_text="Please enter a URL for Event information.")
    
    description = forms.CharField(max_length=Page.DES_MAX_LENGTH,help_text="Please give a brief description of your Upcoming Event")
    
    event_picture = forms.CharField(max_length=Page.URL_MAX_LENGTH, help_text= "Please upload a picture.")
    
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
 # Here, we are hiding the foreign key.
 # we can either exclude the category field from the form,
        exclude = ('category',)
      
 # or specify the fields to include (don't include the category field).
 #fields = ('title', 'url', 'views')
    def clean(self):
        cleaned_data = self.cleaned_data
        event_picture = cleaned_data.get('event_picture')
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
          
        
        return cleaned_data