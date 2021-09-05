from django.contrib import admin

from senior.models import Qna, Review

@admin.register(Qna)
class QnaAdmin(admin.ModelAdmin):
    list_display = ["title", "picture", "writer","desc"]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass