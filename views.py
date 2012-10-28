from django.http import HttpResponse
from django.template import loader, Context

import pusher
import sys

debug = True

def debugPrint(astring):
    if debug:
        print debug

def pusherInitialize():
    pusher.app_id = '30052'
    pusher.key = '8754603d024bc6ca00de'
    pusher.secret = '785335c8057c784eccb0'
    return pusher.Pusher()

def pusherPushData(idNum, actionType, dataChange, dataLocation = None):
    try:
        p['%i'%idNum].trigger('dataChange', {"Type": actionType, "Location": dataLocation, "ChangeTo": dataChange})
        debugPrint("Change Pushed: TYPE=%s LOCATION=%s CHANGE=%s" % (actionType, dataLocation, dataChange))
    except e:
        print("! Unexpected error:", sys.exc_info()[0])