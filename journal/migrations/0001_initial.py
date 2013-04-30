# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workout'
        db.create_table(u'journal_workout', (
            ('workout_name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal(u'journal', ['Workout'])

        # Adding model 'Exercise'
        db.create_table(u'journal_exercise', (
            ('exercise_name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exercises', to=orm['journal.Workout'])),
        ))
        db.send_create_signal(u'journal', ['Exercise'])

        # Adding model 'Set'
        db.create_table(u'journal_set', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['journal.Exercise'])),
            ('max_reps', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal(u'journal', ['Set'])

        # Adding model 'ExerciseSet'
        db.create_table(u'journal_exerciseset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(related_name='exercisesets', to=orm['journal.Exercise'])),
            ('set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sets', to=orm['journal.Set'])),
            ('reps', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'journal', ['ExerciseSet'])


    def backwards(self, orm):
        # Deleting model 'Workout'
        db.delete_table(u'journal_workout')

        # Deleting model 'Exercise'
        db.delete_table(u'journal_exercise')

        # Deleting model 'Set'
        db.delete_table(u'journal_set')

        # Deleting model 'ExerciseSet'
        db.delete_table(u'journal_exerciseset')


    models = {
        u'journal.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'exercise_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exercises'", 'to': u"orm['journal.Workout']"})
        },
        u'journal.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'exercisesets'", 'to': u"orm['journal.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reps': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sets'", 'to': u"orm['journal.Set']"}),
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