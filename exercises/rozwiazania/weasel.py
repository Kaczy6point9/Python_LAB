import random
import string

def randomString(size):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(size)) 

def stringmutation(sentence):
	new_sentence = list(sentence)
	mutation_prob = 0.09
	##index = random.randrange(len(sentence))
	for x in range(len(sentence)):
		if random.random() < mutation_prob:
			new_sentence[x] = random.choice(string.ascii_uppercase + ' ')
	
	return ''.join(new_sentence)

def sen_score(final_sentence, sentences):
	max_score = 0
	best_sentence = sentences[0]
	

	for x in range(len(sentences)):
		pom1 = sentences[x]
		if pom1 == final_sentence:
			return pom1
		else:
			sentence_score = 0
			for y in range (len(final_sentence)):
				if pom1[y] == final_sentence[y]:
						sentence_score += 1
			if sentence_score > max_score:
				best_sentence = pom1
	
	print(sentence_score)
	print(best_sentence)		
	return best_sentence


def weasel(score, sentence):
		
		sentences = []	
		for _ in range(100):
			sentences.append(sentence)
	
		mutations = []
		ile = 0
		for x in range(len(sentences)):
			mutations.append(stringmutation(sentences[x]))

		best_sentence = sen_score(score, mutations)
		while best_sentence != score:
			del sentences[:]
			del mutations[:]
			for _ in range(100):
				sentences.append(best_sentence)

			for x in range(len(sentences)):
				mutations.append(stringmutation(sentences[x]))
			best_sentence = sen_score(score, mutations)
			ile += 1
			print(ile)
		return best_sentence

score ='METHINKS IT IS LIKE A WEASEL'
sentence = randomString(len(score))
print(weasel(score, sentence))

