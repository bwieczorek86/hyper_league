from django.http import HttpResponse

from hyper_leaque_backend.models import Team


def index(request):
    teams = Team.objects.all()
    output = ', '.join([f'{q.player_one} / {q.player_two}' for q in teams])
    return HttpResponse(output)





