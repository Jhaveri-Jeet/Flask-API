from flask import Blueprint
from api.controllers.userController import registerUser, loginUser, getProfile

userBp = Blueprint("userBp", __name__)

userBp.route("/register", methods=['POST'])(registerUser)
userBp.route("/login", methods=['POST'])(loginUser)
userBp.route("/profile",methods=['GET'])(getProfile)