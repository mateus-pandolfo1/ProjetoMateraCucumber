import requests
from behave import given, when, then

BASE_URL = "https://catfact.ninja"

@given("the API is available")
def step_check_api_available(context):
    response = requests.get(BASE_URL + "/breeds")
    assert response.status_code == 200, f"API is not available. Status code: {response.status_code}"

@when('I send a GET request to "/breeds"')
def step_send_get_request(context):
    context.response = requests.get(BASE_URL + "/breeds")

@then("I should receive a 200 status code")
def step_check_status_code_200(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"

@then("the response should contain a list of breeds")
def step_check_response_body(context):
    json_data = context.response.json()
    assert "data" in json_data, "Response does not contain 'data' field"
    assert isinstance(json_data["data"], list), "'data' field is not a list"

@when('I send a GET request to "/invalid-endpoint"')
def step_send_get_request_invalid_url(context):
    context.response = requests.get(BASE_URL + "/invalid-endpoint")

@then("I should receive a 404 status code")
def step_check_status_code_404(context):
    assert context.response.status_code == 404, f"Expected 404, got {context.response.status_code}"

@then("the response should contain an error message")
def step_check_error_message(context):
    json_data = context.response.json()
    assert "message" in json_data, "Response does not contain 'message' field"