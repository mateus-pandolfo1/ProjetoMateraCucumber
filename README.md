# BDD API Testing with Behave

## Overview
This project implements automated BDD (Behavior-Driven Development) tests using Behave to validate the `/breeds` endpoint of the `catfact.ninja` API. The tests ensure that the API is functional and correctly returns expected responses.

## Technologies Used
- Python
- Behave (BDD framework)
- Requests (for HTTP requests)

## Installation
### Prerequisites
Make sure you have Python installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Tests
To execute the BDD tests, run the following command:
```sh
behave
```

## Test Scenarios
The tests cover the following scenarios:

### 1. Checking API Availability
- **Given** the API is available
- **When** I send a GET request to `/breeds`
- **Then** I should receive a 200 status code
- **And** the response should contain a list of breeds

### 2. Sending a GET request with an invalid limit parameter
- **When** I send a GET request to `/breeds` with an invalid limit
- **Then** I should receive a 404 status code
- **And** the response should contain an error message

## Folder Structure
```
project-root/
│── features/
│   ├── breeds.feature  # BDD feature file
│   ├── steps/
│   │   ├── breeds_steps.py  # Step definitions
│── requirements.txt  # Project dependencies
│── README.md  # Documentation
```

