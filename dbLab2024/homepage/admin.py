from django.contrib import admin
from .models import Students,Mentors,Research,Courses,Grades,selectedMaterials,Materials,Subject

admin.site.register(Students)
admin.site.register(Mentors)
admin.site.register(Research)
admin.site.register(Courses)
admin.site.register(Grades)
admin.site.register(selectedMaterials)
admin.site.register(Materials)
admin.site.register(Subject)
