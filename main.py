# import modules
from time import sleep
import random as r
from sys import stdout


# declare variables
sentence_pause = 0
letter_pause = 0.2
characters = ''
choice = ''
pointer = ''
temp = ''

# create a player class for OOP
class Player:
    def __init__(self, name='Tim', health=3):
        self.name = name
        self.health = health

    def remove_health(self):
        self.health -= 1
        return self.health

    def reset_health(self):
        self.health = 3


# checks health points
def check_health(player):
    if player.health == 0:
        dead()
    return True


# method to slowly print characters
def print_characters(characters):
    for char in characters:
        stdout.write(char)
        stdout.flush()
        sleep(letter_pause)


# all it does is print dead
def dead():
    print("YOU ARE DE DE DE DEAD!")
    print("GAME OVER TRY AGAIN")


# method to display intro
def intro():
    print('You are sitting in your dark, cold and damp basement. You can hear the soft pattering of rain and the')
    sleep(sentence_pause)
    print('clicks of your keyboard keys. Staring into the screen, you close all of your social media tabs,')
    sleep(sentence_pause)
    print('closed a kind-of sketchy website called BuyThis, and all the games you downloaded and finally your')
    sleep(sentence_pause)
    print('hacking platform. Just as you were about to Google "Funny Memes" to finish off your night when suddenly')
    sleep(sentence_pause)
    print('an ad flashes onto your screen. This is what you have been looking for your whole life - THE AD, the')
    sleep(sentence_pause)
    print('game where the best of the best gamers battle it out for the ultimate glory. You\'ve never seen a single')
    sleep(sentence_pause)
    print('picture, review or anything about this game other that its name and how hard it is to come across.')
    sleep(sentence_pause)
    print('Engulfed by happiness, you immediately click on the screen. Suddenly your screen brightens, the basement')
    sleep(sentence_pause)
    print('starts to shake, you cat shrieks and runs away and your body seems to be dissolving into the')
    sleep(sentence_pause)
    print('computer screen.........')
    print()
    print()


# Casey's room
def room1():
    pointer = ''
    print('You\'re lying on the floor, your stomach feels sick and your vision is blurry. As you stand up, you feel')
    sleep(sentence_pause)
    print('normal again. You look up and notice 3 hearts above your head. What is this and where am I? It feels like')
    sleep(sentence_pause)
    print('something out of a video game. As your eyes un-blur, you notice you are in your year 7 coding classroom.')
    sleep(sentence_pause)
    print('This is where it all began. Your love of computers, coding and a little hacking. You notice there are only')
    sleep(sentence_pause)
    print('2 people in the class. It\'s your year 7 coding teacher, Miss Whack, and a student who looks like one of')
    sleep(sentence_pause)
    print('your old classmates, Billy. At the exact same time (which is a little creepy), they say, "Talk to me..."')
    print()
    response = input('Who do you talk to? (Miss Whack/Billy) ').strip().lower()
    if response == "miss whack":
        print('You go over to talk to Miss Whack. You notice she was about to fall for a scam. Which read "Are')
        sleep(sentence_pause)
        print('you sick of your boring job, well you don\'t need ot be anymore because if you just give us some')
        sleep(sentence_pause)
        print('information you can win a bunch of money by Tim Secure.')
        sleep(sentence_pause)
        temp = 'Hmm why my is my name on it? I wouldn\'t something like that. '
        print_characters(temp)
        answer = input('Do you warn her about the Scam? Y/N').strip().lower()
        if answer == 'y':
            print('You tell successfully warned her of the scam, she gives you a key to open the door, and you')
            print('into a dark and gloomy room.')
        elif answer == 'n':
            print(f'Teacher got frustrated and threw the laptop, it bounced off the wall flying towards your head.')
            print(f'You copped a decent whack you now have %d points left!' % player.remove_health())
        else:
            print('Invalid input')
            pointer = 'exit'
    elif response == "billy":
        print()
        answer = input('Billy runs at you with a pencil! What do you do? Offer a Sharpener?(O) or Duck?(D) ').strip().lower()
        if answer == 'o':
            print(f'Billy has stabbed you! you now have %d points left!' % player.remove_health())
        elif answer == 'd':
            print('You duck and dodge Billy, flailing your arms all over the joint around the room, you finally')
            sleep(sentence_pause)
            print('manage to crawl over to Miss Whack. You notice she was about to fall for a scam. Which read "Are')
            sleep(sentence_pause)
            print('you sick of your boring job, well you don\'t need ot be anymore because if you just give us some')
            sleep(sentence_pause)
            print('information you can win a bunch of money by Tim Secure.')
            sleep(sentence_pause)
            temp = 'Hmm why my is my name on it? I wouldn\'t something like that. '
            print_characters(temp)
            answer = input('Do you warn her about the Scam? Y/N').strip().lower()
            if answer == 'y':
                print('You tell successfully warned her of the scam, she gives you a key to open the door, and you')
                print('into a dark and gloomy room.')
            elif answer == 'n':
                print(f'Teacher got frustrated and threw the laptop, it bounced off the wall flying towards your head.')
                print(f'You copped a decent whack you now have %d points left!' % player.remove_health())
            else:
                print('Invalid input')
                pointer = 'exit'
    else:
        print('Invalid input')
        pointer = 'exit'
    return pointer


# method to display game banner
def display_banner():
    print()
    print()
    print('************************')
    print('*                      *')
    print('*       The AD         *')
    print('*                      *')
    print('************************')
    print()
    print()


player = Player('Tim', 3)


# main block for programming codey

def main():
    # # reset health
    # player.reset_health()
    while True:
        display_banner()
        answer = input('Welcome to The AD. Do you want to play? (Y/N) ').strip().lower()
        print()
        # main component of game tree
        if answer == 'y':
            name = input('What is your name? ')
            player = Player(name, 3)
            print(f"Welcome %s you have %s health points.\n" % (player.name, player.health))
            intro()
            pointer = room1()
            if pointer == 'exit':
                break
        elif answer == 'n':
            break
        else:
            print('Invalid input')
            break
    print('hit end of while')


if __name__ == '__main__':
    main()


