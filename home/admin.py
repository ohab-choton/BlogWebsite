from django.contrib import admin
from .models import Category, Blogs,Comments

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')
    ordering = (('-updated_at', 'id'))

class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','slug','author','category','status','is_featured','created_at','updated_at')
    prepopulated_fields={'slug':('title',)}
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable=('is_featured',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comments)


