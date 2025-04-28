from Domain.account import account
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

# app = Flask(__name__)

# Mock database of accounts and balances
# accounts = {
#     1: {"balance": 500.0},
#     2: {"balance": 300.0}
# }

class FundTransferService:
    @staticmethod
    def transfer_funds(source_id, destination_id, amount):
        if source_id not in accounts or destination_id not in accounts:
            raise ValueError("Invalid account ID(s)")
        if account[source_id]["balance"] < amount:
            raise ValueError("Insufficient funds")
        
        account[source_id]["balance"] -= amount
        account[destination_id]["balance"] += amount

        transaction = {
            "transactionId": str(uuid.uuid4()),
            "sourceAccountId": source_id,
            "destinationAccountId": destination_id,
            "amount": amount,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "SUCCESS"
        }
        return transaction

# @app.route('/accounts/transfer', methods=['POST'])
def transfer():
    data = request.get_json()
    try:
        source_id = data['sourceAccountId']
        destination_id = data['destinationAccountId']
        amount = data['amount']

        transaction = FundTransferService.transfer_funds(source_id, destination_id, amount)
        return jsonify(transaction), 200
    except (KeyError, TypeError):
        return jsonify({"error": "Invalid input format"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
