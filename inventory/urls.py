from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [

    url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^new_inventory/$', views.add_inventory, name='new_inventory'),

    url(r'^(?P<item_id>[0-9]+)/listview/$', views.list_view, name='listview'),
    url(r'^(?P<item_id>[0-9]+)/new_item/$', views.add_item, name='new_item'),

    url(r'^(?P<item_pk>[0-9]+)/del_item/$', views.delete_item, name='del_item'),
    url(r'^(?P<item_pk>[0-9]+)/ed_item/$', views.edit_item, name='edit_item'),
    url(r'^(?P<item_pk>[0-9]+)/ed_save/$', views.edit_save, name='edit_save')
]
