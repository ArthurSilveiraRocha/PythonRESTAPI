#print([n for n in range(11) if n % 2 == 1])

pessoas = ['Bun Da', 'M odr1 c', 'Po Br e', 'D ESEM PRE GADO', 'ch amiN e', 'do KA']

pessoas_normais = [pessoa.strip().capitalize() for pessoa in pessoas]

print(pessoas_normais)

words = ["alpha","omega","up","down","over","under","purple","red","blue","green"]
total = 0
for word in words:
    total += len(word)

print(total)