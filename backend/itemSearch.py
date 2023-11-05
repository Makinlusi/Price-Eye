from flask import Flask, request, jsonify
import requests
import base64
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

url = "https://api.ebay.com/buy/browse/v1/item_summary/search_by_image?&limit=3&sort=best_match"

headers = {
    "Authorization": "Bearer v^1.1#i^1#p^1#I^3#f^0#r^0#t^H4sIAAAAAAAAAOVYbYwTRRhur70zl/MgfnGIKGVPMIC7ne2223ahTXpftgZoofXA0xO2u7N3e213l90pbVHwvB9gQAwYMSCJkgjIgSTGLySIcqcBotEEQ4KiaERAYjCokY+AX7vtcfROAsg18RL7Y5t55513nueZ952ZXdBZUTl5aXDpuWrzTWUbOkFnmdlMVoHKivIpIyxlY8pNoMjBvKHz3k5rl+XkNI1NJRVmNtQUWdKgLZtKShqTN/qwtCoxMquJGiOxKagxiGOigRnTGQcBGEWVkczJScwWavBhtECyFHDSpNtBkyzn0a3SpZgx2YdxcRckaZr3AOCivZTRr2lpGJI0xErIhzmAg8JJEgfOmINiSCdD0QQgnS2YrRmqmihLugsBMH8eLpMfqxZhvTpUVtOgivQgmD8UaIqGA6GGxpmxafaiWP4+HaKIRWltYKte5qGtmU2m4dWn0fLeTDTNcVDTMLu/MMPAoEzgEpgbgJ+XOi7EeeClOC9FxTm3w10SKZtkNcWiq+MwLCKPC3lXBkpIRLlrKaqrEe+AHOprzdRDhBpsxt+sNJsUBRGqPqyxLvBwIBLB/DPYDgj5QAKPqCIHG3MQj8xuwAVP3OMVAMnighuylMPt7puoEK1P5kEz1csSLxqiabaZMqqDOmo4WBtQpI3uFJbCakBABqJ+P1cMkP0aghZjUQurmEbtkrGuMKULYcs3r70C/aMRUsV4GsH+CIM78hL5MFZRRB4b3JnPxb70yWo+rB0hhbHbM5kMkaEIWW2zOwAg7XNnTI9y7TDFYrqvUesFf/HaA3AxT4WD+khNZFBO0bFk9VzVAUhtmN/pcZEU6NN9ICz/YOs/DEWc7QMrolQV4vK6vS4HzUNvXGA5vhQF4u/LUbsBA8bZHJ5i1QRESpLlIM7paZZOQVXkGcolOCiPAHGe9gq40ysIeNzF0zgpQAggjMc5r+f/VCfXm+lRyKkQlSTVS5bmDyiuRU2JWW0NmqwGvSjSMqc5lY5lOxTVs7Ct/cHg3OyCaNA5pxkmPL7rLYYrkq9PiroyMX3+4VfrQVlDkB8SvSgnKzAiJ0UuN7wWmFL5CKuiXBQmk7phSCQDihIqzVZdMnr/cpu4Md6lO6L+o+Ppiqw0I2WHFytjvKYHYBWRME4ggpNTdtmodVa/fRjmeXnUQ+It6hfXYcVaJ1lgK/KFGychG3QJbSFHqFCT06p+2SbCxgUsJiegpJ9nSJWTSag2k0Ou51Qqjdh4Eg63wi5BgovsMDtsSdrrJSkv7aaHxIvLH6XzhtuWVJKt2Np0Y7dq+8B3fL8p/yO7zL2gy/x+mdkMpoEJZC0YX2F5yGq5eYwmIkiIrEBoYpukv7qqkEjAnMKKatltpnPgh/XcqWD38sSfmQUnpi42FX9i2NAKRvd/ZKi0kFVFXxzA2Ms95eTImmoHRZLAqT+dFN0Cai/3WslR1tufOrT1eO2JZ93fH4zduv3HO9sf/by7B1T3O5nN5SZrl9lUv/yO7rfH/Vr9zYdvdlyoKHupe+OSZUtMNYndC+7eU3XX769+Xf1F75H5E587vPNn4fTmWIOpZ/VrY4nVrRaTY//Sibtf6Nm8JXyma2VwsvXollVfSTsWlb01a3vvxaqpH7yXmd8xWhq97OAmurX2l41r1tD3H6kJ7Wq8755PT+Krjo2rW7TN/dFv0bbjIybtGzkue37vpJe/3RN+8vE9U/76Y/+X1aPm9LzSvRPb8RgKTThw8bvTK39akT6apJZvOswc+6zh6dm1452v1wP0yDOnTj1fOap58bqtu866T9+ydv3Hh9ZutiyuE1ue2PZueO/5M0u4Fy/UnM1JO6e/ceyTZTtWZw+/s6537oGMu3Xf2PUjCmv5NxIYMF78EQAA",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Content-Language": "en-US"
}


@app.route('/search', methods=['POST'])
def search_by_image():
    try:
        #check if the image file is present in the request
        if 'image' in request.files:
            image_file = request.files['image']
            print('Recieved file', image_file.filename)

            # Base64 encode the image data
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

            # Prepare the request data
            request_data = {
                "image": encoded_image,
            }

            # Send a POST request to the eBay API
            response = requests.post(url, headers=headers, json=request_data)
            with open('response.json', 'w') as file:
                json.dump(response.json(), file)
                #data = json.load(file)
            


            # Parse the JSON response and return it
            return jsonify(response.json())
        else:
            return jsonify({"error": "No file uploaded"})

    except requests.exceptions.RequestException as e:
        # Handle network or connection issues
        return jsonify({"error": str(e)})

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run()