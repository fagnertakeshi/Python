from googleapiclient.discovery import build
from google.oauth2 import service_account

# Set up API credentials
credentials = service_account.Credentials.from_service_account_file('C:\\dev\\Python\\youtube\\credentials.json')
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']
api_service_name = 'youtube'
api_version = 'v3'

# Create a client
youtube = build(api_service_name, api_version, credentials=credentials)

# Example: Log in to YouTube account
def login_to_youtube():
    # Authenticate and authorize the request
    request = youtube.channels().list(part='snippet', mine=True)
    response = request.execute()

    # Check if the authentication was successful
    if 'items' in response:
        print("Logged in successfully!")
        # TODO: Implement video upload logic here
    else:
        print("Failed to log in.")

# Call the login function
login_to_youtube()
