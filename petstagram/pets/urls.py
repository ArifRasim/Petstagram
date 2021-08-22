from django.urls import path

from petstagram.pets.views import PetDetailsView, CommentPetView, ListPetsView, \
    CreatePetView, EditPetView, DeletePetView, LikePetView

urlpatterns = [
    path('', ListPetsView.as_view(), name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', LikePetView.as_view(), name='like pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]
