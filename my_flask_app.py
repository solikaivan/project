from flask import Flask, render_template, request, jsonify
import weather_bot  # Import your Python bot script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    city = request.form['city']
    weather_info = weather_bot.get_weather(city)
    return jsonify({'weather': weather_info})  # Return data as JSON
  else:
    return render_template('index.html')

@app.route('/get_weather')
def get_weather_data():
  city = request.args.get('city')
  weather_info = weather_bot.get_weather(city)
  return jsonify({'weather': weather_info})

if __name__ == '__main__':
  app.run(debug=True)
