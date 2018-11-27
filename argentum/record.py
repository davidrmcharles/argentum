import datetime
import flask

bp = flask.Blueprint('record', __name__)

@bp.route('/record', methods=['GET', 'POST'])
def record():
    if flask.request.method == 'GET':
        return flask.render_template(
            'record/record.html',
            today=datetime.datetime.now().strftime('%Y-%m-%d')
            )

    if flask.request.method == 'POST':
        return 'Recorded!'
