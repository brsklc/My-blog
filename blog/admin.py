from django.contrib import admin
from blog.models import Post, About, Comment, Tag

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Tag)