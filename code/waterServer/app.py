import flask
import settings

# Views
from main import Main
from login import Login
from water import Water
from temp import Temperature
from chart import Chart
from startAquaPi import Start
from contact import Contact

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/water/',
		 view_func=Water.as_view('water'),
		 methods=['GET', 'POST'])
app.add_url_rule('/temp/',
                 view_func=Temperature.as_view('temp'),
                 methods=['GET'])
app.add_url_rule('/chart/',
                 view_func=Chart.as_view('chart'),
                 methods=['GET'])
app.add_url_rule('/water/',
		 view_func=Start.as_view('startAquaPi'),
		 methods=['GET', 'POST'])
app.add_url_rule('/contact/',
		 view_func=Contact.as_view('contact'),
		 methods=['GET', 'POST'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404

app.debug = True
app.run(host='0.0.0.0', port=5000)
