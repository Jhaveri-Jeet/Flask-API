from flask import Blueprint
from api.controllers.userController import registerUser, loginUser

userBp = Blueprint("userBp", __name__)

userBp.route("/register", methods=['POST'])(registerUser)
userBp.route("/login", methods=['POST'])(loginUser)