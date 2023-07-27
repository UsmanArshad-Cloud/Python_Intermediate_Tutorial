import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self,name,attrs):
        self.current = name
        if self.current == "book":
            print("___Book___")

    def characters(self, content):
        if self.current == "title":
            self.title = content
        elif self.current == "author":
            self.author = content
        elif self.current == "genre":
            self.genre = content
        else:
            self.published = content
    def endElement(self, name):
        if self.current == "title":
            print(f"Title is {self.title}")
        elif self.current == "author":
            print(f"Author is {self.author}")
        elif self.current == "genre":
            print(f"Genre is {self.genre}")
        elif self.current == "published":
            print(f"Published in {self.published}")
        self.current = ""

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('books.xml')