import flask

bp = flask.Blueprint('status', __name__)

@bp.route('/')
def index():
    return flask.redirect(flask.url_for('status'))

@bp.route('/status', methods=['GET', 'POST'])
def status():
    if flask.request.method == 'GET':
        return '''\
<!DOCTYPE html>
<html>
  <head>
    <title>argentum</title>
  </head>
  <body>
    <h1>argentum</h1>
    <h2>
      Status |
      <a href="/record">Record</a> |
      <a href="/history">History</a>
    </h2>
    <ul>
      <li>Period: 2018-11-16..2018-11-29</li>
      <li>Budget: $1200.00</li>
      <li>Spent: $999.00</li>
      <li>Remaining: $201.00</li>
    </ul>
    <form method="post" onsubmit="return confirm('Are you sure?');">
      <input type="submit" value="Finalize"/>
    </form>
  </body>
</html>
'''

    if flask.request.method == 'POST':
        return 'Finalized!'
