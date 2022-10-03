import os
import re
import string


def filelist(root):

    all_files = []

    for item in os.listdir(root):
        joined_path = os.path.join(root, item)
        item_path = os.path.abspath(joined_path)

        if os.path.isdir(item_path):
            all_files = all_files + filelist(item_path)

        elif os.path.isfile(item_path) and item.endswith('.txt'):
            all_files.append(item_path)

    return all_files


def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    # delete stuff but leave at least a space to avoid clumping together
    nopunct = regex.sub(" ", text)
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    ndocs = len(docs)
    docs = docs[0:100]  # at most 100 results
    terms = set(terms)
    body = ""
    for f in docs:
        lines = get_text(f).split("\n")
        summary = ""
        n = 0
        for line in lines:
            if n > 2:
                break  # show 2 lines at most
            line_words = words(line)
            if set(line_words).intersection(terms):
                for w in line_words:
                    summary += " "
                    if w in terms:
                        # summary += f"<font color=#41b6c4>{w}</font>"
                        summary += f"<b>{w}</b>"
                    else:
                        summary += w
                summary += "<br>"
                n += 1
        result = """
        <p><a href="file://%s">%s</a><br>
        %s<br>
        """ % (f, f, summary)
        body += result
    return """
    <html>
    <body>
    <h2>Search results for <b>%s</b> in %d files</h2>
    %s
    </body>
    </html>
    """ % (" ".join(terms), ndocs, body)
