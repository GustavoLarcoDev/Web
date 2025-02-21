import requests
import os
from PIL import Image
from io import BytesIO

def download_and_save_image(url, filename, size=(1200, 800)):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize(size)
        img.save(f'images/{filename}', 'JPEG', quality=85)
        print(f'Successfully downloaded and saved {filename}')
    except Exception as e:
        print(f'Error downloading {filename}: {str(e)}')

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# List of images to download
images = [
    ('https://gustavolarcodev.github.io/static/media/hero-bg.jpg', 'portfolio-preview.jpg'),
    ('https://gustavolarcodev.github.io/Impulsoyz/images/team.jpg', 'impulsoyz-preview.jpg'),
    ('https://gustavolarcodev.github.io/bella-nails-salon/images/gallery/1.jpg', 'bella-nails-preview.jpg'),
    ('https://gustavolarcodev.github.io/restaurant-la-mesa/images/hero.jpg', 'la-mesa-preview.jpg'),
    ('https://gustavolarcodev.github.io/casa-estilo-furniture/images/hero.jpg', 'casa-estilo-preview.jpg'),
    ('https://gustavolarcodev.github.io/urban-style-clothing/images/hero.jpg', 'urban-style-preview.jpg'),
]

# Download each image
for url, filename in images:
    download_and_save_image(url, filename)
