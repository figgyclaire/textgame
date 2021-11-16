import random as r

lives = 3


def lose():
    lives = lives - 1


def room(story):
    with open(story) as file:
        for line in file:
            line = line.rstrip('\n')
            print(line)


while True:
    if lives < 1:
        print('You lose')
        break
    room('intro.txt')
    # Casey
    while True:
        room('casey.txt')
        teacher_student = input('>')
        # student
        if teacher_student == 'b':
            print('They come running at you with a pencil. What do you do? \
Offer them a sharpener or duck them? (Type "o" for offer or "d" for duck)')
            sharpener = input('>')
            if sharpener == 'o':
                lose()
                continue
            else:
                print('You duck and run around the room to the teacher.')
                break
            
        # teacher
        if teacher_student == 'r':
            print('You see that they are about to fall for a scam. It says, \
"Are you sick of your boring job? Well you don\'t need to be anymore because \
if you just give us some information, you can win a bunch of money by \
TimSecure! "Why is my name on an ad I have never created before?" you thought.\
Should you tell them about the scam? (Type "y" for yes or "n" for no)')
            scam = input('>')
            if scam == 'y':
                print('You decide to tell Miss Rack. She thanks you dearly and \
you earn a key. You find a door which the key fits in so you unlock it and \
enter to find that you are surronded by darkness and gloom.')
                break
            else:
                print('You lose a life')
                lose()
                continue
    #Yash
    while True:
        room('yash.txt')
        while True:
            print('Should you install something off a website that you feel is \
not secure?')
            q1 = input('>')
            if q1 == 'y':
                lose()
                continue

            else:
                print('The virus self-destructs. Amazed, you slowly advance to \
the next virus which asks you another question in a raspy voice that reminds \
you of someone who has the flu.')
                break

        while True:
            print('Should you post personal data online?')
            q2 = input('>')
            if q2 == 'y':
                lose()
                continue

            else:
                print('Finally; ther is only one more virus you have to pass, \
and it asks you this question...')
                break

        while True:
            print('Is it safe to accept random friend requests online?')
            q3 = input('>')
            if q3 == 'y':
                lose()
                continue

            else:
                print('Suddenly, a key appears in your hand. It must unlock \
the door at the end of the room, you think to yourself. When you unlock the \
door and pull it open, you realise it leads you to a blue tube- a slide. \
Uneasy, you turn back towards the room you just left, when suddenly, the \
remaining viruses push you down the slide.')
                break

        #Kadie
        while True:
            room('kd1.txt')
            l_r = input('>')
            if l_r == 'left':
                room('kd_left.txt')
                break

            else:
                room('kd_right.txt')
                break

        while True:
            room('kd_continue.txt')
            light_look = input('>')
            if light_look == 'ls':
                    room('kd_light_switch.txt')
                    break

                





