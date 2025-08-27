from pprint import pprint

names = open("names.txt", "r").read().split()

#<S> == start of name; <E> == end of name
#names = [['<S>'] + list(i) + ['<E>'] for i in names]

listvalue = {}

for i in names:
    names = ['<S>'] + list(i) + ['<E>']
    for char1, char2 in zip(names, names[1:]):
        bigram = (char1, char2)
        listvalue[bigram] = listvalue.get(bigram, 0) + 1

sorted_items = sorted(listvalue.items(), key=lambda x: x[1], reverse=True)

pprint(sorted_items)
