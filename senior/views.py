from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, resolve_url
from senior.models import Qna, Review
from senior.forms import QnaForm, ReviewForm
from django.urls import reverse



def main (request: HttpRequest):
    return render(request, "senior/main.html")

def purpose (request: HttpRequest):
    return render(request, "senior/purpose.html")

def definition (request: HttpRequest):
    return render(request, "senior/definition.html")

def rank (request: HttpRequest):
    return render(request, "senior/rank.html")

def ml (request: HttpRequest):
    return render(request, "senior/ml.html")

def index (request: HttpRequest):
    qs = Qna.objects.all()
    return render(request, "senior/qna_list.html", {"qna_list":qs},)
	

def qna_new(request: HttpRequest):
	if request.method == "POST":
		form = QnaForm(request.POST, request.FILES)
		if form.is_valid():
			qna = form.save(commit=False)
			qna.save()
			return redirect(reverse('index'))
	else:
		form = QnaForm()

	return render(request,"senior/qna_form.html",{"form": form,},)

def qna_edit(request: HttpRequest, pk):
	qna = Qna.objects.get(pk=pk)

	if request.method == "POST":
		form = QnaForm(request.POST, request.FILES, instance=qna)
		if form.is_valid():
			form.save()
			#movie = form.save(commit=False)  # 방금 저장한 모델 객체를 반환
			#movie.ip = request.META["REMOTE_ADDR"]
			#movie.save()
			return redirect(f"/senior/qna/{qna.pk}/")
	else:
		form = QnaForm(instance=qna)

	return render(request,"senior/qna_form.html",{"form": form,},)


def qna_detail(request, pk):
    qna = Qna.objects.get(pk=pk)
    review_list = Review.objects.filter(qna_id=pk) #여기서만든 review_list를 qna_detail.html의 review_list에서 불러들이는 것이다.
	#review_list에서 pk를 qna_id에 담아서 qna_id 인 Review를 가져온다.
    return render(request,"senior/qna_detail.html",
	{"qna": qna,"review_list":review_list},
	)
# qna_id 로 저장이 되고 있었다. qna_id(FK=참조키)가 pk(부모키=고유번호)였다.
# qna_id는 고유번호로서 컬럼으로 자동 저장되게 되는 구조이다.


def review_new(request, pk):
    qna = Qna.objects.get(pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review: Review = form.save(commit=False)
            review.qna = qna
            review.save()
            return redirect(f"/senior/qna/{qna.pk}/")
    else:  # GET
        form = ReviewForm()

    return render(request, "senior/review_form.html", {"form": form,})

def review_edit(request, id, pk):
    review = Review.objects.get(pk=id) #id=pk에서 순서를 바꾸니까 되네?? 잉???

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review: Review = form.save()
            #return redirect("movie_detail", movie_pk) # URL Reverse
            return redirect(f"/senior/qna/{pk}/")
    else:  # GET
        form = ReviewForm(instance=review)

    return render(request, "senior/review_form.html", {
        "form": form,
    })

def review_delete(request, id, pk):
	review = Review.objects.get(pk=id) #삭제할 대상
	if request.method =="POST":
		review.delete() # DB에 즉시 Delte 쿼리를 전달
		return redirect(f"/senior/qna/{pk}/")
			
	return render(request,"senior/review_confirm_delete.html",{
		"review":review,
		},)
