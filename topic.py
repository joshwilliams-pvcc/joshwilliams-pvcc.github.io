# Name: Josh Williams
# Prog Purpose: This program finds a random number for our C.E. Project topic
#   "A" means the topic number is available
#   "U" means the topic numbe ris unavailable (used)

import random
topics = []     #create an empty list to hold the topic codes
TOTAL_TOPICS = 5 # test this program with 5 topics before changing to 40

def main():
    num_used_topics = 0
    for i in range(TOTAL_TOPICS):# fill the list with items with an "A" in each one 
        topics.append("A")

    generate_another_randnumber = True #this boolean variable will control the outer loop
    continue_search = True #this boolean variable will control the inner loop

    while generate_another_randnumber: # OUTER LOOP
        continue_search = True

        while continue_search: #INNER LOOP
            randnumber = random.randint(0, TOTAL_TOPICS-1) #items in list started with 0, not 1
            if topics[randnumber] == "A":
                topics[randnumber] = "U"
                num_used_topics +=1
                continue_search = False

        print("\nRandom Topic Number: " + str(randnumber+1)) #items in list start with 0, so add 1
        print("List of topic availibility by number:")
        for i in range(TOTAL_TOPICS):
            print("\t" + str(i+1)+ ". " + topics[i])

        if num_used_topics == TOTAL_TOPICS:
            print("There are no more topics available at this time.")
            return() #quit the main() function
        else:
            answer = input("Would you like another random number? Y/N: ")
            if answer.upper() == "n" or answer.upper() == "N":
                generate_another_randnumber = False

main()


