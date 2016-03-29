from django.views.generic import TemplateView

from django.conf import settings
from django.utils import translation as trans_settings


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        context = {}

        if 's' in self.request.GET:
            s = self.request.GET['s']
        else:
            s = False

        if s:
            dim = {'M': 'minds',
                   'F': 'finance',
                   'A': 'appearance',
                   'T': 'touch',
                   'B': 'behavior',
                   'L': 'language',
                   'S': 'stimulation'}

            for i, x in enumerate(dim.keys()):

                # MINDS 1.---7. STIMULATION
                if x.lower() in s and x.upper() in s:
                    context[dim[x]] = ''
                elif x.lower() in s:
                    context[dim[x]] = x.upper()+'-'*(s.count(x.lower())-1)
                elif x.upper() in s:
                    context[dim[x]] = x.upper()+'+'*(s.count(x.upper())-1)
            
            # 8. GENDER
            if 'x' in s.lower() and 'y' in s.lower():
                context['gender'] = 'bisexual'
            elif 'x' in s.lower():
                context['gender'] = 'female'
            elif 'y' in s.lower():
                context['gender'] = 'male'
            else:
                context['gender'] = ''

        context.update(kwargs)
        return context
