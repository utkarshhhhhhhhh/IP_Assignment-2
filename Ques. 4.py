import random
def length_of_word(guess):
    if len(guess)==5:
        return guess
    else:
        print("Invalid word.")
    
List=["angry","awful","brave","basic","clean","close","crazy","daily","dirty","early","equal","fresh","funny","giant","great","happy","heavy","ideal","inner","joint","large","light","lucky","magic","nasty","other","outer","prime","proud","prior","quick","quiet","right","ready","royal","sharp","solid","spare","sweet","total","thick","urban","usual","usual","vague","vital","whole","wrong","young","zonal","zitty"]
random_word=List[random.randint(0,len(List)-1)]
k=0
tries=6
while k<6:
    guess=input()
    if not(length_of_word(guess)):
        continue
    if guess==random_word:
        print("Congrats! You have guessed the whole word correctly.The word was",random_word)
        break
    else:
        correct_places=""
        correct_alphabets=""
        for i in range(len(guess)):
            if guess[i]==random_word[i]:
                correct_places+=guess[i]
            else:
                correct_places+=("-")
            if guess[i] in random_word:
                correct_alphabets+=guess[i]
        print("Correct Alphabets in their correct places:",correct_places)
        print("Correct Alphabets:",correct_alphabets)
    k+=1
    if k==6:
        print("Oops. All your tries are over.The correct word is,",random_word) 
        
