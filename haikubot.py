#Andrew LaFrance 2014
#HaikuBot - Program to randomly create haikus for the MSU StreetCar Journal
#Word Lists provided by ashley-bovan.co.uk

#import makehaiku
#print(makehaiku.haiku)
#print("By RAL")



import random

nouns1 = [line.strip() for line in open('dictionary\\nouns\\1syllablenouns.txt')]
nouns2 = [line.strip() for line in open('dictionary\\nouns\\2syllablenouns.txt')]
nouns3 = [line.strip() for line in open('dictionary\\nouns\\3syllablenouns.txt')]
nouns4 = [line.strip() for line in open('dictionary\\nouns\\4syllablenouns.txt')]

def noun1():
    return random.choice(nouns1)
def noun2():
    return random.choice(nouns2)
def noun3():
    return random.choice(nouns3)
def noun4():
    return random.choice(nouns4)

nouns = {1:noun1, 2:noun2, 3:noun3, 4:noun4}



verbs1 = [line.strip() for line in open('dictionary\\verbs\\1syllableverbs.txt')]
verbs2 = [line.strip() for line in open('dictionary\\verbs\\2syllableverbs.txt')]
verbs3 = [line.strip() for line in open('dictionary\\verbs\\3syllableverbs.txt')]
verbs4 = [line.strip() for line in open('dictionary\\verbs\\4syllableverbs.txt')]

def verb1():
    return random.choice(verbs1)
def verb2():
    return random.choice(verbs2)
def verb3():
    return random.choice(verbs3)
def verb4():
    return random.choice(verbs4)

verbs = {1:verb1, 2:verb2, 3:verb3, 4:verb4}



adjs1 = [line.strip() for line in open('dictionary\\adjectives\\1syllableadjectives.txt')]
adjs2 = [line.strip() for line in open('dictionary\\adjectives\\2syllableadjectives.txt')]
adjs3 = [line.strip() for line in open('dictionary\\adjectives\\3syllableadjectives.txt')]
adjs4 = [line.strip() for line in open('dictionary\\adjectives\\4syllableadjectives.txt')]

def adj1():
    return random.choice(adjs1)
def adj2():
    return random.choice(adjs2)
def adj3():
    return random.choice(adjs3)
def adj4():
    return random.choice(adjs4)

adjs = {1:adj1, 2:adj2, 3:adj3, 4:adj4}



adverbs1 = [line.strip() for line in open('dictionary\\adverbs\\1syllableadverbs.txt')]
adverbs2 = [line.strip() for line in open('dictionary\\adverbs\\2syllableadverbs.txt')]
adverbs3 = [line.strip() for line in open('dictionary\\adverbs\\3syllableadverbs.txt')]
adverbs4 = [line.strip() for line in open('dictionary\\adverbs\\4syllableadverbs.txt')]

def adverb1():
    return random.choice(adverbs1)
def adverb2():
    return random.choice(adverbs2)
def adverb3():
    return random.choice(adverbs3)
def adverb4():
    return random.choice(adverbs4)

adverbs = {1:adverb1, 2:adverb2, 3:adverb3, 4:adverb4}



preps1 = [line.strip() for line in open('dictionary\\prepositions\\1syllableprepositions.txt')]
preps2 = [line.strip() for line in open('dictionary\\prepositions\\2syllableprepositions.txt')]

def prep1():
    return random.choice(preps1)
def prep2():
    return random.choice(preps2)

preps = {1:prep1, 2:prep2}



#structure 1 = <adj><noun>
#structure 2 = {adj}<noun><Prep><noun>
#structure 3 = <verb><adverb>
#structure 4 = <adverb><verb>{adj}<noun>



def adjNoun(syll):
    print("adjNoun", syll)
    #TESTING
    first = random.randint(1,4)
    phrase = ""
    
    phrase += adjs[first]()
    phrase += " "
    phrase += nouns[random.randint(1,syll-first)]()
    return phrase

def nounPNoun(syll):
    print("nPN",syll)
    #TESTING
    adj = random.randint(0,2)
    syll -= adj
    first = random.randint(1,syll-2)
    syll -= first
    second = random.randint(1,syll-1)
    syll -= second
    phrase = ""
    
    if(adj != 0):  phrase = adjs[adj]() + " "
    phrase += nouns[first]()
    phrase += " "
    phrase += preps[second]()
    phrase += " "
    phrase += nouns[random.randint(1,syll)]()
    return phrase

phrase1 = {1:adjNoun,
           2:nounPNoun
           }

print(phrase1[random.randint(1,2)](5))    