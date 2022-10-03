"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""


def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for _ in range(nbuckets)]


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        h = 0
        for char in o:
            h = h * 31 + ord(char)
        return h
    else:
        return None


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket_idx = hashcode(key) % len(table)

    for idx, data_item in enumerate(table[bucket_idx]):
        if data_item[0] == key:
            return idx

    return None


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """

    bucket_idx = hashcode(key) % len(table)
    idx = bucket_indexof(table, key)

    if idx is None:
        table[bucket_idx].append((key, value))
    else:
        # repalce
        table[bucket_idx][idx] = (key, value)


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    key_idx = bucket_indexof(table, key)

    if key_idx is None:
        return None

    bucket_idx = hashcode(key) % len(table)

    for data_item in table[bucket_idx]:
        if data_item[0] == key:
            return data_item[1]


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    output = ""
    new_line = "\n"
    arrow = "->"
    space = " "
    comma = ","

    for idx, bucket in enumerate(table):
        idx_padded = str(idx).rjust(4, '0')
        output += idx_padded

        if len(bucket) == 0:
            output += arrow + new_line
        else:
            output += arrow

            for idx_bucket, (k, v) in enumerate(bucket):
                k, v = str(k), str(v)
                if idx_bucket == len(bucket) - 1:
                    output += k + ":" + v
                    continue

                output += k + ":" + v + comma + space

            output += new_line

    return output


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    output = "{"

    for bucket in table:
        for k, v in bucket:
            output += str(k) + ":" + str(v) + ", "

    output = output.strip(", ")
    output += "}"

    return output
