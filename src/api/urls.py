from app import swagger
from .views import (
    Register
)

swagger.add_resource(Register, '/register/')
