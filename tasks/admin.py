from django.contrib import admin
from import_export import resources
import tasks.models as tasks_models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TaskResource(resources.ModelResource):

    class Meta:
        model = tasks_models.Task


class TaskTagResource(resources.ModelResource):

    class Meta:
        model = tasks_models.TaskTag


@admin.register(tasks_models.Task)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = TaskResource


@admin.register(tasks_models.TaskTag)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = TaskTagResource
