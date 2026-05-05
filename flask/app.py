from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/book', methods=['POST'])
def book():
    data = request.get_json() or {}
    required = ['origin', 'destination', 'depart_date', 'passengers']
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({'success': False, 'error': f'Missing fields: {missing}'}), 400

    booking_id = str(uuid.uuid4())
    response = {
        'success': True,
        'booking_id': booking_id,
        'summary': {
            'origin': data.get('origin'),
            'destination': data.get('destination'),
            'depart_date': data.get('depart_date'),
            'return_date': data.get('return_date'),
            'passengers': data.get('passengers'),
            'class': data.get('class') or 'Economy'
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
