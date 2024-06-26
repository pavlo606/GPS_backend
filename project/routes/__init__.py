from flask import Flask

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    from .user_route import user_bp
    from .route_route import route_bp
    from .point_route import point_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(point_bp)