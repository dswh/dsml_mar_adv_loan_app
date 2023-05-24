from flask import Flask, request
import pickle

app = Flask(__name__)

# loading the ML model
model_pickle = open("./artefacts/classifier.pkl", "rb")
clf = pickle.load(model_pickle)


## first sample endpoint
@app.route("/ping", methods=['GET'])
def ping():
    return {"message": "Hi there, this endpoint is working!!!"}


## endpoint to get template request for model inference
@app.route("/template", methods = ['GET'])
def get_template():
    return {
	"gender": "Male/Female",
	"married": "Married/Unmarried",
	"applicant_income": "<Numeric Salary>",
	"loan_amount": "Numeric loan amount",
	"credit_history": "Cleared Debts / Uncleared Debts"}


##defining the endpoint for the classification
@app.route("/predict", methods=["POST", "GET"])
def prediction():
    """
    Returns the loan application status using ML model.
    """
    loan_req = request.get_json()
    if loan_req['gender'] == "Male":
        gender = 0
    else:
        gender = 1
    if loan_req['married'] == "Unmarried":
        marital_status = 0
    else:
        marital_status = 1
    if loan_req['credit_history'] == "Unclear Debts":
        credit_status = 0
    else:
        credit_status = 1
    applicant_income = loan_req['applicant_income']
    loan_amt = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, applicant_income, loan_amt, credit_status]])

    if result == 0:
        pred = "Rejected"
    else: 
        pred = "Approved"

    return {"loan_approval_status": pred}
    






