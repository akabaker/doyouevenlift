from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Workout

class ListWorkoutView(ListView):
    
    model = Workout
    template_name = 'workout_list.html'

class CreateWorkoutView(CreateView):

    model = Workout
    template_name = 'edit_workout.html'

    def get_success_url(self):
        return reverse('workouts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateWorkoutView, self).get_context_data(**kwargs)
        context['action'] = reverse('workouts-new')

        return context

class UpdateWorkoutView(UpdateView):
    
    model = Workout
    template_name = 'edit_workout.html'

    def get_success_url(self):
        return reverse('workouts-list')

    def get_context_data(self, **kwargs):
        
        context = super(UpdateWorkoutView, self).get_context_data(**kwargs)
        context['action'] = reverse('workouts-edit',
                                    kwargs={'pk': self.get_object().id})

        return context

class DeleteWorkoutView(DeleteView):
    
    model = Workout
    template_name = 'delete_workout.html'

    def get_success_url(self):
        return reverse('workouts-list')

class WorkoutView(DetailView):
    
    model = Workout
    template_name = 'workout.html'

# Workouts
class ListWorkoutView(ListView):
    model = Workout
    template_name = 'workout_list.html'

    """
    def get_context_data(self, **kwargs):

        context = super(ListWorkoutView, self).get_context_data(**kwargs)
        # Uses the named group pk to get the primary key of Workout
        context['exercises'] = self.get_object().exercise_set.all()
        return context
    """
