from django.test import TestCase
from .models import Workout
    
class JournalTests(TestCase):
    """Journal model tests"""

    def test_str(self):

        workout = Workout(name='Power')

        self.assertEquals(
            str(workout), 
            'Power'
        )
