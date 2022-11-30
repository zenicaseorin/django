# from django.http import HttpResponse
#
# def homePageView(request):
#     return HttpResponse("안녕하세요 :)")

from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = "home.html"


class second(TemplateView):
    template_name = "second.html"


class yakwan(TemplateView):
    template_name = "yakwan.html"
