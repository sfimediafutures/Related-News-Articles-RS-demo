from bs4 import BeautifulSoup
import requests

def get_image_src(url):
    """
    Fetches the image source URL from a given article URL.

    Parameters:
    url (str): The URL of the page to scrape.

    Returns:
    str: The image source URL if found, otherwise an error message.
    """
    #Prepare for TV2
    url = 'https://www.tv2.no/nyheter/' + url
    # Fetch the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the specific structure of containers to reach the target image
    container = soup.find('div', class_='articleHeader-article')
    if container:
        image_div = container.find('figure', class_='image--articleheader')
        if image_div:
            img_tag = image_div.find('img', class_='image__img')
            if img_tag and 'src' in img_tag.attrs:
                return img_tag['src']
            else:
                return "Image tag or src attribute not found."
        else:
            return "Image container not found."
    else:
        return "Main container not found."

# Example usage
if __name__ == "__main__":
    url = 'TV2-14517245'  # Replace with the actual URL
    image_src = get_image_src(url)
    print("Image src:", image_src)