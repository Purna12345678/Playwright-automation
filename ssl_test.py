import truststore
truststore.inject_into_ssl()

import requests

try:
    response = requests.get("https://www.google.com", timeout=10)
    print("SUCCESS")
    print(response.status_code)
except Exception as e:
    print("FAILED")
    print(type(e).__name__)
    print(e)