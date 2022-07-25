import wsgi; from core.models import User

BOT_TOKEN = ""

class USER:
    def get(self, **kwargs):
        user = User.objects.filter( **kwargs )
        if user.exists():
            return user.first()
        return False
    
    def create(self, **kwargs):
        user = User( **kwargs )
        try:
            user.save(); return True
        except Exception as e:
            return False
    
    def delete(self, **kwargs):
        user = User.objects.filter( **kwargs )
        if user.exists():
            try: user.delete(); return True
            except Exception as e: pass
        return False