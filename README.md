# Projeto Matera Cucumber

## Overview
This project provides automated tests for the Cat Breeds API (https://catfact.ninja) using Behavior-Driven Development (BDD) practices. The tests are implemented with the Behave framework in Python and utilize the Requests library to perform HTTP calls. The main goal is to verify that the API endpoints behave as expected, including proper handling of both valid and invalid requests.

## Test Scenarios
The project includes the following test scenarios defined in the `breeds.feature` file:

- **Successful Cat Breeds Retrieval:**  
  Verifies that when a GET request is sent to the `/breeds` endpoint, the API responds with a 200 status code and returns a list of cat breeds.

- **Invalid Endpoint Error Handling:**  
  Checks that when a GET request is sent to an invalid endpoint (e.g., `/invalid-endpoint`), the API responds with a 404 status code along with an error message.

## Technologies Used
- **Python:** Programming language for implementing tests.
- **Behave:** BDD testing framework that uses Gherkin syntax to describe test scenarios.
- **Requests:** Python HTTP library for making API calls.
- **Gherkin & BDD:** For writing clear, human-readable test scenarios.

## Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Set Up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *If a requirements file is not available, install the necessary packages manually:*
   ```bash
   pip install behave requests
   ```

## Project Structure
```
├── features
│   ├── breeds.feature       # Gherkin feature file defining the test scenarios
│   └── steps
│       └── breeds_steps.py  # Step definitions implementing the test logic
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Running the Tests
To execute all test scenarios, navigate to the project root directory and run:
```bash
behave
```
To run a specific scenario, you can use the `--name` option. For example:
- **Run the "Successful Cat Breeds Retrieval" scenario:**
  ```bash
  behave --name "Successful Cat Breeds Retrieval"
  ```
- **Run the "Invalid Endpoint Error Handling" scenario:**
  ```bash
  behave --name "Invalid Endpoint Error Handling"
  ```

## Additional Resources
For further information on the tools and methodologies used in this project, please refer to the following documentation:
- [JavaScript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Cypress Documentation](https://docs.cypress.io)
- [GitHub Documentation](https://docs.github.com)
- [StackOverflow](https://stackoverflow.com/)
- [QA and Automated Testing Guides](https://www.softwaretestinghelp.com/)
- [Jira Documentation](https://www.atlassian.com/software/jira)
- [Gherkin Language Documentation](https://cucumber.io/docs/gherkin/) & [BDD Practices](https://cucumber.io/docs/bdd/)

## Contributing
Contributions, issues, and feature requests are welcome! For more details, please see the [GitHub issues page](https://github.com/).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy testing!
