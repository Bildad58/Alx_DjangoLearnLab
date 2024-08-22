
from django.contrib import admin
# from .models import Book
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Student



# admin.site.register(Book)

# # form class admin 
# class BookAdmin(admin.ModelAdmin):
# # create list display
#     list_display = ('title', 'author', 'publication_year')

# #create list filter 
#     list_filter = ('author', 'publication_year')
# # create search field 
#     search_fields = ('title', 'author')

# # register  Book and Bookadmo
# admin.site.register(Book, BookAdmin)

# # Register your models here.
# # Register your models here.

from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import CustomUser


class UserAdmin(CustomUserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Permission)

editors_group, created = Group.objects.get_or_create(name='Editors') 
viewers_group, created = Group.objects.get_or_create(name='Viewers') 
admin_group, created = Group.objects.get_or_create(name='Admins') 


content_type = ContentType.objects.get_for_model(Student)
post_permission = Permission.objects.filter(content_type=content_type)
print([perm.codename for perm in post_permission])

for perm in post_permission:
    if perm.codename == "Can_delete" and "Can_edit" and "Can_create" and "Can_view":
     admin_group.permissions.add(perm)

    if perm.codename ==  "Can_edit" and "Can_create" and "Can_view":
     editors_group.permissions.add(perm)


    elif perm.codename == "can_view":
        viewers_group.permissions.add(perm)


