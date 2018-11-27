import flask

bp = flask.Blueprint('history', __name__)

@bp.route('/history')
def history():
    return flask.render_template(
        'history/history.html',
        view='history',
        transactions=[
            dict(
                date='2018-11-19',
                amount='20.53',
                description='Cornish Pasty Co',
                ),
            dict(
                date='2018-11-20',
                amount='11.87',
                description='Señor Taco',
                ),
            dict(
                date='2018-11-21',
                amount='71.92',
                description='True Value Hardware',
                ),
            ]
        )
