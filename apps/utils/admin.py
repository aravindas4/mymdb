from django.contrib import admin


class DynamicColumnAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(DynamicColumnAdmin, self).__init__(*args, **kwargs)
        field_list = [i.name for i in self.model._meta.fields]
        all_fields = [i.name for i in self.model._meta.fields
                      if not hasattr(i, 'remote_field') and 'invalid_date'
                      not in i.error_messages]
        self.search_fields = all_fields
        self.list_display = field_list
        self.list_display_links = field_list

