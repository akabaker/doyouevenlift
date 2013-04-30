from .models import Workout, Exercise, Set, ExerciseSet
from rest_framework import serializers

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = serializers.RelatedField(many=True)

    class Meta:
        model = Workout
        fields = ('workout_name','exercises')

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ('exercise_name', 'workout')

class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = ('exercise', 'max_reps')

class ExerciseSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseSet
        fields = ('exercise', 'reps', 'weight', 'date', 'set')
