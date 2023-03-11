import hashlib
import base64

def shorten_url(url):
    # Use SHA-256 hash function to generate a unique identifier for the URL
    hash_object = hashlib.sha256(url.encode())
    hash_bytes = hash_object.digest()

    # Encode the hash using base64 to generate a short URL
    base64_bytes = base64.urlsafe_b64encode(hash_bytes[:9])
    short_url = base64_bytes.decode().rstrip('=')

    return short_url

# Example usage
url = "https://shahportfolio.com"
short_url = shorten_url(url)
print(short_url)
