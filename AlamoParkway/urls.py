from django.conf.urls import patterns, url

from AlamoParkway import views
import django.views.generic.list as ListView
urlpatterns = patterns('',
    # URL pattern for the OrdersView
    url(
        regex=r'^$',
        view=views.OrderView.as_view(),
        name='Orders'
    ),
    url(
        regex=r'^special-order/update/(?P<pk>\w+)',
        view=views.SpecialOrderUpdateView.as_view(),
        name='SpecialOrderUpdate'
    ),
    url(
        regex=r'^special-order/create/$',
        view=views.SpecialOrderCreateView.as_view(),
        name='SpecialOrderCreate'
    ),
    url(
        regex=r'^bulk-order/update/(?P<pk>\w+)',
        view=views.BulkOrderUpdateView.as_view(),
        name='BulkOrderUpdate'
    ),
    url(
        regex=r'^bulk-order/create/$',
        view=views.BulkOrderCreateView.as_view(),
        name='BulkOrderCreate'
    ),
    url(
        regex=r'^reports/$',
        view=views.reports.as_view(),
        name='reports'
    ),
    )