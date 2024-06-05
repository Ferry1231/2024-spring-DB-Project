# Generated by Django 4.2.13 on 2024-05-30 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Courses",
            fields=[
                (
                    "cous_id",
                    models.CharField(
                        help_text="enter course id",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "cous_summary",
                    models.TextField(help_text="enter summary of the course"),
                ),
                (
                    "cous_name",
                    models.CharField(help_text="enter course name", max_length=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Materials",
            fields=[
                (
                    "matr_id",
                    models.CharField(
                        help_text="inter materials id",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "matr_summary",
                    models.TextField(help_text="enter summary of the material"),
                ),
                (
                    "cous_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.courses",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mentors",
            fields=[
                (
                    "mentor_id",
                    models.CharField(
                        help_text="enter mentor id",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "mentor_name",
                    models.CharField(help_text="enter mentor name", max_length=10),
                ),
                (
                    "mentor_gender",
                    models.CharField(help_text="enter mentor gender", max_length=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Research",
            fields=[
                (
                    "res_name",
                    models.CharField(
                        help_text="enter res name",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "res_summary",
                    models.TextField(help_text="enter summary of the research"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "subject_id",
                    models.CharField(
                        help_text="enter the subject id",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "subject_name",
                    models.CharField(help_text="enter the subject name", max_length=10),
                ),
                (
                    "subject_summary",
                    models.TextField(help_text="enter summary of the subject"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "stu_id",
                    models.CharField(
                        help_text="enter student id",
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "stu_name",
                    models.CharField(help_text="enter student name", max_length=10),
                ),
                (
                    "stu_gender",
                    models.CharField(help_text="enter student gender", max_length=10),
                ),
                ("stu_age", models.IntegerField(help_text="enter student age")),
                (
                    "mentor_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.mentors",
                    ),
                ),
                (
                    "res_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.research",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="research",
            name="res_subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="homepage.subject",
            ),
        ),
        migrations.AddField(
            model_name="mentors",
            name="res_name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="homepage.research",
            ),
        ),
        migrations.AddField(
            model_name="courses",
            name="cous_subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="homepage.subject",
            ),
        ),
        migrations.CreateModel(
            name="selectedMaterials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "matr_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.materials",
                    ),
                ),
                (
                    "stu_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.students",
                    ),
                ),
            ],
            options={
                "unique_together": {("matr_id", "stu_id")},
            },
        ),
        migrations.CreateModel(
            name="Grades",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.FloatField(help_text="enter the score")),
                (
                    "cous_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.courses",
                    ),
                ),
                (
                    "stu_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="homepage.students",
                    ),
                ),
            ],
            options={
                "unique_together": {("cous_id", "stu_id")},
            },
        ),
    ]