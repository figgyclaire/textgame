# import modules
from time import sleep
import random as r
from sys import stdout

# declare variables
sentence_pause = 2
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
        exit()
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


# Casey's room
def room1():
    # setup something to return
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
        print()
        sleep(sentence_pause)
        temp = 'Hmm why my is my name on it? I wouldn\'t something like that. '
        print_characters(temp)
        answer = input('Do you warn her about the Scam? Y/N ').strip().lower()
        if answer == 'y':
            print()
            print('You tell successfully warned her of the scam, she gives you a key to open the door.')
        elif answer == 'n':
            print()
            print(f'The teacher got frustrated and threw the laptop, it bounced off the wall flying towards your head.')
            print(f'You copped a decent whack you now have %d health points left!' % player.remove_health())
            check_health(player)
            print()
        else:
            print('Invalid input')
            pointer = 'exit'
    elif response == "billy":
        print()
        answer = input(
            'Billy runs at you with a pencil! What do you do? Offer a Sharpener?(O) or Duck?(D) ').strip().lower()
        print()
        if answer == 'o':
            print(f'Billy has stabbed you! you now have %d health points left!' % player.remove_health())
            print()
            check_health(player)
        elif answer == 'd':
            print('You duck and dodge Billy, flailing your arms all over the joint around the room, you finally')
            sleep(sentence_pause)
            print('manage to crawl over to Miss Whack. You notice she was about to fall for a scam. Which read "Are')
            sleep(sentence_pause)
            print('you sick of your boring job, well you don\'t need ot be anymore because if you just give us some')
            sleep(sentence_pause)
            print('information you can win a bunch of money by Tim Secure.')
            print()
            sleep(sentence_pause)
            temp = 'Hmm why my is my name on it? I wouldn\'t something like that. '
            print_characters(temp)
            answer = input('Do you warn her about the Scam? Y/N ').strip().lower()
            if answer == 'y':
                print()
                print('You tell successfully warned her of the scam, she gives you a key to open the door.')
            elif answer == 'n':
                print('Teacher got frustrated and threw the laptop, it bounced off the wall flying towards your head.')
                print(f'You copped a decent whack you now have %d points left!' % player.remove_health())
                check_health(player)
            else:
                print('Invalid input')
                pointer = 'exit'
    else:
        print('Invalid input')
        pointer = 'exit'
    return pointer


