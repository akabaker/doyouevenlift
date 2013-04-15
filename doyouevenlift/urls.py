from django.conf.urls import patterns, include, url
import journal.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', journal.views.ListWorkoutView.as_view(),
        name='workouts-list'),
    url(r'^new$', journal.views.CreateWorkoutView.as_view(),
        name='workouts-new'),
    url(r'^edit/(?P<pk>\d+)/$', journal.views.UpdateWorkoutView.as_view(),
        name='workouts-edit'),
    url(r'^delete/(?P<pk>\d+)/$', journal.views.DeleteWorkoutView.as_view(),
        name='workouts-delete'),
    url(r'^(?P<pk>\d+)/$', journal.views.WorkoutView.as_view(),
        name='workouts-view'),
    # Examples:
    # url(r'^$', 'doyouevenlift.views.home', name='home'),
    # url(r'^doyouevenlift/', include('doyouevenlift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
