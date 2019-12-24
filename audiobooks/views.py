from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Audiobook, Review


class IndexView(ListView):
    context_object_name = 'latest_audiobooks'
    template_name = 'audiobooks/index.html'

    def get_queryset(self):
        return Audiobook.objects.order_by('-release_date')[:5]


# v.1
# def index(request):
#     latest_books = Audiobook.objects.order_by('-release_date')[:5]
#     context = {'latest_audiobooks' : latest_books}
#     return render(request, 'audiobooks/index.html', context)



def detail(request, audiobook_id):
    audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
    context = {
        'audiobook': audiobook,
        'rating_options': Review.RATING_OPTIONS
    }
    return render(request, 'audiobooks/detail.html', context)


# v.1
# def detail(request, audiobook_id):
#     try:
#         audiobook = Audiobook.objects.get(pk=audiobook_id)
#     except Audiobook.DoesNotExist:
#         raise Http404(f"<h4>Could not retrieve audiobook with id {audiobook_id}</h4>")
#
#     return render(request, 'audiobooks/detail.html', {'audiobook': audiobook})



def review(request, audiobook_id):

    audiobook = get_object_or_404(Audiobook, pk=audiobook_id)

    try:
        rating = request.POST['rating']
        comment = request.POST['comment']
    except KeyError as err:
        err_context = {
            'audiobook':audiobook,
            'err_msg': f'ERROR: {str(err)}'
        }
        return render(request, 'audiobooks/detail.html', err_context)

    audiobook.review_set.create(rating=int(rating), comment=comment)
    redicted_to_url = reverse('audiobooks:detail_updated', args=(audiobook_id,))
    return HttpResponseRedirect(redirect_to=redicted_to_url)


class DetailUpdatedView(DetailView):
    model = Audiobook
    template_name = 'audiobooks/detail_updated.html'


# v.1
# def detail_updated(request, audiobook_id):
#     audiobook = get_object_or_404(Audiobook, pk=audiobook_id)
#     sorted_reviews = audiobook.review_set.order_by('-timestamp')
#     context = {
#         'audiobook': audiobook,
#         'sorted_reviews': sorted_reviews
#     }
#     return render(request, 'audiobooks/detail_updated.html', context)