# Yash's room
def room2():
    # setup something to return
    pointer = ''
    print('You step into a dark, gloomy room with only one dull light hanging from the ceiling. You notice that you')
    sleep(sentence_pause)
    print(f'now have %d hearts above your head again. As you start to look around, you see lots of blobs floating' % player.health)
    sleep(sentence_pause)
    print('mysteriously in the air. They are an unusual green and yellow in colour and their shape feels familiar.')
    sleep(sentence_pause)
    print('However, you can\'t identify what they are. You get goosebumps on your arms and start to feel scared, so')
    sleep(sentence_pause)
    print('you slowly tremble towards the door on the other side of the room. Ah yes - you think to yourself, those')
    sleep(sentence_pause)
    print('blobs are in fact viruses! Standing in awe of these mysterious viruses, you realise that the viruses are')
    sleep(sentence_pause)
    print('slowly floating towards you. You try to run away, but your legs are frozen to the floor. Suddenly, one of')
    sleep(sentence_pause)
    print('the viruses has inched itself closer towards you, almost at eye level, and it asks you a question in a')
    sleep(sentence_pause)
    print('glitchy, sniffly voice.')
    print()
    response = input('Should you install something off a website that you feel is not secure? (Y/N) ').strip().lower()
    if response == 'y':
        print()
        print('The virus you have downloaded caused the computer lose data, and you lost all of your group assignment.')
        sleep(sentence_pause)
        print('work and now your friends are very disappointed. You take 1 point of emotional damage.')
        sleep(sentence_pause)
        print(f'You now have %d health points left!' % player.remove_health())
        sleep(sentence_pause)
        check_health(player)
        print('Feeling slightly hurt, you manage to pull yourself together and move on to the next virus.')
        sleep(sentence_pause)
        print()
        answer = input('It asks you: Should you post personal data online? (Y/N) ')
        if answer == 'y':
            print()
            print('Someone has found all your dress up baby photos on your social media account and has shared it.')
            sleep(sentence_pause)
            print('You take 1 point of extreme embarrassment damage.')
            sleep(sentence_pause)
            print(f'You now have %d health points left!' % player.remove_health())
            check_health(player)
        elif answer == 'n':
            print()
            print('The virus self destructs somehow. Your now seriously amazed about how the viruses are doing this.')
            sleep(sentence_pause)
            print('You move on to the final virus, it asks you -')
            sleep(sentence_pause)
            answer = input('Is it safe to accept random friend requests? (Y/N ')
        else:
            print('Invalid input')
            pointer = 'exit'
    elif response == 'n':
        print()
        print('The virus self destructs somehow. Amazed you slowly advance to the next virus who asks you another')
        sleep(sentence_pause)
        print('question in a voice that reminds you of someone who has a flu.')
        sleep(sentence_pause)
        print()
        answer = input('Should you post personal data online? (Y/N) ')
        if answer == 'y':
            print()
            print('Someone has found all your dress up baby photos on your social media account and has shared it.')
            sleep(sentence_pause)
            print('You take 1 point of extreme embarrassment damage.')
            sleep(sentence_pause)
            print(f'You now have %d health points left!' % player.remove_health())
            check_health(player)
        elif answer == 'n':
            print()
            print('The virus self destructs somehow. Your now seriously amazed about how the viruses are doing this.')
            sleep(sentence_pause)
            print('You move on to the final virus, it asks you -')
            sleep(sentence_pause)
            print()
            answer = input('Is it safe to accept random friend requests? (Y/N) ')
            if answer == 'y':
                print()
                print('You added a new friend, he befriends you and convinces you to send them all your money.')
                sleep(sentence_pause)
                print('You take 1 point of having no money damage')
                sleep(sentence_pause)
                print(f'You now have %d health points left!' % player.remove_health())
                sleep(sentence_pause)
                check_health(player)
            elif answer == 'n':
                print()
                print('You get a key to the door at the end of the room. You put it through the keyhole and open the')
                sleep(sentence_pause)
                print('door, only to realise it leads you to a blue tube, almost like a high slide. Uneasy, you turn')
                sleep(sentence_pause)
                print('back towards the room you had just left, when suddenly the viruses that didn\'t ask you a ')
                sleep(sentence_pause)
                print('question pushes you down the slide.')
                sleep(sentence_pause)
            else:
                print()
                print('Invalid input')
                pointer = 'exit'
    else:
        print('Invalid input')
        pointer = 'exit'
    return pointer


