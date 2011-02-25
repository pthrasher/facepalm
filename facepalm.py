#!/usr/bin/env python

import datetime, sys
import cPickle as pickle

try:
    if sys.argv[1]=="--close" or sys.argv[1]=="-C":
        bugs=pickle.load(open("bugs"))
        for i in bugs:
            print "Date:\t%s" % i['date']
            print "Notes:\t%s" % i['notes']
            print "Scale:\t%d" % i['scale']
            print "ID:\t%d" % i['id']
            print "\n"
        print "Which ID should I remove?"
        del bugs[int(raw_input("> "))]
        pickle.dump(bugs, open("bugs", "wb"))
    else:
        print "Usage: python facepalm.py [-C --close]"
except IndexError:
    print "Welcome to Facepalm! How epik is the fail? On a scale of 1-5, with 5 being a small fail and 1 being 'EFFING HUGE!'"
    scale = int(raw_input("> "))

    if scale == 5:
        print "Dude, fail properly! *facepalm*"
    elif scale == 4:
        print "Dude! Face, meet palm *facepalm*"
    elif scale == 3:
        print "Dude! WTF? *headdesk*"
    elif scale == 2:
        print "%s NOOO!" % ("."*10)
    elif scale == 1:
        print "%s *falls off cliff* retard!" % ("."*20)

    print "\nDo you want to add this to the bug list? [Y]/[N]"
    
    if raw_input("> ").lower() == "y":
        try:
            bugs=pickle.load(open("bugs"))
        except IOError:
            bugs = []
        new = {"date":datetime.date.today(), "scale":scale, "id":len(bugs)}
        
        print "Notes about bug:"
        new["notes"]=raw_input("> ")

        bugs.append(new)
        print "Bug succesfully added!"
        pickle.dump(bugs, open("bugs", "wb"))
    else:
        print "Fine, don't use me then!"