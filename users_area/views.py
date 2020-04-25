from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "users_area/home.html"

