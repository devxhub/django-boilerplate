from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

User = get_user_model()

class UserFactory(DjangoModelFactory[User]):
    {%- if dxh_py.username_type == "username" %}
    username = Faker("user_name")
    {%- endif %}
    email = Faker("email")
    name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):  # noqa: FBT001
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """Save again the instance if creating and at least one hook ran."""
        if create and results and not cls._meta.skip_postgeneration_save:
            # Some post-generation hooks ran, and may have modified us.
            instance.save()

    class Meta:
        model = User
        django_get_or_create = ["{{dxh_py.username_type}}"]