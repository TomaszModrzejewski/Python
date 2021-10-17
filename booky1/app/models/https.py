def convert_to_https(url):
    """
    Replace the first instance of http:// in a string with https://
    """
    return url.replace("http://", "https://", 1)
