import webbrowser
import sys
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results

class Htable():

    def __init__(self, rootdir):

        self.files = filelist(rootdir)
        N = len(self.files)
        print(f"{N} files to be indexed")
        self.index = myhtable_create_index(self.files)
        print(f"Index created...")

    def hashtable_search(self, terms):

        terms = words(terms)
        docs = myhtable_index_search(self.files, self.index, terms)
        page = results(docs, terms)

        with open("/tmp/results.html", "w", encoding='UTF-8') as f:
            f.write(page)

        webbrowser.open_new_tab("file:///tmp/results.html")


if __name__ == '__main__':
    path = "./slate"
    htable = Htable(path)
    while True:
        terms = input("Search terms: ")

        if terms == "end":
            break

        else:
            htable.hashtable_search(terms)
