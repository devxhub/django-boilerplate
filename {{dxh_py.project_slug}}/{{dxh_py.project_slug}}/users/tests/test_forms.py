"""
Module for all Form Tests.
"""
from django.utils.translation import gettext_lazy as _

from {{ dxh_py.project_slug }}.users.forms import UserAdminCreationForm
from {{ dxh_py.project_slug }}.users.models import User


class TestUserAdminCreationForm:
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def test_username_validation_error_msg(self, user: User):
        """
        Tests UserAdminCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserAdminCreationForm(
            {
                {%- if dxh_py.username_type == "email" %}
                "email": user.email,
                {%- else %}
                "username": user.username,
                {%- endif %}
                "password1": user.password,
                "password2": user.password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        {%- if dxh_py.username_type == "email" %}
        assert "email" in form.errors
        assert form.errors["email"][0] == _("This email has already been taken.")
        {%- else %}
        assert "username" in form.errors
        assert form.errors["username"][0] == _("This username has already been taken.")
        {%- endif %}
