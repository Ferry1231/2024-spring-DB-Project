from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    stu_id = models.CharField(max_length=20,help_text="enter student id",primary_key=True)
    stu_name = models.CharField(max_length=10,help_text="enter student name")
    stu_gender = models.CharField(max_length=10,help_text="enter student gender")
    stu_age = models.IntegerField(help_text="enter student age")
    mentor_id = models.ForeignKey('Mentor',to_field='mentor_id',on_delete=models.RESTRICT,null=True)
    res_name = models.ForeignKey('Research',to_field='res_name',on_delete=models.RESTRICT,null=True)
    
    def __str__(self):
        return self.stu_name
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.stu_id)])
    
class Mentor(models.Model):
    mentor_id = models.CharField(max_length=20,help_text="enter mentor id",primary_key=True)
    mentor_name = models.CharField(max_length=10,help_text="enter mentor name")
    mentor_gender = models.CharField(max_length=10,help_text="enter mentor gender")
    res_name = models.ForeignKey('Research',to_field='res_name',on_delete=models.RESTRICT,null=True)

    def __str__(self):
        return self.mentor_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.mentor_id)])
    
class Research(models.Model):
    res_name = models.CharField(max_length=30,help_text="enter res name",primary_key=True)
    res_summary = models.TextField(help_text="enter summary of the research")
    res_subject = models.ForeignKey('Subject',to_field='subject_id',on_delete=models.RESTRICT,null=True)

    def __str__(self):
        return self.res_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.res_name)])

class Course(models.Model):
    cous_subject = models.ForeignKey('Subject',to_field='subject_id',on_delete=models.RESTRICT,null=True)
    cous_id = models.CharField(max_length=20,help_text="enter course id",primary_key=True)
    cous_summary = models.TextField(help_text="enter summary of the course")
    cous_name = models.CharField(max_length=30,help_text="enter course name")

    def __str__(self):
        return self.cous_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.cous_id)])
    
class Grade(models.Model):
    cous_id = models.ForeignKey('Course',to_field='cous_id',on_delete=models.RESTRICT,null=True)
    stu_id = models.ForeignKey('Student',to_field='stu_id',on_delete=models.RESTRICT,null=True)
    score = models.FloatField(help_text="enter the score")

    class Meta:
        unique_together = (('cous_id', 'stu_id',),)

    def __str__(self):
        return f"{self.cous_id.cous_name} - {self.stu_id.stu_name}: {self.score}"

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.cous_id + " " + str(self.score))])
    
class selectedMaterial(models.Model):
    matr_id = models.ForeignKey('Material',to_field='matr_id',on_delete=models.RESTRICT,null=True)
    stu_id = models.ForeignKey('Student',to_field='stu_id',on_delete=models.RESTRICT,null=True)
    
    class Meta:
        unique_together = (('matr_id', 'stu_id',),)

    def __str__(self):
        return self.matr_id + " " + self.stu_id

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.matr_id+self.stu_id)])
    
class Material(models.Model):
    matr_id =  models.CharField(max_length=30,help_text="inter materials id",primary_key=True)
    matr_name = models.CharField(max_length=20,help_text="inter materials id")
    matr_summary = models.TextField(help_text="enter summary of the material")
    cous_id = models.ForeignKey('Course',to_field='cous_id',on_delete=models.RESTRICT,null=True)

    def __str__(self):
        return self.matr_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.matr_name)])
    
class Subject(models.Model):
    subject_id = models.CharField(max_length=20,help_text="enter the subject id",primary_key=True)
    subject_name = models.CharField(max_length=10,help_text="enter the subject name")
    subject_summary = models.TextField(help_text="enter summary of the subject")
    
    def __str__(self):
            return self.subject_name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.subject_id)])