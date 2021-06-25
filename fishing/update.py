from .models import CustomUser

def update():
    users = CustomUser.objects.all()
    i = 0
    for user in users:
        user.nick = user.nick + str(i)
        user.save()
        i += 1
