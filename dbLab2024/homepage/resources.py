# myapp/resources.py
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
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
    subject = fields.Field(
        column_name='cous_subject',  # 你的CSV文件中对应的列名
        attribute='cous_subject',
        widget=ForeignKeyWidget(Subject, 'subject_id')  
    )
    class Meta:
        model = Course
        import_id_fields = ('cous_id',)

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
        import_id_fields = ('subject_id',)
