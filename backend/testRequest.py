import requests
import base64
import json

# url = "https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search_by_image?&limit=3&sort=price"

url = "https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?&limit=3&sort=best_match"


headers = {
    "Authorization": "Bearer v^1.1#i^1#r^0#I^3#p^1#f^0#t^H4sIAAAAAAAAAOVYa2wUVRTuPlpEqCJUgQbNdpCoNDN7Z6f7mKG7ydJtu4VCt92lYBOFO7N3trOPmWFmlnZ5pVZFYwA1ihpEJZGYGCM/SFVAgklFMGCMQWKEAAmRR6WKhGBAfhBndpeyrQSQbmIT989mzj333O/77jn3BXrKxs9eF1x3pdw0zry1B/SYTSZyAhhfVlr9gMVcWVoCChxMW3se77H2WgZqVZhKykwbUmVJVJGtO5UUVSZr9GJpRWQkqAoqI8IUUhmNY8L+Bc2MgwCMrEiaxElJzNYU8GKQhW43cNZwTsjzFGR1q3gjZkTyYjwJPbQ7ilzIA0kaRfV2VU2jJlHVoKh5MQdwUDhJ4oCKAJJx0IyDItwOugOztSNFFSRRdyEA5svCZbJ9lQKst4cKVRUpmh4E8zX5G8It/qZA/cJIrb0gli+vQ1iDWlod/lUnRZGtHSbT6PbDqFlvJpzmOKSqmN2XG2F4UMZ/A8w9wM9KzQKXriGLaJ7jaMA7iyJlg6SkoHZ7HIZFiOJ81pVBoiZomTspqqvBxhGn5b8W6iGaAjbjrzUNkwIvIMWL1c/1P+0PhTDfAhhHKOpP4CFF4FB9BuGhtgDOe1gPzQMS4rwbQcrhducHykXLyzxipDpJjAqGaKptoaTNRTpqNFIbskAb3alFbFH8vGYgKvSjbmhIkh3GpOZmMa11isa8opQuhC37eecZGOqtaYrApjU0FGFkQ1YivaxkWYhiIxuzuZhPn27Vi3VqmszY7V1dXUQXRUhKzO4AgLQvWdAc5jpRCmK6r1HrOX/hzh1wIUuFQ3pPVWC0jKxj6dZzVQcgxjBfjcdJUiCv+3BYvpHWfxgKONuHV0SxKoSiWBfinMAR5Z3QxaJiVIgvn6R2AwdiYQZPQSWBNDkJOYRzep6lU0gRogzl5B2Uh0d41EXzeA3N8zjrjLpwkkcIIMSyHO35PxXK3aZ6GHEK0oqS60XL80bZubIh0RoLqJISpLVQx+L2VDrSHZcVz4pY57zgku7l4WDN4naU8HjvthpuSb4uKejKRPTxiyGAUevFEyEoqRqKjopemJNkFJKSApcZWxNMKdEQVLRMGCWTumFUJP2y3FSctbpo9P7lMnFvvIu3R/1H+9MtWalGyo4tVkZ/VQ8AZYEwdiCCk1J2o9YlqB8/DPPSLOpR8Rb0k+uYYq2TzLEVorkjJ5GlS6grOEJBqpRW9NM20WKcwCJSAon6fqYpUjKJlHZy1PWcSqU1yCbRWCvsIiS4AMfYZku6aP2KWEO7qFHx4rJb6dKxtiQVYym2Nt7jsdo+/JLvK8n+yF5TP+g17TWbTKAWzCJngqoyyyKrZWKlKmiIECBPqEJM1O+uCiISKCNDQTFPKbkCzr3L/Rb8+JXE9a7lZ+esKSl8Y9j6DJg29Mow3kJOKHhyADNutpSSD04td1AkCShAOmgH1QFm3my1ko9YKzrnTX/i9T/3Dl479tqm+WvZltgXk74D5UNOJlNpibXXVDKz6vDPmy+VmxYtXfylZWpVvP5A5aST1YGpk37sW42OlJ3ef9FRe/IIXzXxTPW1Htw88Kvv003bKx8F+MMVF8DAU5M/2znnF2b6jg0TPly9pHrV7rXLdr3Kv3f9oz9Ozbl6nzfY1zhu+/4pVU+2rnorXV5+PLHth1WTz86wH3zp7fMP7Tq5/Ju5A5cvHqq1HO2PfSI2fPvB+njV75+3Te9vPTb//Dzh3NW+M1MGDwubLbvBG17qxE/7YqlTL4t7+nYeemH2O199v+3y+xvaZlw9+jzcURHYt/4S9ua0ZVsq1qw/ULeH2fLXbOWxF+3URmv11ytP1C1rPH0w3jw4OO14c1f1hef6j8T3bzRH7n92VjA3l38DoBTfev0RAAA=",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Content-Language": "en-US"
}

try:
    # Read the image file
    with open("/Users/dami/Desktop/PriceEye/price-eye/src/assets/knives.jpeg", "rb") as file:
        image_data = file.read()

    # Base64 encode the image data
    encoded_image = base64.b64encode(image_data).decode("utf-8")

    request_data = {
        "image": encoded_image,
        # other request data...
    }

    response = requests.post(url, headers=headers, json=request_data)

    print("Status Code", response.status_code)
    print("JSON Response", response.json())

    # Save the JSON response to a file
    with open("response.json", "w") as json_file:
        json.dump(response.json(), json_file)

    # Parse the JSON response
    parsed_response = response.json()
    warnings = parsed_response['warnings']
    href = parsed_response['href']
    total = parsed_response['total']
    next_url = parsed_response['next']
    limit = parsed_response['limit']
    offset = parsed_response['offset']
    item_summaries = parsed_response['itemSummaries']

    # Access specific information from the item summaries
    for item_summary in item_summaries:
        item_id = item_summary['itemId']
        title = item_summary['title']
        leaf_category_ids = item_summary['leafCategoryIds']
        categories = item_summary['categories']
        image_url = item_summary['thumbnailImages'][0]['imageUrl']
        price = item_summary['price']['value']
        # ... access other information as needed

except requests.exceptions.RequestException as e:
    # Handle network or connection issues
    print(f"Request Exception: {e}")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")