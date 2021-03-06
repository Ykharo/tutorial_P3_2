#encoding:utf-8
from django.contrib import admin
from django.conf.locale.es import formats as es_formats
import datetime

# Register your models here.
#from __future__ import unicode_literals

#from import_export.resources import ModelResource
#from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

#from .models import Book, Category, Author


#class BookResource(ModelResource):

#    class Meta:
#        model = Book

#    def for_delete(self, row, instance):
#        return self.fields['name'].clean(row) == ''


#class BookAdmin(ImportExportMixin, admin.ModelAdmin):
#    list_filter = ['categories', 'author']
#    resource_class = BookResource


#class CategoryAdmin(ExportActionModelAdmin):
#    pass


#class AuthorAdmin(ImportMixin, admin.ModelAdmin):
#    pass

#admin.site.register(Book, BookAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Author, AuthorAdmin)


#---------------------------------------

USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = ','

from .models import Question, Choice, Area, Ceco, Mdte, Ctta, Ctto, Edp, Odc, Monedas

class EdpInline(admin.StackedInline): #TabularInline
    model = Edp
    extra = 1
    list_editable = ('NumEDP', 'ValEDP_sep')

    def ValEDP_sep(self, instance):
        return '{0:,}'.format(self.ValEDP)


class OdcInline(admin.StackedInline):
    model = Odc
    extra = 1


class CttoAdmin(admin.ModelAdmin):
    list_display = ('NumCtto','DescCtto','EstCtto','FechTerCtto','IdCecoCtto','IdCtta','ObservCtto')
    list_editable = ('EstCtto','FechTerCtto','ObservCtto')
    list_per_page = 20
    list_filter = ('TipoServ', )
    inlines = [EdpInline,OdcInline]
    def formatted_amount(self, obj):
        # obj is the Model instance

        # If your locale is properly set, try also:
        # locale.currency(obj.amount, grouping=True)
        return '%.2f EUR' % obj.amount

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date','slug','fecha_creacion', 'status')
    fields = ('question_text', 'pub_date','slug','status')
#    fieldsets = [
#        (None, { 'fields': [('question_text','slug')] } ),
#    ]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            obj.fecha_creacion = datetime.datetime.now()
        obj.modificado_por = request.user
        obj.fecha_ultima_modificacion = datetime.datetime.now()
        obj.save()



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Area)
admin.site.register(Ceco)
admin.site.register(Mdte)
admin.site.register(Ctta)
admin.site.register(Ctto, CttoAdmin)
admin.site.register(Edp)
admin.site.register(Odc)
admin.site.register(Monedas)
