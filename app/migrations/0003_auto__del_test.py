# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Test'
        db.delete_table(u'app_test')


    def backwards(self, orm):
        # Adding model 'Test'
        db.create_table(u'app_test', (
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'app', ['Test'])


    models = {
        
    }

    complete_apps = ['app']