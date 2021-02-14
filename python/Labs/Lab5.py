
import random, time

bottom = 1
top = 100
h = random.randint(bottom, top)
count = 0
###If you have ever played Apex Legends, I keep thinking of the machine as Pathfinder. haha
print("Hello will you play a game with me friend?")
time.sleep(1)
print("yes or no?")
answer = input()

if answer == 'yes':
    print("You only get 7 trys to guess the number im thinking of between 1 and 100 friend!")
    while count < 7:
        try:
            count += 1
            guess = int(input("Guess a number: "))
            if h == guess:
                print("Oh good job friend! You guessed my number in ",
                        count, " guesses.")
                break
            elif h > guess:
                print("Nope that number is too small, guess higher.")
            elif h < guess:
                print("Too big, guess lower.")
        except:
            print("Oh no friend.. you messed something up in such a simple game!" 
            " you must use an integer"
            " I am couting that as one of your guesses >:|")
                
    if count >= 7:
        print("The number I was thinking of was %s" % h)
        print("I hope you will try again friend!")

elif answer == 'no':
    print("Oh... Okay well have a nice day friend.")
else:
    print("Well if you can't give me a simple yes or no I don't want to play with you anyway! *angry robot noises*")