# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from hashtable.htable import *
from hashtable.words import get_text, words, filelist


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    index = htable(4011)

    for file_idx, file in enumerate(files):

        terms = words(get_text(file))
        for term in terms:
            term_files = htable_get(index, term)
            if term_files is None:
                htable_put(index, term, {file_idx})
            else:
                term_files.add(file_idx)

    return index


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """

    if len(terms) < 1:
        return []
    file_idxes = htable_get(index, terms[0])

    if file_idxes is None:
        return []

    for term in terms:
        term_set = htable_get(index, term)
        if term_set is None:
            return []
        file_idxes = file_idxes.intersection(term_set)

    return [file for idx, file in enumerate(files) if idx in file_idxes]
