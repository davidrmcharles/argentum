import flask

bp = flask.Blueprint('status', __name__)

@bp.route('/')
def index():
    return flask.redirect(flask.url_for('status.status'))

@bp.route('/status', methods=['GET', 'POST'])
def status():
    if flask.request.method == 'GET':
        return flask.render_template(
            'status/status.html',
            first_day='2018-11-16',
            last_day='2018-11-29',
            budget='$1200.00',
            spent='$999.00',
            remaining='$201.00',
            )

    if flask.request.method == 'POST':
        return 'Finalized!'
