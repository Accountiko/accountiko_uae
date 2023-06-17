from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class HomeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class CoverAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class WhyChooseAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class TestimonialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class AboutUsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class WorkHistoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass
class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    pass

admin.site.register(HomePage,HomeAdmin)
admin.site.register(Cover,CoverAdmin)
admin.site.register(WhyChoose,WhyChooseAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(WorkHistory,WorkHistoryAdmin)
admin.site.register(Client,ClientAdmin)
admin.site.register(Contact,ContactAdmin)