# Kadie's room
def room3():
    # setup something to return
    pointer=''
    print()
    print('You slide out of the tunnel, dazed and confused to your left you see a lantern, but to the right, a long')
    sleep(sentence_pause)
    print('dark corridor awaits you.')
    sleep(sentence_pause)
    print()
    response = input('Do you want to do want to go left or right? (left/right) ').strip().lower()
    if response == 'left' or response == 'l':
        print()
        print('You grab the lantern, it suddenly lights - scaring you. You look around only to see the room is made')
        sleep(sentence_pause)
        print('from cold, dark walls unlike the other interesting levels you have passed. Your only choice is to go')
        sleep(sentence_pause)
        print('right through the corridor.')
        sleep(sentence_pause)
        print()
        print('Your lantern illuminates the corridor, revealing wires lining the roof. Confused , you continue until')
        sleep(sentence_pause)
        print('you stumble onto something .. maybe a wire? until suddenly the wires on top of the roof illuminates')
        sleep(sentence_pause)
        print('revealing stunning neon lights that will guide you through the tunnel. When you reach the end of the')
        sleep(sentence_pause)
        print('tunnel, you come to another dark room. You reach for your lantern, but it won\'t turn on and suddenly')
        sleep(sentence_pause)
        print('it disappears into thin air. Standing in the dark, you carefully and slowly walk forward, reaching out')
        sleep(sentence_pause)
        print('to ensure you don\'t crash into anything.')
        print()
        answer = input('Look for a light switch or walk around the room? (look/walk) ')
        if answer == 'look' or answer == 'l':
            print()
            print('You travel alongside the edge of the room, feeling the wall in search of a light switch. When you')
            sleep(sentence_pause)
            print('get back to the doorway where you entered, you discovered there is no light switch. You only choice')
            sleep(sentence_pause)
            print('now is to look around the room.')
            sleep(sentence_pause)
            print('You walk around slowly, with outstretched arms, until suddenly you feel something in the middle of')
            sleep(sentence_pause)
            print('the room. It feels like a pedestal, with a large button on top.')
            sleep(sentence_pause)
            print()
            print('You decide to press the button. Large bright rectangles appear to be floating in the air. No that')
            sleep(sentence_pause)
            print('can\'t be right you think to your self, and blink several times in confusion, allowing you eyes to')
            sleep(sentence_pause)
            print('adjust. When everything is clearer, you realise the floating rectangles are your posts, searches,')
            sleep(sentence_pause)
            print('passwords and PERSONAL INFORMATION!?!??!??!')
            sleep(sentence_pause)
            print()
            print('One of the floating rectangles flies towards you. You see a question with a button for YES and NO')
            sleep(sentence_pause)
            print('You inspect closer and it says: ')
            sleep(sentence_pause)
            print()
            answer = input('Is it ok to post personal info to people that you don\'t know? (Y/N) ').strip().lower()
            if answer == 'y' or answer == 'yes':
                print()
                print('You gave a guy named Steve all your details, and he has now changed your identity to Steve')
                sleep(sentence_pause)
                print('You take 1 point for not legally existing')
                sleep(sentence_pause)
                print(f'You now have %d health points left!' % player.remove_health())
                check_health(player)
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                print()
            elif answer == 'n' or answer == 'no':
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    check_health(player)
                    print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input('Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
            else:
                print()
                print('Invalid input')
                pointer = 'exit'
        elif answer == 'walk' or answer == 'w':
            print()
            print('You walk around slowly, with outstretched arms, until suddenly you feel something in the middle of')
            sleep(sentence_pause)
            print('the room. It feels like a pedestal, with a large button on top.')
            sleep(sentence_pause)
            print()
            print('You decide to press the button. Large bright rectangles appear to be floating in the air. No that')
            sleep(sentence_pause)
            print('can\'t be right you think to your self, and blink several times in confusion, allowing you eyes to')
            sleep(sentence_pause)
            print('adjust. When everything is clearer, you realise the floating rectangles are your posts, searches,')
            sleep(sentence_pause)
            print('passwords and PERSONAL INFORMATION!?!??!??!')
            sleep(sentence_pause)
            print()
            print('One of the floating rectangles flies towards you. You see a question with a button for YES and NO')
            sleep(sentence_pause)
            print('You inspect closer and it says: ')
            sleep(sentence_pause)
            print()
            answer = input('Is it ok to post personal info to people that you don\'t know? (Y/N) ').strip().lower()
            if answer == 'y' or answer == 'yes':
                print()
                print('You gave a guy named Steve all your details, and he has now changed your identity to Steve')
                sleep(sentence_pause)
                print('You take 1 point for not legally existing')
                sleep(sentence_pause)
                print(f'You now have %d health points left!' % player.remove_health())
                sleep(sentence_pause)
                check_health(player)
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                print()
            elif answer == 'n' or answer == 'no':
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
            else:
                print()
                print('Invalid input')
                pointer = 'exit'
        else:
            print('Invalid input')
            pointer = 'exit'
    elif response == 'right' or response == 'r':
        print()
        print('You stumble around aimlessly through the dark corridor, but turn back to get the lantern, regretting')
        sleep(sentence_pause)
        print('your decision. When you pick up the lantern, it suddenly lights - scaring you. You look around only')
        sleep(sentence_pause)
        print('to see the room is made from cold, dark walls, unlike the other interesting levels you have passed.')
        sleep(sentence_pause)
        print('Your only choice now is to continue through the corridor.')
        sleep(sentence_pause)
        print()
        print('Your lantern illuminates the corridor, revealing wires lining the roof. Confused , you continue until')
        sleep(sentence_pause)
        print('you stumble onto something .. maybe a wire? until suddenly the wires on top of the roof illuminates')
        sleep(sentence_pause)
        print('revealing stunning neon lights that will guide you through the tunnel. When you reach the end of the')
        sleep(sentence_pause)
        print('tunnel, you come to another dark room. You reach for your lantern, but it won\'t turn on and suddenly')
        sleep(sentence_pause)
        print('it disappears into thin air. Standing in the dark, you carefully and slowly walk forward, reaching out')
        sleep(sentence_pause)
        print('to ensure you don\'t crash into anything.')
        sleep(sentence_pause)
        print()
        answer = input('Look for a light switch or walk around the room? (look/walk) ')
        if answer == 'look' or answer == 'l':
            print()
            print('You travel alongside the edge of the room, feeling the wall in search of a light switch. When you')
            sleep(sentence_pause)
            print('get back to the doorway where you entered, you discovered there is no light switch. You only choice')
            sleep(sentence_pause)
            print('now is to look around the room.')
            sleep(sentence_pause)
            print('You walk around slowly, with outstretched arms, until suddenly you feel something in the middle of')
            sleep(sentence_pause)
            print('the room. It feels like a pedestal, with a large button on top.')
            sleep(sentence_pause)
            print()
            print('You decide to press the button. Large bright rectangles appear to be floating in the air. No that')
            sleep(sentence_pause)
            print('can\'t be right you think to your self, and blink several times in confusion, allowing you eyes to')
            sleep(sentence_pause)
            print('adjust. When everything is clearer, you realise the floating rectangles are your posts, searches,')
            sleep(sentence_pause)
            print('passwords and PERSONAL INFORMATION!?!??!??!')
            sleep(sentence_pause)
            print()
            print('One of the floating rectangles flies towards you. You see a question with a button for YES and NO')
            sleep(sentence_pause)
            print('You inspect closer and it says: ')
            sleep(sentence_pause)
            print()
            answer = input('Is it ok to post personal info to people that you don\'t know? (Y/N) ').strip().lower()
            if answer == 'y' or answer == 'yes':
                print()
                print('You gave a guy named Steve all your details, and he has now changed your identity to Steve')
                sleep(sentence_pause)
                print('You take 1 point for not legally existing')
                sleep(sentence_pause)
                print(f'You now have %d health points left!' % player.remove_health())
                sleep(sentence_pause)
                check_health(player)
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                print()
            elif answer == 'n' or answer == 'no':
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
            else:
                print()
                print('Invalid input')
                pointer = 'exit'
        elif answer == 'walk' or answer == 'w':
            print()
            print('You walk around slowly, with outstretched arms, until suddenly you feel something in the middle of')
            sleep(sentence_pause)
            print('the room. It feels like a pedestal, with a large button on top.')
            sleep(sentence_pause)
            print()
            print('You decide to press the button. Large bright rectangles appear to be floating in the air. No that')
            sleep(sentence_pause)
            print('can\'t be right you think to your self, and blink several times in confusion, allowing you eyes to')
            sleep(sentence_pause)
            print('adjust. When everything is clearer, you realise the floating rectangles are your posts, searches,')
            sleep(sentence_pause)
            print('passwords and PERSONAL INFORMATION!?!??!??!')
            sleep(sentence_pause)
            print()
            print('One of the floating rectangles flies towards you. You see a question with a button for YES and NO')
            sleep(sentence_pause)
            print('You inspect closer and it says: ')
            sleep(sentence_pause)
            print()
            answer = input('Is it ok to post personal info to people that you don\'t know? (Y/N) ').strip().lower()
            if answer == 'y' or answer == 'yes':
                print()
                print('You gave a guy named Steve all your details, and he has now changed your identity to Steve')
                sleep(sentence_pause)
                print('You take 1 point for not legally existing')
                sleep(sentence_pause)
                print(f'You now have %d health points left!' % player.remove_health())
                sleep(sentence_pause)
                check_health(player)
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
                print()
            elif answer == 'n' or answer == 'no':
                print()
                print('Suddenly the rectangles around the room fade away, revealing the door at the other side of the')
                sleep(sentence_pause)
                print('room. You try to walk towards it, but you are blocked again by the floating rectangles and')
                sleep(sentence_pause)
                print('realise you can only pass if you answer more questions correctly. Another rectangle flies by')
                sleep(sentence_pause)
                print('with a question ...')
                sleep(sentence_pause)
                print()
                answer = input('Should you share passwords with other people? (Y/N) ').strip().lower()
                if answer == 'y' or answer == 'yes':
                    print()
                    print('Your friends hacked your accounts and have changed your display name to something funny.')
                    sleep(sentence_pause)
                    print('You lose a health point.')
                    sleep(sentence_pause)
                    print(f'You now have %d health points left!' % player.remove_health())
                    sleep(sentence_pause)
                    check_health(player)
                    print()
                elif answer == 'n' or answer == 'no':
                    print()
                    print('More rectangles disappear, the door is becoming clearer ... one more rectangle approaches.')
                    sleep(sentence_pause)
                    print()
                    answer = input(
                        'Do you promise that you will no longer share private information? (Y/N) ').strip().lower()
                    if answer == 'y' or answer == 'yes':
                        print()
                        print('All the rectangles disappear. You open the door using the key that has spawned into')
                        sleep(sentence_pause)
                        print('your hand and descend into the darkness')
                        sleep(sentence_pause)
                        print()
                    elif answer == 'n' or answer == 'no':
                        print()
                        print('You hear a static noise building up. A flash of lightning emitting from the rectangle')
                        sleep(sentence_pause)
                        print('strikes out and hits you. You lose a health point.')
                        sleep(sentence_pause)
                        print(f'You now have %d health points left!' % player.remove_health())
                        sleep(sentence_pause)
                        check_health(player)
                        print()
            else:
                print()
                print('Invalid input')
                pointer = 'exit'
        else:
            print('Invalid input')
            pointer = 'exit'
    else:
        print()
        print('Invalid output')
        pointer = 'exit'


def final_room():
    # create something to return
    pointer = ''
    print('You lose your footing, slipping and falling but it seems like you haven\'t hit the ground yet. It was only')
    sleep(sentence_pause)
    print('around 6 seconds later when you did, but for some reason you kept on going down, just not while in teh air.')
    sleep(sentence_pause)
    print('You were in some slide tunnel or something and it was going extremely fast which kind of made you panic.')
    sleep(sentence_pause)
    print('Air whooshed past you, whistling in your ears. It was originally so quiet, even your presence echoed.')
    sleep(sentence_pause)
    print('Finally, a peak  of light was visible and the next second, you were out in the open. It was bright and you')
    sleep(sentence_pause)
    print('could barely see a thing, so you squinted around the room and your surprise, you were back in your basement')
    sleep(sentence_pause)
    print('except something seemed a bit off....')
    sleep(sentence_pause)
    print()
    print('You peered to your right and you saw your lucky pen, but oddly it was 10x bigger than you. Immediately, you')
    sleep(sentence_pause)
    print('looked down and dwa you were standing on the letter "y" on your keyboard. Your eyes darted around to see')
    sleep(sentence_pause)
    print('your large screen and most shockingly... yourself, but larger, or normal size according to your gigantic')
    sleep(sentence_pause)
    print('surroundings.')
    sleep(sentence_pause)
    print()
    print('What happened next really startled you as the other you suddenly spoke with a mischievious grin, "Let\'s')
    sleep(sentence_pause)
    print('play a game shall we?" It doesn\'t seem like there is any other choice, so you accept as you stared at')
    sleep(sentence_pause)
    print('yourself. "Turn around now" instructed the larger you so you could face the screen. On there, it said ..')
    sleep(sentence_pause)
    print('TRIVIA ... not more questions you thought in dread, bt you know you had no options. You take a deep breath')
    sleep(sentence_pause)
    print('as your clone clicks on start .....')
    sleep(sentence_pause)
    print()
    sleep(sentence_pause)
    line1='************************'
    line2='*                      *'
    line3='*       The AD         *'
    line4='*                      *'
    line5='************************'
    line6='..^^..^^..^^..^^..^^..^^'
    line7='........THE END.........'
    print_characters(line1)
    print_characters(line2)
    print_characters(line3)
    print_characters(line4)
    print_characters(line5)
    print_characters(line6)
    print_characters(line7)


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


# main block for programming code

def main():
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
            pointer = room2()
            if pointer == 'exit':
                break
            pointer = room3()
            if pointer == 'exit':
                break
            pointer = final_room()
            if pointer == 'exit':
                break
        elif answer == 'n':
            break
        else:
            print('Invalid input')
            break
    # resets health if game restarts
    player.reset_health()
    print('hit end of while')


if __name__ == '__main__':
    main()
