from django.contrib import admin
from .models import Author, Book



"""
Default
"""
# admin.site.register(Author)
# admin.site.register(Book)


""" 
TabularInline
"""
class BookInline(admin.TabularInline):
    model = Book
    extra = 3  # Number of extra forms to display

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)


"""
StackedInline
"""
# class BookInline(admin.StackedInline):
#     model = Book
#     extra = 2  # Number of extra forms to display

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookInline]

# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)


"""
Customizing Inline Admin
"""
# class BookInline(admin.TabularInline):
#     model = Book
#     extra = 2 # Number of extra forms to display
#     fields = ['title', 'publication_date']  # Specify fields to display
#     readonly_fields = ['publication_date']  # Make certain fields read-only

#     def some_custom_method(self, obj):
#         # Custom method to display extra information
#         return obj.title

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookInline]

# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)


""" 
Enhancing Inline Admin with CSS and JavaScript
"""

# class BookInline(admin.TabularInline):
#     model = Book
#     extra = 2 # Number of extra forms to display

#     class Media:
#         css = {
#             'all': ('css/custom_admin.css',)  # Include custom CSS
#         }
#         js = ('js/custom_admin.js',)  # Include custom JavaScript

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [BookInline]
    
# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)

