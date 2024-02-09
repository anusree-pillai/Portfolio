
from django.contrib import admin
from .models import Media,Portfolio,Skill,Education,Workexperience,UserProfile,ContactProfile,Certificate

# Register your models here.
'''admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Workexperience)
#admin.site.register(about)
admin.site.register(UserProfile)
admin.site.register(ContactProfile)
admin.site.register(Certificate)
admin.site.register(Media)'''



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')
     

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
     list_display = ('id' , 'degree', 'institution', 'graduation_year')

@admin.register(Workexperience)
class WorkAdmin(admin.ModelAdmin):
     list_display = ('id', 'job_title', 'company','start_date', 'end_date','description')     

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')
# Register your models here.
