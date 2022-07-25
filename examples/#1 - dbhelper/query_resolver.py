import wsgi
from core.models import Film

film = Film(name = "Avatar", count=3)
film.save()

print(Film.objects.all())