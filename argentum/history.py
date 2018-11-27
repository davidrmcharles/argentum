import flask

bp = flask.Blueprint('history', __name__)

@bp.route('/history')
def history():
    return flask.render_template(
        'history/history.html',
        transactions=[
            dict(
                date='2018-11-20',
                amount='11.87',
                description='Señor Taco',
                ),
            ]
        )
