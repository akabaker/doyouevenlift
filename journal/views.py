from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from journal.serializers import *
from .models import Exercise, Set, ExerciseSet, Workout

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'workouts': reverse('workout-list', request=request),
        'exercises': reverse('exercise-list', request=request),
        'sets': reverse('set-list', request=request),
        'exercisesets': reverse('exerciseset-list', request=request),
    })

class WorkoutList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Workout
    serializer_class = WorkoutSerializer

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Workout
    serializer_class = WorkoutSerializer

class ExerciseList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Exercise
    serializer_class = ExerciseSerializer

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Exercise
    serializer_class = ExerciseSerializer

class SetList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Set
    serializer_class = SetSerializer

class SetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Set
    serializer_class = SetSerializer

class ExerciseSetList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = ExerciseSet
    serializer_class = ExerciseSetSerializer

class ExerciseSetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = ExerciseSet
    serializer_class = ExerciseSetSerializer
