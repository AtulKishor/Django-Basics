from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
# class CBView(View):
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'basic inject'
        return context