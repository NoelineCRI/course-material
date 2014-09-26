# bencode / bdecode

Introduces: bytes.

Author(s): Julien Palard

## Instructions

Expose two functions `encode` and `decode`.

 + `encode` take one object as a parameter and return a `byte`.
 + `decode` take a `bytes` as a parameter and return an object.

objects may be of `type`:

 + `bytes`
 + `int`
 + `list`
 + `dict`

You have to follow the `bencode` encoding and decoding algorithm, see
[Wikipedia bencode page](http://en.wikipedia.org/wiki/Bencode).

## Hints

You may code other `helper` functions in your module,
functions to help `encode` and `decode` in their work. You also can
store module variables and use them, like in exercice 450, but only
for you to use.

You may want to not use any `str` nor any in this project, only
`bytes`, so I can use b'\x00' as a dictionary key !

## References
 - [bytes](https://docs.python.org/3.1/reference/lexical_analysis.html#strings)
