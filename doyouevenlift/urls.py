from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from journal.views import WorkoutList, WorkoutDetail, ExerciseList, ExerciseDetail, SetList, SetDetail, ExerciseSetList, ExerciseSetDetail

urlpatterns = patterns('journal.views',
    url(r'^$', 'api_root'),
    url(r'^workouts/$', WorkoutList.as_view(), name='workout-list'),
    url(r'^workouts/(?P<pk>\d+)/$', WorkoutDetail.as_view(), name='workout-detail'),
    url(r'^exercises/$', ExerciseList.as_view(), name='exercise-list'),
    url(r'^exercises/(?P<pk>\d+)/$', ExerciseDetail.as_view(), name='exercise-detail'),
    url(r'^sets/$', SetList.as_view(), name='set-list'),
    url(r'^sets/(?P<pk>\d+)/$', SetDetail.as_view(), name='set-detail'),
    url(r'^exercisesets/$', ExerciseSetList.as_view(), name='exerciseset-list'),
    url(r'^exercisesets/(?P<pk>\d+)/$', ExerciseSetDetail.as_view(), name='exerciseset-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
