from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for doctors (replace this with your actual data source)
doctors = [
    {"name": "Dr. Smith", "domain": "Cardiology"},
    {"name": "Dr. Johnson", "domain": "Dermatology"},
    {"name": "Dr. Brown", "domain": "Pediatrics"},
    # Add more doctors here
]

@app.route('/doctors', methods=['GET'])
def get_doctors_by_domain():
    domain = request.args.get('domain')  # Get the domain from query parameter
    if domain:
        domain_doctors = [doctor for doctor in doctors if doctor['domain'] == domain]
        return jsonify(domain_doctors)
    else:
        return jsonify({"error": "Domain parameter is missing."}), 400

if __name__ == '__main__':
    app.run(debug=True)
