from django.urls import path

from audiobooks import views

app_name = 'audiobooks'

urlpatterns = [
    # audiobooks/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # audiobooks/5/
    path('<int:audiobook_id>/', views.detail, name='detail'),

    # audiobooks/5/review/
    path('<int:audiobook_id>/review/', views.review, name='review'),

    # audiobooks/5/updated/
    # path('<int:audiobook_id>/updated/', views.detail_updated, name='detail_updated')
    path('<int:pk>/updated/', views.DetailUpdatedView.as_view(), name='detail_updated')

]