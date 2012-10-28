import random
import pusher
import sys

pusher.app_id = '30052'
pusher.key = '8754603d024bc6ca00de'
pusher.secret = '785335c8057c784eccb0'
p = pusher.Pusher()

def pusherPushData(idNum, actionType, lineStart = None, lineEnd = None, charStart = None, charEnd = None, dataChange=None):
    p['%i'%idNum].trigger('dataChange', {"Type": actionType, "LineFrom": lineStart, "LineTo": lineEnd, "CharFrom":charStart, "CharTo":charEnd, "ChangeTo": dataChange})

    print("Change Pushed: ID=%s TYPE=%s LINESTART=%s LINEEND=%s CHARSTART=%s CHAREND=%s CHANGE=%s" % (idNum, actionType, lineStart, lineEnd, charStart, charEnd, dataChange))


def main():
    while True:
        raw_input("Press enter to send pusher data")
        pusherPushData(random.randint(1000,9999), "Test", random.randint(1,9), random.randint(10,19), random.randint(20,29), random.randint(30,39), "j")


main()
