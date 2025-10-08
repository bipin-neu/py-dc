from collections import Counter
#from .token_utils import tokenize

class Document:
  """Analyze text data
  :param text: text to analyze
  :ivar text: text originally passed to the instance on creation
  :ivar tokens: Parsed list of words from text
  :ivar word
  _
  counts: Counter containing counts of hashtags used in text
  """
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    #return tokenize(self.text)
    return (str(self.text).split())
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)
