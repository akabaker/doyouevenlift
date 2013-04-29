from .models import Workout, Exercise, Set, ExerciseSet
from rest_framework import serializers

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.RelatedField(many=True)

    class Meta:
        model = Workout
        fields = ('name','exercises')

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = ('name', 'workout')

class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = ('exercise', 'max_reps')

class ExerciseSet(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = ('exercise', 'reps', 'weight', 'date')
