'''Write a program to compute the frequency of the words from the input.
   The output should output after sorting the key alphanumerically.
line = “which is better python 2 or python 3”
Output = ('2',1)
        ('3',1)
        ('better',1)
        ('is',1)
        ('or',1)
        ('python',2)
        ('which',1)
        '''
def count_word(line):
    d = {}
    for word in line.split():
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


def sort_words(d):
    words = list(d.keys())
    for i in range(len(words)):
        for j in range(0, len(words)-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
    
    sw_freq = [(word, d[word]) for word in words]

    for item in sw_freq:
        print(item)
    return sw_freq


def word_count_sort(line):
    d = count_word(line)
    return sort_words(d)

line = "which is better python 2 or python 3"
word_count_sort(line)