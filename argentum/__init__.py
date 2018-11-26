import os
import flask

def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'argentum.sqlite'),
        )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import status
    app.register_blueprint(status.bp)

    from . import record
    app.register_blueprint(record.bp)

    from . import history
    app.register_blueprint(history.bp)

    return app
