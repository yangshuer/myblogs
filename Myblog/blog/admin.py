from django.contrib import admin
from blog.models import Article,BlockInfo,TextInfo,Images
# Register your models here.
# 一对多编辑
class TextToImage(admin.StackedInline):
    model = Images
    extra = 5

class BlockAdmin(admin.ModelAdmin):
    list_display = ['Block_in']

class TextAdmin(admin.ModelAdmin):
    inlines = [TextToImage,]
    list_display = ['id','title','author','Block','image','introduce','text','date']

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id','image','Text']

admin.site.register(BlockInfo,BlockAdmin)
admin.site.register(TextInfo,TextAdmin)
admin.site.register(Images,ImagesAdmin)