"""Module for TextRank based document summarization."""
from collections import defaultdict
from collections.abc import MutableMapping


class DocumentGraph(MutableMapping):
    """Represents a graph of a document."""

    def __init__(self, text):
        """Initialize a document graph."""
        self.documentgraph = defaultdict(set)
        self.fulltext = text

    def __delitem__(self, key):
        """Delete from the DocumentGraph."""
        del self.documentgraph[key]

    def __getitem__(self, key):
        """Get a node from the DocumentGraph."""
        return self.documentgraph[key]

    def __setitem__(self, key, item):
        """Set a node for the Documentgraph."""
        self.documentgraph.add(item)


class DocumentSummarizer(object):
    """Class implementation of the TextRank algorithm.

    The paper describing the algorithm can be found at:

    https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
    """

    def __init__(self, N=4):
        """Create a TextRank summarization object.

        :N: The number of words to use to consider sentences linked.
        :returns: The TextRank instance.

        """
        super(DocumentSummarizer, self).__init__()
        self.N = N
