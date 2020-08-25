# Generated by Django 3.1 on 2020-08-21 18:59

import datetime

import django.db.models.deletion

from django.conf import settings
from django.db import migrations
from django.db import models

import codex.models


def init_admin_flags(apps, schema_editor):
    """Initalize the admin flag rows"""
    # AdminFlag = apps.get_model("codex", "AdminFlag")  # noqa N806
    for name in codex.models.AdminFlag.FLAG_NAMES:
        codex.models.AdminFlag.objects.update_or_create(name=name)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sessions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="Imprint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_default", models.BooleanField(default=False)),
                ("sort_name", models.CharField(max_length=32)),
                ("name", models.CharField(default="Main Imprint", max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Library",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "path",
                    models.CharField(
                        db_index=True,
                        max_length=128,
                        unique=True,
                        validators=[codex.models.validate_dir_exists],
                    ),
                ),
                ("enable_watch", models.BooleanField(db_index=True, default=True)),
                ("enable_scan_cron", models.BooleanField(db_index=True, default=True)),
                (
                    "scan_frequency",
                    models.DurationField(default=datetime.timedelta(seconds=43200)),
                ),
                ("last_scan", models.DateTimeField(null=True)),
                ("scan_in_progress", models.BooleanField(default=False)),
                ("schema_version", models.PositiveSmallIntegerField(default=0)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_default", models.BooleanField(default=False)),
                ("sort_name", models.CharField(db_index=True, max_length=32)),
                ("name", models.CharField(default="No Publisher", max_length=32)),
            ],
            options={"unique_together": {("name", "is_default")},},
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_default", models.BooleanField(default=False)),
                ("sort_name", models.CharField(db_index=True, max_length=32)),
                ("name", models.CharField(default="Default Series", max_length=32)),
                ("volume_count", models.PositiveSmallIntegerField(null=True)),
                (
                    "imprint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.imprint"
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=codex.models.Publisher.get_default_publisher,
                        to="codex.publisher",
                    ),
                ),
            ],
            options={"unique_together": {("name", "imprint", "is_default")},},
        ),
        migrations.CreateModel(
            name="Volume",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_default", models.BooleanField(default=False)),
                ("sort_name", models.CharField(db_index=True, max_length=32)),
                ("name", models.CharField(default="", max_length=32)),
                (
                    "issue_count",
                    models.DecimalField(decimal_places=2, max_digits=6, null=True),
                ),
                (
                    "imprint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.imprint"
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=codex.models.Publisher.get_default_publisher,
                        to="codex.publisher",
                    ),
                ),
                (
                    "series",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.series"
                    ),
                ),
            ],
            options={"unique_together": {("name", "series", "is_default")},},
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="StoryArc",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="SeriesGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.AddField(
            model_name="imprint",
            name="publisher",
            field=models.ForeignKey(
                on_delete=models.SET(codex.models.Publisher.get_default_publisher),
                to="codex.publisher",
            ),
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="Folder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
                (
                    "path",
                    models.CharField(
                        db_index=True,
                        max_length=128,
                        validators=[codex.models.validate_dir_exists],
                    ),
                ),
                ("sort_name", models.CharField(max_length=32)),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.library"
                    ),
                ),
                (
                    "parent_folder",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="codex.folder",
                    ),
                ),
            ],
            options={"unique_together": {("library", "path")},},
        ),
        migrations.CreateModel(
            name="CreditRole",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="CreditPerson",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.CreateModel(
            name="Credit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="codex.creditperson",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="codex.creditrole",
                    ),
                ),
            ],
            options={"unique_together": {("person", "role")},},
        ),
        migrations.CreateModel(
            name="Comic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("path", models.CharField(db_index=True, max_length=128)),
                (
                    "issue",
                    models.DecimalField(
                        db_index=True, decimal_places=2, default=0.0, max_digits=6
                    ),
                ),
                ("title", models.CharField(db_index=True, max_length=64, null=True)),
                ("year", models.PositiveSmallIntegerField(null=True)),
                ("month", models.PositiveSmallIntegerField(null=True)),
                ("day", models.PositiveSmallIntegerField(null=True)),
                ("summary", models.TextField(null=True)),
                ("notes", models.TextField(null=True)),
                ("description", models.TextField(null=True)),
                (
                    "critical_rating",
                    models.CharField(db_index=True, max_length=32, null=True),
                ),
                (
                    "maturity_rating",
                    models.CharField(db_index=True, max_length=32, null=True),
                ),
                (
                    "user_rating",
                    models.CharField(db_index=True, max_length=32, null=True),
                ),
                ("country", models.CharField(db_index=True, max_length=32, null=True)),
                ("language", models.CharField(db_index=True, max_length=16, null=True)),
                (
                    "page_count",
                    models.PositiveSmallIntegerField(db_index=True, default=0),
                ),
                ("cover_image", models.CharField(max_length=64, null=True)),
                ("read_ltr", models.BooleanField(default=True)),
                ("web", models.URLField(null=True)),
                ("format", models.CharField(max_length=16, null=True)),
                ("scan_info", models.CharField(max_length=32, null=True)),
                ("sort_name", models.CharField(db_index=True, max_length=32)),
                ("date", models.DateField(db_index=True, null=True)),
                ("decade", models.PositiveSmallIntegerField(db_index=True, null=True)),
                ("size", models.PositiveSmallIntegerField(db_index=True)),
                ("max_page", models.PositiveSmallIntegerField(default=0)),
                ("cover_path", models.CharField(max_length=32)),
                ("characters", models.ManyToManyField(to="codex.Character")),
                ("credits", models.ManyToManyField(to="codex.Credit")),
                ("folder", models.ManyToManyField(to="codex.Folder")),
                ("genres", models.ManyToManyField(to="codex.Genre")),
                (
                    "imprint",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.imprint"
                    ),
                ),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.library"
                    ),
                ),
                ("locations", models.ManyToManyField(to="codex.Location")),
                (
                    "myself",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comic",
                        to="codex.comic",
                    ),
                ),
                (
                    "parent_folder",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comic_in",
                        to="codex.folder",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="codex.publisher",
                    ),
                ),
                (
                    "series",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.series"
                    ),
                ),
                ("series_groups", models.ManyToManyField(to="codex.SeriesGroup")),
                ("story_arcs", models.ManyToManyField(to="codex.StoryArc")),
                ("tags", models.ManyToManyField(to="codex.Tag")),
                ("teams", models.ManyToManyField(to="codex.Team")),
                (
                    "volume",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.volume"
                    ),
                ),
            ],
            options={"unique_together": {("path", "volume", "year", "issue")},},
        ),
        migrations.AlterUniqueTogether(
            name="imprint", unique_together={("name", "publisher", "is_default")},
        ),
        migrations.CreateModel(
            name="AdminFlag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(db_index=True, max_length=32)),
                ("on", models.BooleanField(default=True)),
            ],
            options={"abstract": False, "unique_together": {("name",)},},
        ),
        migrations.AlterField(
            model_name="imprint",
            name="sort_name",
            field=models.CharField(db_index=True, max_length=32),
        ),
        migrations.CreateModel(
            name="UserBookmark",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bookmark",
                    models.PositiveSmallIntegerField(db_index=True, null=True),
                ),
                ("finished", models.BooleanField(db_index=True, default=False)),
                (
                    "fit_to",
                    models.CharField(
                        default=None,
                        max_length=6,
                        null=True,
                        validators=[codex.models.validate_fit_to_choice],
                    ),
                ),
                ("two_pages", models.BooleanField(default=None, null=True)),
                (
                    "comic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="codex.comic"
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        null=True,
                        on_delete=codex.models.cascade_if_user_null,
                        to="sessions.session",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("user", "session", "comic")},},
        ),
        migrations.RunPython(code=init_admin_flags,),
    ]