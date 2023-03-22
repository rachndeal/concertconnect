import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'concertconnect.settings')

import django
django.setup()
from concertconnect_app.models import Category, Page


def populate():
   
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/','views':23},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/','views':76},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/','views':100}]
        
    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views':7},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/','views':18},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/','views':127}]

    other_pages = [
        {'title':'Bottle',
            'url':'http://bottlepy.org/docs/dev/','views':19},
        {'title':'Flask',
            'url':'http://flask.pocoo.org','views':34}]

    cats = {'Python': {'pages': python_pages, 'views':128, 'likes':64},
            'Django': {'pages': django_pages, 'views':64,'likes':32},
            'Other Frameworks': {'pages': other_pages, 'views':32,'likes':16}
           }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'] )
 
    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting ConcertConnects population script...')
    populate()
