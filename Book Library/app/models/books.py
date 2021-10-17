from .search import google_book_search
from .https import convert_to_https


class Books():
    def __init__(self, query="", start=0, testing=False, https=False):
        if not testing:
            self.json = google_book_search(query, start)
        else:
            self.json = testing

        self.https = True if https else False

    def parse(self):
        """
        Takes the google books api and displays the results to the screen and returns
        an empty payload if there is an error
        """

        if self.json["status"] != 200:
            return empty_payload()

        body = self.json["body"]
        book_list = []

        try:
            for i in body["items"]:
                book = {}

                # checks the API responses for an existing data - and
                # adds an empty string if no data is returned from the API
                for field in ["authors", "title", "publisher", "imageLinks", "infoLink"]:
                    try:
                        book[field] = i["volumeInfo"][field]
                    except KeyError:
                        book[field] = ""

                book["authors"] = self._parse_authors(book["authors"])
                book["imageLinks"] = self._parse_thumbnail(book["imageLinks"])
                book_list.append(book)

        except KeyError:
            return empty_payload()

        return {"total": body["totalItems"], "items": book_list}

    def _parse_authors(self, authors_list=""):
        """
        Joins array of authors into comma-separated string
        """
        return ", ".join(authors_list)

    def _parse_thumbnail(self, imageLinks=""):
        """
        Adding own image if there is no image for book covers
        """
        if not imageLinks:
            return {"thumbnail": "static/images/booky-book.jpg"}
        else:
            if self.https:
                for link in imageLinks:
                    imageLinks[link] = convert_to_https(imageLinks[link])

            return imageLinks


def payload(items, total):
    return {"total": total, "items": items}


def empty_payload():
    return payload([], 0)
