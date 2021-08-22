from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.core.views import PostOnlyView, BootStrapFormViewMixin
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


class ListPetsView(ListView):
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'
    model = Pet


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']

        pet.likes_count = pet.like_set.count()
        is_owner = pet.user == self.request.user

        is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id) \
            .exists()
        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context


class CommentPetView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
            user=self.request.user,
        )
        comment.save()

        return redirect('pet details', pet.id)

    def form_invalid(self, form):
        pass


class LikePetView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = pet.like_set.filter(user_id=self.request.user.id) \
            .first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                pet=pet,
                user=self.request.user,
            )
            like.save()
        return redirect('pet details', pet.id)


class CreatePetView(LoginRequiredMixin, BootStrapFormViewMixin, CreateView):
    model = Pet
    fields = ('name', 'description', 'image', 'age', 'type')
    success_url = reverse_lazy('list pets')
    template_name = 'pets/pet_create.html'

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


class EditPetView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pets/pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('list pets')


class DeletePetView(LoginRequiredMixin, DeleteView):
    template_name = 'pets/pet_delete.html'
    model = Pet
    success_url = reverse_lazy('list pets')
