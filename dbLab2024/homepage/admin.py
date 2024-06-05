from django.contrib import admin
from .models import Student,Mentor,Research,Course,Grade,selectedMaterial,Material,Subject

from import_export.admin import ImportExportModelAdmin
from .resources import CourseResource,StudentResource,MentorResource,ResearchResource,GradeResource,selectedMaterialResource,MaterialResource,SubjectResource


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

@admin.register(Mentor)
class MentorAdmin(ImportExportModelAdmin):
    resource_class = MentorResource

@admin.register(Research)
class ResearchAdmin(ImportExportModelAdmin):
    resource_class = ResearchResource

@admin.register(Grade)
class GradeAdmin(ImportExportModelAdmin):
    resource_class = GradeResource

@admin.register(selectedMaterial)
class selectedMaterialAdmin(ImportExportModelAdmin):
    resource_class = selectedMaterialResource

@admin.register(Material)
class MaterialAdmin(ImportExportModelAdmin):
    resource_class = MaterialResource

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):
    resource_class = SubjectResource

