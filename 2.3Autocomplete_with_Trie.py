

# # >>> t = trie(an=0, ant=1, all=2, allot=3, alloy=4, aloe=5, are=6, be=7)
# # >>> t
# # SortedStringTrie({'all': 2, 'allot': 3, 'alloy': 4, 'aloe': 5, 'an': 0, 'ant': 1, 'are': 6, 'be': 7})
# # >>> t.keys(prefix='al')
# # ['all', 'allot', 'alloy', 'aloe']
# # >>> t.items(prefix='an')
# # [('an', 0), ('ant', 1)]
# # >>> t.longest_prefix('antonym')
# # 'ant'
# # >>> t.longest_prefix_item('allstar')
# # ('all', 2)
# # >>> t.longest_prefix_value('area', default='N/A')
# # 6
# # >>> t.longest_prefix('alsa')
# # Traceback (most recent call last):
# #     ...
# # KeyError
# # >>> t.longest_prefix_value('alsa', default=-1)
# # -1
# # >>> list(t.iter_prefixes('allotment'))
# # ['all', 'allot']
# # >>> list(t.iter_prefix_items('antonym'))
# # [('an', 0), ('ant', 1)]
#
#
# '''
# def keys(self, prefix=None):
#     Return a list of this trie's keys.
#
#     :param prefix: If not None, return only the keys prefixed by ``prefix``.
#
#     return list(self.iterkeys(prefix))
#
#
#
#
#     def iterkeys(self, prefix=None):
#         '''Return an iterator over this tries keys.
#
#         :param prefix: If not None, yield only the keys prefixed by ``prefix``.
#         '''
#         return (key for key,value in self.iteritems(prefix))
# '''
#
#
#
# t = trie(an=0, ant=1, all=2, allot=3, alloy=4,aloe=5,are=6,be=7)
# print t.keys(prefix='al')


import sys


_end = '_end_'


def create_dictionary_trie_from_corpus():
    corpus_file = open('./words.txt','r')
    corpus_file_read = corpus_file.read()

    words = corpus_file_read.split()
    trie_root = dict()

    for word in words:
        # a dict
        current_node = trie_root
        for letter in word:
            # setdefault creates the format of the dictionary
            current_node = current_node.setdefault(letter, {})
            # the end of the dictioary will be the end node of the trie
        current_node[_end] = _end
        corpus_file.close()
        return trie_root

def search_trie(trie, prefix):
    current_node = trie
    for letter in prefix:
        if letter in current_node:
            current_node = current_node[letter]
        else:
            return False

def autocomplete(trie, prefix):
    current_node = trie
    for letter in prefix:
        if letter in current_node:
            current_node = current_node[letter]
        else:
            return False

    print(current_node,prefix)

def print_trie(trie, prefix):
    current_node = trie
    word = prefix
    for key in current_node:
        if key == _end:
            print str(word)
        else:
            word = prefix + key
            print_trie(current_node[key], word)

tree = create_dictionary_trie_from_corpus()
search_trie(tree, "Hel")
print_trie()

# create_dictionary_trie_from_corpus()
