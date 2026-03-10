"""
# CHAPTER 6 EXERCISE 3
'''
URL Shortener Simulator Exercise

Create a mini URL shortener like a simplified TinyURL.

Requirements

- A long URL should get a short code (for example: "a1b2c3")
- If the same URL is shortened again, return the same code
- If a collision happens (same code for different URL), resolve it
- Be able to:
    - shorten a URL
    - retrieve the original URL from a short code
    - track how many times a short code was used

Hint!
Use hashlib (built-in Python module)
Store:
    code -> url
    url -> code
    code -> click_count

'''

# FOR TESTING:

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"  # same as url1

# TODO: Uncomment after implementing methods
# code1 = shortener.shorten(url1)
# code2 = shortener.shorten(url2)
# code3 = shortener.shorten(url3)
# print("Codes:", code1, code2, code3)  # code1 and code3 should match
# print("Open code1:", shortener.open_url(code1))
# print("Open code1 again:", shortener.open_url(code1))
# print("Stats code1:", shortener.get_stats(code1))"""

import hashlib

class URLShortener:
    """
    Mini URL shortener.

    Stores:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int

    Collision rule:
    - If generated code already exists for another URL,
      generate a new one using an extra counter.
    """

    def __init__(self):
        # Initialize dictionaries
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        """Create a short code using MD5 hashing"""
        digest = hashlib.md5((url + extra).encode()).hexdigest()
        return digest[:6]  # take first 6 characters

    def shorten(self, url):
        """Return a short code for the URL"""
        # Return existing code if already shortened
        if url in self.url_to_code:
            return self.url_to_code[url]

        counter = 0
        while True:
            code = self._make_code(url, str(counter) if counter > 0 else "")
            # Collision check: code exists but for a different URL
            if code not in self.code_to_url:
                break
            elif self.code_to_url[code] == url:
                break
            else:
                counter += 1  # try a new code

        # Save mappings and initialize click count
        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0
        return code

    def open_url(self, code):
        """Return original URL and increase click count"""
        if code in self.code_to_url:
            self.click_counts[code] += 1
            return self.code_to_url[code]
        return None

    def get_stats(self, code):
        """Return dictionary with code, url, clicks"""
        if code in self.code_to_url:
            return {
                "code": code,
                "url": self.code_to_url[code],
                "clicks": self.click_counts[code]
            }
        return None


# ======= TESTING =======

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"  # same as url1

code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)

print("Codes:", code1, code2, code3)  # code1 and code3 should match

print("Open code1:", shortener.open_url(code1))
print("Open code1 again:", shortener.open_url(code1))
print("Stats code1:", shortener.get_stats(code1))