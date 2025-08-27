names = open("names.txt", "r").read().split()

#<S> == start of name; <E> == end of name
names = [['<S>'] + list(i) + ['<E>'] for i in names]

print(names[:10])



#function bigrams()
