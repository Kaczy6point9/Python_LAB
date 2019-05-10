import argparse
import random
import string
from itertools import count


def randomString(size):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(size))


def mutation(sentence):
    new_sentence = list(sentence)
    index = random.randrange(len(sentence))
    new_sentence[index] = random.choice(string.ascii_uppercase + ' ')

    return ''.join(new_sentence)


def weasel(target, init_sentence, num_copies):
    sentence_score = lambda sen: sum([1 for s, t in zip(sen, target) if s == t])
    best_sentnce = init_sentence
    best_score = sentence_score(best_sentnce)

    for n in count():
        sent = [best_sentnce] * num_copies
        for mut in map(mutation, sent):
            if mut == target:
                return mut

            score = sentence_score(mut)
            if score > best_score:
                best_sentnce = mut
                best_score = score
        print(n, best_sentnce)


parser = argparse.ArgumentParser(description='Argumenty wchodzace do symulacji')
parser.add_argument('--sentence', '-s', type=str, default='METHINKS IT IS LIKE A WEASEL')
parser.add_argument('--copies', '-c', type=int, default=100)
args = parser.parse_args()

target = args.sentence
num_copies = args.copies
sentence = randomString(len(target))
print(weasel(target, sentence, num_copies))
