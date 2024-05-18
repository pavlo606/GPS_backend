from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .user_route import user_bp

    app.register_blueprint(user_bp)