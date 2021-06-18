from django.template import loader
from django.http import HttpResponse

from wavepool.code_exercise_defs import code_exercise_defs, code_review_defs, code_design_defs
from django.conf import settings


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')

    context = {
        'code_exercise_defs': code_exercise_defs,
        'code_design_defs': code_design_defs,
        'code_review_defs': code_review_defs,
        'user_type': settings.USER_TYPE,
    }
    return HttpResponse(template.render(context, request))
