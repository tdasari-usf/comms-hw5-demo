# HashTables

Team - Ben Chen, Jessica Wang, Tejaswi Samrat Dasari.

**HashTables** 

Hash Tables, also known as hashmaps, is a data structure that implements the storage of data in key value pairs. It uses a hash function to calculate an index which is also called hashcode. With the help of the index, data(values) are stored into an array of buckets. The hashcode determines which bucket the values fall into. At the time of lookup, the hashcode is calculated to retrieve the corresponding value.

Hashtables are extensively used for their faster retrievability. On average the time complexity of a hashtable is O(1). Ideally a hash function should  associate each value to a distinct key, but in cases where that is not possible a “collision” is caused. Collisions are handled using two techniques. The first one is open addressing, and the second is called Chaining.

Diagramatical view of hashtable

![Alt text](./images/img.png?raw=true "Title")


#### Implementation of HashTable: 

We implemented a hashtable to retrieve the files containting given terms(words) from a dataset of raw txt files.

To run a demo:

```
python demo.py
```

You can enter the terms you would like to look up in the data set, after which the hashtable gets created, and then directed to a html
containing the terms, and filenames.


#### Conclusion:

In many situations, hash tables turn out to be more efficient than search trees or any other table lookup structure. For this reason, they are widely used in many kinds of computer softwares, particularly for associative arrays, database indexing, caches and sets.
