import pathlib
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import PageHits

# Create your views here.


__dir__ = pathlib.Path(__file__).resolve().parent


def home(request, *args, **kwargs):

    # html_file_path = __dir__ / "home.html"
    # html_file_content = html_file_path.read_text(encoding="utf-8")

    page_hit = PageHits.objects.filter(page=request.path).first()
    if page_hit:
        PageHits.objects.filter(id=page_hit.id).update(hits=page_hit.hits + 1)
        # page_hit.update(hits=page_hit.hits + 1)
    else:
        PageHits.objects.create(page=request.path)
    print(page_hit)

    ctx = {
        "page_hit": page_hit,
    }
    return render(request, "home.html", ctx)


def bio(request, *args, **kwargs):

    page_hit = PageHits.objects.filter(page=request.path).first()

    if page_hit:
        PageHits.objects.filter(page=request.path).update(hits=page_hit.hits + 1)
    else:
        PageHits.objects.create(page=request.path, hits=1)
    print(page_hit)

    ctx = {
        "page_hit": page_hit,
    }
    return render(request, "home.html", ctx)
