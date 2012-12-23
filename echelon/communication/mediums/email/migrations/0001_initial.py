# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailMedium'
        db.create_table('email_emailmedium', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('from_address', self.gf('django.db.models.fields.EmailField')(default='notifier@lateral-thoughts.com', max_length=75)),
            ('to_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject_prefix', self.gf('django.db.models.fields.CharField')(default='[Prefix]', max_length=50)),
        ))
        db.send_create_signal('email', ['EmailMedium'])


    def backwards(self, orm):
        # Deleting model 'EmailMedium'
        db.delete_table('email_emailmedium')


    models = {
        'email.emailmedium': {
            'Meta': {'object_name': 'EmailMedium'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'default': "'notifier@lateral-thoughts.com'", 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'subject_prefix': ('django.db.models.fields.CharField', [], {'default': "'[Prefix]'", 'max_length': '50'}),
            'to_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['email']