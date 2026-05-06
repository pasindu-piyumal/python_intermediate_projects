from typing import Final
import requests

API_KEY: Final[str] = 'f663ad0b9544b97eef25aa8a6d604e564d946'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link: str):
    payload: dict = {
        'key': API_KEY,
        'short': full_link
    }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        if url_data.get('status') == 7:
            short_link: str = url_data['shortLink']
            print(f'Shortened link: {short_link}')  
        else:
            print('Error: Unable to shorten the link. Please check the URL and try again.')

def main():
    input_link: str = input('Enter the URL you want to shorten: ')
    shorten_link(input_link)

if __name__ == "__main__":
    main()