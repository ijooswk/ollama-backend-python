from flask import Blueprint, request, jsonify
from app.services.scraper import url_summary

import asyncio
import threading

api = Blueprint('api', __name__)

@api.route('/extract-description', methods=['POST'])
async def extract_description():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Respond immediately with 200
    response = jsonify({'message': 'Processing started'})
    response.status_code = 200

    def process_and_save():
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            description = loop.run_until_complete(url_summary(url))
            # Log or use the description
            print(f"Description for URL {url}: {description}")
        except Exception as e:
            # Log the error or handle it as needed
            print(f"Error processing URL {url}: {e}")
        finally:
            loop.close()

    # Run the task in a separate thread to avoid blocking
    threading.Thread(target=process_and_save).start()
    return response