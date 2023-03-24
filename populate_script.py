import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'concertconnect.settings')

import django
django.setup()
from concertconnect_app.models import Category, Page


def populate():

      ao_arena = [
       {'title': 'AO Arenas Disco',
        'url': 'https://www.ao-arena.com',
        'description':'Disco night at the AO arena! Time to show off some moves!!',
        'event_picture':'AO-arena.jpg',
        'views': 300}]

      first_direct_arena = [
       {'title': 'First Direct Night Out',
        'url': 'https://www.firstdirectarena.com',
        'description':'We have got an action packed month - Snoop Dogg and George Ezra are coming to Leeds!!! ',
        'event_picture':'First_Direct_arena.jpg',
        'views': 1350}]

      the_gorge = [
       {'title': 'Gorge Amphiltheatre',
        'url': 'https://www.livenation.com/venue/KovZpZAEkk1A/gorge-amphitheatre-events',
        'description':'All the way from Washington we bring you the Best american Glastonbury around.',
        'event_picture':'the_gorge.jpg',
        'views': 600}]

      o2_academy = [
       {'title': 'O2 Pop gigs',
        'url': 'https://www.academymusicgroup.com/o2academyglasgow',
        'description':'Fancy some pop country gigs this weekend? Come on over to O2 Academy at Glasgow',
        'event_picture':'O2_Aca.jpg',
        'views': 450}]

      ovo_hydro_arena = [
       {'title': 'Hydro Arenas "all-night long" ',
        'url': 'https://www.thessehydro.com',
        'description':'SEC Hydro are hosting range of hits; Superstar Ed Sheeran and a special guest will be there?!',
        'event_picture':'OVO_Hydro_Arena.jpg',
        'views': 400}]

      pj_live_arena = [
       {'title': 'P&J Mascots Live',
        'url': 'https://www.pandjlive.com',
        'description':'Up in north east of Scotland we have the state of the venue reaching capacities of 15k',
        'event_picture':'liveArena.png',
        'views': 1200}]

      resorts_world_arena = [
       {'title': 'Resorts World Sing Off',
        'url': 'https://www.resortsworldarena.co.uk',
        'description':'LATEST FIGHTS, TOURS & COMEDY HERE!! -- Once its gone.. its gone! ', 'event_picture':'World_Arena.jpg',
        'views': 550}]

      glastonbury= [
       {'title': 'Glastonbury Festival',
        'url': 'https://www.glastonburyfestivals.co.uk/',
        'description':'Name says it all',
        'event_picture':'glastonbury-festival.jpg',
        'views': 4600}]

      cats = {'AO Arena': {'pages': ao_arena, 'views': 400, 'venue_info':'Manchester', 'likes': 200},
             'First Direct Arena': {'pages': first_direct_arena, 'views': 1350, 'venue_info':'Leeds', 'likes': 175},
             'The Gorge': {'pages': the_gorge, 'views': 700, 'venue_info':'Washington', 'likes': 150},
             'O2 Academy': {'pages': o2_academy, 'views': 450, 'venue_info':'Glasgow',  'likes': 225},
             'OVO Hydro Arena': {'pages': ovo_hydro_arena, 'views': 500, 'venue_info':'Glasgow', 'likes': 250},
             'P&J Live Arena': {'pages': pj_live_arena, 'views': 2200, 'venue_info':'Aberdeen',  'likes': 300},
             'Resorts World Arena': {'pages': resorts_world_arena, 'views': 550, 'venue_info':'Birmingham', 'date':'', 'likes': 275},
             'Glastonbury': {'pages': glastonbury, 'views': 6000, 'venue_info':'Glastonbury', 'likes': 3000}
             }
        
      for cat, cat_data in cats.items():
              c = add_cat(cat, views=cat_data['views'], venue_info=cat_data['venue_info'], likes=cat_data['likes'])
              for p in cat_data['pages']:
                  add_page(c, p['title'], p['url'], p['description'], p['event_picture'], views=p['views'] )
                  
      for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, description=True, event_picture=False, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.description=description
    p.event_picture=event_picture
    p.views=views
    p.save()
    return p

def add_cat(name, views=0, venue_info=True, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.venue_info=venue_info
    c.likes=likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting ConcertConnects population script...')
    populate()

