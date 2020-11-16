"""

IN: "Ala ma kota a kot ma Ale."
OUT: "A ma ma ala kot ale kota."

"""

def sort_words_in_sentence(string: str) -> str:
  # pozbyc sie kropki i zamienic litery na male
  # zamienic stringa na liste
  # sortowanie (hint: key)
  # dodac kropke, przygotowac semantyke zdania
  # polaczyc wszystkie slowa w stringa

  # string = string.lower()
  # string = string.strip('.')
  # string = string.lower().strip('.')
  words = string.lower().strip('.').split()
  words.sort(key=len)
  # words = sorted(words, key=len)
  # [4,1,7,3,9] 4 > 1
  # ['c', 'b', 'a'] 'c' > 'a'
  # [4,1,7,3,9] func(4) > func(1)
  # ['c', 'b', 'a'] len('c') > len('a')
  words[-1] += '.'
  words[0] = words[0].title()
  return ' '.join(words)


print(sort_words_in_sentence('Ala ma kota a kot ma Ale.'))
