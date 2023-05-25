from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Todo, Contact

@admin.register(Todo)
class TodosAdmin(admin.ModelAdmin):
    list_display = ["title", "is_completed", "created_at", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["is_completed"]
    search_fields = ["title", "content"]
    list_filter = ["is_completed", "created_at", "updated_at"]
    list_per_page = 25
    date_hierarchy = "created_at"
    ordering = ["-created_at", "title"]
    readonly_fields = ["created_at"]
    class Meta:
        model: Todo     
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos") 
  
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["subject", "email", "created_at", "updated_at"]
    list_display_links = ["subject"]
    search_fields = ["subject","message"]
    list_filter = ["created_at"]
    date_hierarchy = "created_at"
    ordering = ["-created_at", "subject"]
    readonly_fields = ["created_at"]

    class Meta:
        model: Contact     
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")   

