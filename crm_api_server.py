from flask import Flask, request, jsonify
from faker import Faker

response_list = []

id = set(range(10000))

fake = Faker()

for i in id:
    
    response = {
            "id": i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth" : str(fake.date_of_birth()),
            "phone": fake.phone_number(),
            "company_name": fake.company(),
            "company_description": fake.bs(),
            "job": fake.job(),
            "email": fake.email(),
            "user_name": fake.user_name(),
            "credit_card" : {
            "credit_card_number": fake.credit_card_number(),
            "credit_card_provider": fake.credit_card_provider(),
            "credit_card_expire": fake.credit_card_expire(),
        },
            "address": {
            "address_street" : fake.street_address(),
            "address_postal" : fake.postcode(),
            "address_country" : fake.country(),
        },

    }

response_list.append(response)

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return jsonify(response_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
