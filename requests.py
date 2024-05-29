import requests # type: ignore

# Application URL
APP_URL = "http://example.com"

def check_application():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            print("Application is up")
        else:
            print(f"Application is down (Status code: {response.status_code})")
    except requests.ConnectionError:
        print("Application is down (Connection error)")

if __name__ == "__main__":
    check_application()