#Andrew LaFrance 2014
#HaikuBot - Program to randomly create haikus for the MSU StreetCar Journal
#Word Lists provided by ashley-bovan.co.uk

import random

nouns1 = [line.strip() for line in open('dictionary\\nouns\\1syllablenouns.txt')]
nouns2 = [line.strip() for line in open('dictionary\\nouns\\2syllablenouns.txt')]
nouns3 = [line.strip() for line in open('dictionary\\nouns\\3syllablenouns.txt')]
nouns4 = [line.strip() for line in open('dictionary\\nouns\\4syllablenouns.txt')]

verbs1 = [line.strip() for line in open('dictionary\\verbs\\1syllableverbs.txt')]
verbs2 = [line.strip() for line in open('dictionary\\verbs\\2syllableverbs.txt')]
verbs3 = [line.strip() for line in open('dictionary\\verbs\\3syllableverbs.txt')]
verbs4 = [line.strip() for line in open('dictionary\\verbs\\4syllableverbs.txt')]

adjs1 = [line.strip() for line in open('dictionary\\adjectives\\1syllableadjectives.txt')]
adjs2 = [line.strip() for line in open('dictionary\\adjectives\\2syllableadjectives.txt')]
adjs3 = [line.strip() for line in open('dictionary\\adjectives\\3syllableadjectives.txt')]
adjs4 = [line.strip() for line in open('dictionary\\adjectives\\4syllableadjectives.txt')]

adverbs1 = [line.strip() for line in open('dictionary\\adverbs\\1syllableadverbs.txt')]
adverbs2 = [line.strip() for line in open('dictionary\\adverbs\\2syllableadverbs.txt')]
adverbs3 = [line.strip() for line in open('dictionary\\adverbs\\3syllableadverbs.txt')]
adverbs4 = [line.strip() for line in open('dictionary\\adverbs\\4syllableadverbs.txt')]

preps1 = [line.strip() for line in open('dictionary\\prepositions\\1syllableprepositions.txt')]
preps2 = [line.strip() for line in open('dictionary\\prepositions\\2syllableprepositions.txt')]
compPreps = [line.strip() for line in open('dictionary\\prepositions\\compoundprepositions.txt')]


#Phrase1 structure 1 = <adj><noun>
#Phrase1 structure 2 = <noun 1/2><compPrep><noun 2/1>
#Phrase1 structure 3 = <adj><noun><prep1/2><noun2/1>