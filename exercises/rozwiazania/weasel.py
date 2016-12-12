import random
import string
import argparse

def randomString(size):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(size)) 

def stringmutation(sentence):
	new_sentence = list(sentence)
	#mutation_prob = 0.05
	index = random.randrange(len(sentence))
	##for x in range(len(sentence)):
		##if random.random() < mutation_prob:
	new_sentence[index] = random.choice(string.ascii_uppercase + ' ')
	
	return ''.join(new_sentence)


def sentence_score(sentence, final_sentence):
	sen_score=0	
	for x in range(len(final_sentence)):
		if sentence[x] == final_sentence[x]:
			sen_score += 1
	return(sen_score)


def weasel(score, sentence, copies):
		
		sentences = []	
		mutations = []
		ile = 0
		best_sentence = sentence
		best_score = sentence_score(sentence, score)
		while best_sentence != score:
			del sentences[:]
			del mutations[:]
			for _ in range(copies):
				sentences.append(best_sentence)

			for x in range(len(sentences)):
				mutations.append(stringmutation(sentences[x]))
			for x in range(len(mutations)):
				if sentence_score(mutations[x], score) > best_score:
					best_sentence = mutations[x]
					best_score = sentence_score(mutations[x], score)
			ile += 1
			print(ile)
			print(best_sentence)
		return best_sentence


parser = argparse.ArgumentParser(description='Argumenty wchodzace do symulacji')
parser.add_argument('--sentence', '-s', type=str, default='METHINKS IT IS LIKE A WEASEL') 
parser.add_argument('--copies', '-c', type=int, default=100)
args = parser.parse_args()

score =args.sentence
copies=args.copies
sentence = randomString(len(score))
print(weasel(score, sentence, copies))

