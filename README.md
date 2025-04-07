# Flask URL Summary API

This project is a Flask-based web application that provides an asynchronous API to accept a URL input and return the page description and summary.

## Project Structure

```
flask-url-summary
├── app
│   ├── __init__.py          # Initializes the Flask application and sets up routes
│   ├── routes.py            # Defines API endpoints
│   ├── services
│   │   └── scraper.py       # Contains logic for fetching HTML content and extracting descriptions
│   └── templates            # Directory for HTML templates (if needed)
├── tests
│   ├── __init__.py          # Initializes the test suite
│   └── test_routes.py       # Contains unit tests for the API routes
├── requirements.txt          # Lists project dependencies
├── config.py                 # Configuration settings for the application
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-url-summary
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
flask run
```

The API will be available at `http://127.0.0.1:5000`.

### API Endpoint

- **POST /api/summary**
  - **Request Body**: 
    ```json
    {
      "url": "https://example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "description": "Page description here",
      "summary": "Page summary here"
    }
    ```

## Testing

To run the tests, use the following command:

```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.