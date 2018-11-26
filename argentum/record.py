import flask

bp = flask.Blueprint('record', __name__)

@bp.route('/record', methods=['GET', 'POST'])
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
