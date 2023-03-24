from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from datetime import datetime

from concertconnect_app.models import Category, Page, UserProfile

from concertconnect_app.forms import CategoryForm, PageForm
from concertconnect_app.forms import UserForm, UserProfileForm

from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from concertconnect_app.bing_search import run_query
from django.views import View
from django.contrib.auth.models import User


class ConcertsView(View):
    def get(self,request):

        category_list = Category.objects.order_by('name')
        page_list = Page.objects.order_by('title')

        context_dict = {}
        context_dict['categories'] = category_list
        context_dict['pages'] = page_list

        response = render(request, 'concertconnect_app/index.html', context=context_dict)

        visitor_cookie_handler(request)

        context_dict['visits'] = request.session['visits']

        return render(request, 'concertconnect_app/concerts.html', context_dict)



def search_denial():
    # Take the user back to the homepage.
    return redirect(reverse('concertconnect_app:restricted'))

###Chapter 13
def search_bar(request):
    result_list = []
    query = ''
    
    if request.method == 'POST':
        #Until You have made a key You will be sent to this page - if deleted without key, a 404 page shows
        return search_denial() # Delete when key is made 
        
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)
    
    return render(request, 'concertconnect_app/search.html', {'result_list': result_list, 'query': query})




class IndexView(View):
    def get(self, request):
        category_list = Category.objects.order_by('-likes')[:5]
        page_list = Page.objects.order_by('-views')[:5]
        near_list = Category.objects.filter(venue_info__icontains= 'Glasgow')[:5]
        
        context_dict = {}
        context_dict['boldmessage']= 'Events up coming'
        context_dict['near_you'] = near_list
        context_dict['categories'] = category_list
        context_dict['pages'] = page_list

        # Obtain our Response object early so we can add cookie information.
        response = render(request, 'concertconnect_app/index.html', context=context_dict)

 
        visitor_cookie_handler(request)

        return render(request, 'concertconnect_app/index.html', context=context_dict)

class AboutView(View):
    """
    The about view, converted to a class-based approach. DM.
    """
    def get(self, request):
        context_dict = {}
        context_dict = {'name':'Group 4 Team A'} 
        visitor_cookie_handler(request)
        context_dict['visits'] = request.session['visits']

        return render(request, 'concertconnect_app/about.html', context_dict)

class ShowCategoryView(View):
    def create_context_dict(self, category_name_slug):
        context_dict = {}

        try:
            category = Category.objects.get(slug=category_name_slug)
            pages = Page.objects.filter(category=category).order_by('-views')

            context_dict['pages'] = pages
            context_dict['category'] = category
        except Category.DoesNotExist:
            context_dict['pages'] = None
            context_dict['category'] = None
        
        return context_dict
    
    def get(self, request, category_name_slug):
        context_dict = self.create_context_dict(category_name_slug)
        return render(request, 'concertconnect_app/category.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, category_name_slug):
        if request.method == 'POST':# delete both lines when you have key
            return search_denial() ##
        
        context_dict = self.create_context_dict(category_name_slug)
        query = request.POST['query'].strip()

        if query:
            context_dict['result_list'] = run_query(query)
            context_dict['query'] = query
        
        return render(request, 'concertconnect_app/category.html', context_dict)

class AddCategoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = CategoryForm()
        return render(request, 'concertconnect_app/add_category.html', {'form': form})
    
    @method_decorator(login_required)
    def post(self, request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('concertconnect_app:index'))
        else:
            print(form.errors)
        
        return render(request, 'concertconnect_app/add_category.html', {'form': form})

class AddPageView(View):
    def get_category_name(self, category_name_slug):
   
        try:
            category = Category.objects.get(slug=category_name_slug)
        except Category.DoesNotExist:
            category = None
        
        return category
    
    @method_decorator(login_required)
    def get(self, request, category_name_slug):
        form = PageForm()
        category = self.get_category_name(category_name_slug)

        if category is None:
            return redirect(reverse('concertconnect_app:index'))
        
        context_dict = {'form': form, 'category': category}
        return render(request, 'concertconnect_app/add_page.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, category_name_slug):
        form = PageForm(request.POST)
        category = self.get_category_name(category_name_slug)

        if category is None:
            return redirect(reverse('concertconnect_app:index'))
        
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()

            return redirect(reverse('concertconnect_app:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
        
        context_dict = {'form': form, 'category': category}
        return render(request, 'concertconnect_app/add_page.html', context=context_dict)

class RestrictedView(View):
    @method_decorator(login_required)
    def get(self, request):
        context_dict ={'bold': 'Restricted Page'}
        return render(request, 'concertconnect_app/restricted.html', context_dict)

class GotoView(View):
    def get(self, request):
        page_id = request.GET.get('page_id')

        try:
            selected_page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            return redirect(reverse('concertconnect_app:index'))

        selected_page.views = selected_page.views + 1
        selected_page.save()

        return redirect(selected_page.url)

class RegisterProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = UserProfileForm()
        context_dict = {'form': form}
        return render(request, 'concertconnect_app/profile_registration.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('concertconnect_app:index'))
        else:
            print(form.errors)
        
        context_dict = {'form': form}
        return render(request, 'concertconnect_app/profile_registration.html', context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'concerts': user_profile.concerts,
                                'picture': user_profile.picture,})
        
        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('concertconnect_app:index'))
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'concertconnect_app/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('concertconnect_app:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('concertconnect_app:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'concertconnect_app/profile.html', context_dict)

class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = UserProfile.objects.all()

        return render(request, 'concertconnect_app/list_profiles.html', {'user_profile_list': profiles})

class LikeCategoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        category_id = request.GET['category_id']

        try:
            category = Category.objects.get(id=int(category_id))
        except Category.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        
        category.likes = category.likes + 1
        category.save()

        return HttpResponse(category.likes)

class CategorySuggestionView(View):
    def get(self, request):
        if 'suggestion' in request.GET:
            suggestion = request.GET['suggestion']
        else:
            suggestion = ''
        
        category_list = get_category_list(max_results=8, starts_with=suggestion)

        if len(category_list) == 0:
            category_list = Category.objects.order_by('-likes')
        
        return render(request, 'concertconnect_app/categories.html', {'categories': category_list})

class SearchAddPageView(View):
    @method_decorator(login_required)
    def get(self, request):
        category_id = request.GET['category_id']
        title = request.GET['title']
        url = request.GET['url']

        try:
            category = Category.objects.get(id=int(category_id))
        except Category.DoesNotExist:
            return HttpResponse('Error - category not found.')
        except ValueError:
            return HttpResponse('Error - bad category ID.')
        
        p = Page.objects.get_or_create(category=category, title=title, url=url)

        pages = Page.objects.filter(category=category).order_by('-views')
        return render(request, 'concertconnect_app/page_listing.html', {'pages': pages})

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

def get_category_list(max_results=0, starts_with=''):
    category_list = []

    if starts_with:
        category_list = Category.objects.filter(name__istartswith=starts_with)
    
    if max_results > 0:
        if len(category_list) > max_results:
            category_list = category_list[:max_results]
    
    return category_list
