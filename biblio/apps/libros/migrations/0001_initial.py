# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Libro'
        db.create_table(u'libros_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('resumen', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('portada', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'libros', ['Libro'])

        # Adding M2M table for field autor on 'Libro'
        m2m_table_name = db.shorten_name(u'libros_libro_autor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('libro', models.ForeignKey(orm[u'libros.libro'], null=False)),
            ('autor', models.ForeignKey(orm[u'autores.autor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['libro_id', 'autor_id'])


    def backwards(self, orm):
        # Deleting model 'Libro'
        db.delete_table(u'libros_libro')

        # Removing M2M table for field autor on 'Libro'
        db.delete_table(db.shorten_name(u'libros_libro_autor'))


    models = {
        u'autores.autor': {
            'Meta': {'object_name': 'Autor'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'libros.libro': {
            'Meta': {'object_name': 'Libro'},
            'autor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['autores.Autor']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'portada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'resumen': ('django.db.models.fields.TextField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['libros']