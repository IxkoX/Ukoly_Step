from django.urls import path
from myapp import views

# 127.0.0.1:8000/
# 127.0.0.1:8000/admin/

urlpatterns = [
    path('', views.index_page),
    # path('time/', ), # zde přidejte time_page

    # http://127.0.0.1:8000/url-paths/
    path('url-paths/', views.url_paths),

    path('my-path/', views.my_math),

    path('test-template/', views.test_template),

    path('calculator/', views.calculator),

    # path('jmeno/jana/', views.my_page),
    # path('jmeno/petr/', views.my_page),
    # path('jmeno/karel/', views.my_page),
    
    # jmeno/ales/
    # instagram.com/suche.cz/
    # instagram.com/uzivatel/
    # zpravy.cz/clanky/top-mista-na-bydleni-109282/
    # zpravy.cz/clanky/top-mista-na-sport-28273/
    # slug 'Top místa na bydlení' -> 'top-mista-na-bydleni'

    # toto udělá validaci pro /clanky/<slug>-<id>/
    # máme vzor
    # zpravy.cz/clanky/top-mista-na-bydleni-109282/

    # toto udělá validaci pouze pro /clanky/
    # zpravy.cz/clanky/?id=109282
    
    path('jmeno/<str:name>/', views.my_page),
    # todo: ukazat url cesty pomocí regex

    # clanky jak-nazbrat-houb110009
    path('clanky/<slug:name>-<int:number>/', views.article ),

    path('pages/<int:number>/<slug:name>', views.pages),

    path('login/', views.login),
    
    path('time/', views.time_page),

    path('age/', views.age_page),

    path('signup/', views.signup_page, name="signup"),

    
]

