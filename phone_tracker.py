import phonenumbers
import requests

def get_phone_number_details(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number"

        # Get the carrier information
        carrier = phonenumbers.carrier.name_for_number(parsed_number, "en")
        region = phonenumbers.region_code_for_number(parsed_number)

        # Get the geolocation (you can use a third-party API for this)
        geolocation = get_geolocation(phone_number)

        return {
            "phone_number": phone_number,
            "carrier": carrier,
            "region": region,
            "geolocation": geolocation
        }
    except Exception as e:
        return str(e)

def get_geolocation(phone_number):
    # Replace 'YOUR_API_KEY' with your actual API key from a geolocation service
    api_url = f"https://api.example.com/geolocation?phone={phone_number}&key=YOUR_API_KEY"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Geolocation data not available"

if __name__ == "__main__":
    phone_number = input("Enter the phone number to track: ")
    details = get_phone_number_details(phone_number)
    print(details)