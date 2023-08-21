from django.urls import path
from .views import note_view, note_detail_view

urlpatterns = [
    path('', note_view, name='note'),
    path('/<int:note_id>', note_detail_view, name='note_detail')
]
