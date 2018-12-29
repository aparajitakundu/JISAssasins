# question 12 done by aparajita kundu
def reverseword(s): 
   
   w = s.split(" ")        # Splitting the Sentence into list of words.
                           # reversing each word and creating a new list of words
                           # apply List Comprehension Technique
   nw = [i[::-1] for i in w]
                           # Join the new list of words to for a new Sentence
   ns = " ".join(nw)
   return ns
# Driver's Code 
s = input("ENTER A SENTENCE PROPERLY ::")
print(reverseword(s))
