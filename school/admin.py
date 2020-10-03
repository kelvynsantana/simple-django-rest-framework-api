from django.contrib import admin
from school.models import Student

# Register your models here.


class Students(admin.ModelAdmin):
  list_display = ('id', 'name', 'document', 'email')
  list_display_links = ('name', 'email')
  search_fields = ('name',)


admin.site.register(Student, Students)