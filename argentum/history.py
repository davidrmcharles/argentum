import flask

bp = flask.Blueprint('history', __name__)

@bp.route('/history')
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
