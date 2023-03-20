# PDF Merger

## Installation

This library has python dependencies that must be included in the upload to Lambda, learn more here: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html. To install Python dependencies:
  ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
  ```

## Usage

This handler merges multiple remote pdfs into a single document. The handler expects json in the request body, and requires a key `pdf_urls` set as an array of url strings. It then outputs a base64 encoded binary string representation of the merged pdf document.

## Deployment

This script is intended to be hosted on AWS Lambda and API Gateway with proxy turned on. Use the `deply.sh` script to deploy to lambda, making sure to replace any names with your own (e.g. profile).
