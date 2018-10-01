from flask import Flask, render_template
from flask import request
from flask import make_response
from constants import AircraftType

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():

    if request.method == 'GET':
        context = {
            'aircrafy_type_opts': AircraftType.to_select_options(alphabetic_order=True)
        }
        return render_template('aircraft_create.html', **context)

    elif request.method == 'POST':

        if request.form['aircraft_type'] not in AircraftType.get_all():
            return make_response('Invalid aircraft type "%s". Should be one of "%s"' % (
                request.form['aircraft_type'], AircraftType.get_all()))

        return make_response('New aircraft created...')

    else:
        raise NotImplementedError()


if __name__ == '__main__':
    app.run(debug=True, port=8080)
