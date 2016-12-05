import random
import string

def randomString(size):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(size)) 

def stringmutation(sentence):
	new_senetence = list(sentence)
	index = random.randint(0, 27)
	new_senetence[index] = random.choice(string.ascii_uppercase + ' ')
	return ''.join(new_senetence)

def sen_score(score_sentence, sentences):
	score = len(score_sentence)
	max_score = 0
	best_sentence = sentences[0]

	for x in range(len(sentences)):
		sentence_score = 0
		pom1 = sentences[x]
		if pom1 == score_sentence:
			return pom1
		else:
			for y in range(len(pom1)):
				if pom1[y] == score_sentence[y]:
						sentence_score += 1
				if sentence_score > max_score:
					best_sentence = pom1
			
	return best_sentence


def weasel(score, sentence):
		
		sentences = []	
		for _ in range(100):
			sentences.append(sentence)
	
		mutations = []

		for x in range(len(sentences)):
			mutations.append(stringmutation(sentences[x]))

	 

sentence = randomString(28)
print(weasel('METHINKS IT IS LIKE A WEASEL', sentence))

