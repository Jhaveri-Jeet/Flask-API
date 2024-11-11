from flask import jsonify, request
from api import db
from api.schemas.userModel import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


def registerUser():
    data = request.get_json()
    
    # Validate that all required fields are provided
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    
    if not name or not password or not email:
        return jsonify({"message": "Name, Email, Password field is required"}), 400
    
    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 409
    
    try:
        # Create the new user
        user = User(name=name, email=email)
        user.setPassword(password)  # Assuming this method hashes the password securely
        
        # Add the user to the database and commit
        db.session.add(user)
        db.session.commit()

        # Respond with a success message
        return jsonify({"message": "User created successfully!", "user": {"name": user.name, "email": user.email}}), 201
    
    except Exception as e:
        # Catch any errors during the database operation
        db.session.rollback()  # Rollback the session in case of an error
        return jsonify({"message": "An error occurred while creating the user", "error": str(e)}), 500


def loginUser():
    data = request.get_json()
    
    # Validate if email and password are provided
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Find the user by email
    user = User.query.filter_by(email=email).first()

    # Check if the user exists and the password matches
    if user and user.checkPassword(password):
        # Create access token for the user
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        # If credentials are invalid, return an unauthorized response
        return jsonify({"message": "Invalid credentials"}), 401
    

def get_user_by_id(user_id):
    return User.query.get_or_404(user_id)


@jwt_required()
def getProfile():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    return jsonify(name=user.name, email=user.email)