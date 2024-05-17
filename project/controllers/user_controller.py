from .general_controller import GeneralController
from project.models import User

class UserController(GeneralController):
    _model_type = User