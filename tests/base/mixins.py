from django.contrib.auth import get_user_model

from petstagram.pets.models import Pet, Like

UserModel = get_user_model()


class PetTestUtils:
    def create_pet(self, **kwargs):
        return Pet.objects.create(**kwargs)

    def create_pet_with_like(self, like_user, **kwargs):
        pet = self.create_pet(**kwargs)
        Like.objects.create(
            pet=pet,
            user=like_user,
        )
        return pet


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)
