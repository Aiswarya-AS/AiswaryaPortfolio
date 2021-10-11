from django.contrib import admin
from .models import Education, Experience, Skill, PortfolioDetail
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display= ("skill_name","value",)
    

admin.site.register(Skill,SkillAdmin)

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(PortfolioDetail)