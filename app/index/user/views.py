# -*- coding: utf8 -*-
from app.contrib.mixins import TemplateNameMixin


class UserView(TemplateNameMixin):
    template_name = 'index/user.html'
