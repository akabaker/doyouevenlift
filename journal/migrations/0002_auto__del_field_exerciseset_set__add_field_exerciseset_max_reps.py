# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ExerciseSet.set'
        db.delete_column(u'journal_exerciseset', 'set_id')

        # Adding field 'ExerciseSet.max_reps'
        db.add_column(u'journal_exerciseset', 'max_reps',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['journal.Set']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ExerciseSet.set'
        raise RuntimeError("Cannot reverse this migration. 'ExerciseSet.set' and its values cannot be restored.")
        # Deleting field 'ExerciseSet.max_reps'
        db.delete_column(u'journal_exerciseset', 'max_reps_id')


    models = {
        u'journal.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'exercise_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exercises'", 'to': u"orm['journal.Workout']"})
        },
        u'journal.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['journal.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_reps': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['journal.Set']"}),
            'reps': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'})
        },
        u'journal.set': {
            'Meta': {'object_name': 'Set'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['journal.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_reps': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        u'journal.workout': {
            'Meta': {'object_name': 'Workout'},
            'workout_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        }
    }

    complete_apps = ['journal']