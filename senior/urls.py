from django.urls import path
from senior import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path("purpose/", views.purpose, name="purpose"),
    path("definition/", views.definition, name="definition"),
    path("rank/", views.rank, name="rank"),
    path("ml/", views.ml, name="ml"),
    path("qna/", views.index, name="index"),
    path("qna/<int:pk>/", views.qna_detail, name="qna_detail"),
    path("qna/new/", views.qna_new, name="qna_new"),
    path("qna/<int:pk>/edit/", views.qna_edit, name="qna_edit"),
    path("qna/<int:pk>/reviews/new/", views.review_new, name="review_new"),
    path("qna/<int:pk>/reviews/<int:id>/edit/", views.review_edit, name="review_edit"),
    path("qna/<int:pk>/reviews/<int:id>/delete/", views.review_delete, name="review_delete"),
    ]
