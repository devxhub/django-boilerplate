from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
{%- if dxh_py.use_drf == "y" %}
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
{%- endif %}
from {{ dxh_py.project_slug }}.users.models import User
import environ

env = environ.Env()

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    {%- if dxh_py.username_type == "email" %}
    slug_field = "id"
    slug_url_kwarg = "id"
    {%- else %}
    slug_field = "username"
    slug_url_kwarg = "username"
    {%- endif %}


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None=None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        {%- if dxh_py.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.request.user.username})
        {%- endif %}


user_redirect_view = UserRedirectView.as_view()


{%- if dxh_py.use_drf == "y" %}
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = env("FACEBOOK_CALLBACK_URL")


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = env("GOOGLE_CALLBACK_URL")
    client_class = OAuth2Client
{%- endif %}
