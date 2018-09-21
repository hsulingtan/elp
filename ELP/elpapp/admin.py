from django.contrib import admin
from elpapp.models import AccessRecord, Employer, jobs, Student, EUserProfileInfo, SUserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Employer)
admin.site.register(jobs)
admin.site.register(Student)
admin.site.register(EUserProfileInfo)
admin.site.register(SUserProfileInfo)
