from django.contrib import admin
from .models import *
from django.conf import settings
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.site_header = 'Accountkio Dashboard'



class PageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','category','is_featured','is_usefull')
    search_fields = ['title',]

class CatAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class DefinitionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class HowToRegisterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class DocumentsRequiredAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class EligibilityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class FAQAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class SplitFaceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class CardsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

admin.site.register(Pages,PageAdmin)
admin.site.register(Definition,DefinitionAdmin)
admin.site.register(HowToRegister,HowToRegisterAdmin)
admin.site.register(DocumentsRequired,DocumentsRequiredAdmin)
admin.site.register(Eligibility,EligibilityAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(SplitFace,SplitFaceAdmin)
admin.site.register(Cards,CardsAdmin)
admin.site.register(Category,CatAdmin)