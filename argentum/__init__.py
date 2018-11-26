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

    @app.route('/')
    def index():
        return flask.redirect(flask.url_for('status'))

    @app.route('/status', methods=['GET', 'POST'])
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

    @app.route('/record', methods=['GET', 'POST'])
    def record():
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
      <a href="/status">Status</a> |
      Record |
      <a href="/history">History</a>
    </h2>
    <form method="post">
      <label for="date">Date</label><br/>
      <input type="text" id="date"><br/>

      <label for="amount">Amount</label><br/>
      <input type="text" id="amount"><br/>

      <label for="description">Description</label><br/>
      <input type="text" id="description"></br>

      <input type="submit" value="Record"/>
    </form>
  </body>
</html>
'''
        if flask.request.method == 'POST':
            return 'Recorded!'

    @app.route('/history')
    def history():
        return '''\
<!DOCTYPE html>
<html>
  <head>
    <title>argentum</title>
  </head>
  <body>
    <h1>argentum</h1>
    <h2>
      <a href="/status">Status</a> |
      <a href="/record">Record</a> |
      History
    </h2>
    <table>
      <tr>
        <th>Date</th>
        <th>Amount</th>
        <th>Description</th>
      </tr>
      <tr>
        <td>2018-11-20</td>
        <td>11.87</td>
        <td>Senor Taco</td>
      </tr>
      <tr>
      </tr>
      <tr>
      </tr>
    </table>
  </body>
</html>
'''

    return app
