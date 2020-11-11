from django.contrib import admin
from . models import Todo, Location
from django.utils.safestring import mark_safe

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'place')
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'task_link')
    readonly_fields = ('task_link',)

    def task_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            ("../todo/" + str(obj.task_id)),
            "Task link"
        ))

    task_link.short_description = 'task'

# Register these models as part of the admin panel
admin.site.register(Todo, TodoAdmin)
admin.site.register(Location, LocationAdmin)