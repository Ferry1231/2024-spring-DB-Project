# myapp/resources.py
from import_export import resources
from .models import Student,Mentor,Research,Course,Grade,selectedMaterial,Material,Subject

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class MentorResource(resources.ModelResource):
    class Meta:
        model = Mentor

class ResearchResource(resources.ModelResource):
    class Meta:
        model = Research

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course

class GradeResource(resources.ModelResource):
    class Meta:
        model = Grade

class selectedMaterialResource(resources.ModelResource):
    class Meta:
        model = selectedMaterial

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material

class SubjectResource(resources.ModelResource):
    class Meta:
        model = Subject
