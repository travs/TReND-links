from flask.ext.login import LoginManager, login_user, logout_user
from app import app
import models
                            

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


