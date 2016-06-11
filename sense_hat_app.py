from flask import Flask, render_template, request, redirect, url_for
from sense_hat import SenseHat
app = Flask(__name__)

def humidity():
    return SenseHat().get_humidity()

def temperature():
    return SenseHat().get_temperature()

def temperature_from_humidity():
    return SenseHat().get_temperature_from_humidity()

def temperature_from_pressure():
    return SenseHat().get_temperature_from_pressure()

def pressure():
    return SenseHat().get_pressure()

@app.route("/")
def root():
    templateData = {
        'title' : 'SenseHat Controller',
        'temperature' : temperature(),
        'humidity' : humidity(),
        'temperature_from_humidity' : temperature_from_humidity(),
        'temperature_from_pressure' : temperature_from_pressure(),
        'pressure' : pressure(),
        }
    return render_template('root.html', **templateData)

@app.route("/message", methods=['POST'])
def message():
    sense = SenseHat()
    sense.set_rotation(180)
    color = tuple(map(ord, request.form['color'].decode('hex')))
    sense.show_message(request.form['message'], text_colour=color)
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
