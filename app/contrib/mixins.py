from django.views.generic import TemplateView


class TemplateNameMixin(TemplateView):
    template_name = None

    def get_template_names(self):
        if self.request.user.is_staff:
            return ['adm/' + self.template_name]
        return ['site/' + self.template_name]
