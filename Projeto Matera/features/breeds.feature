Feature: Test API endpoint GET /breeds

  Scenario: Retrieve a list of breeds successfully
    Given the API is available
    When I send a GET request to "/breeds"
    Then I should receive a 200 status code
    And the response should contain a list of breeds

  Scenario: Error when sending an invalid limit parameter
    Given the API is available
    When I send a GET request to "/breeds" with an invalid limit "invalid"
    Then I should receive a 404 status code
    And the response should contain an error message
