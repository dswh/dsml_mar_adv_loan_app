import pytest

from app import app

## we need to run a server to test the flask app
@pytest.fixture
def client():
    return app.test_client()


## testing the ping endpoint
def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, this endpoint is working!!!"}


## testing the prediction endpoint
def test_prediction_approval(client):
    test_data = {"gender":"Male", "married":"Unmarried",
               "credit_history" : "Unclear Debts","applicant_income":100000,
               "loan_amount":2000000}
    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': "Rejected"}
