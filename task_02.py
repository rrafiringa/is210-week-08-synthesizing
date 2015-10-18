#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple alarm """

RETRY = True
BEEPS = 'Beep! Beep! Beep! Beep! Beep!'
while RETRY:
    DOW = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    DAY = raw_input('What day is it? ')[:3].title()
    if DAY in DOW:
        HOUR = raw_input('What time is it? ')
        if HOUR.isdigit():
            if int(HOUR[:2]) in range(0, 24) and \
                    int(HOUR[2:]) in range(0, 60):
                SNOOZE = True if \
                    ((DAY in ('Sat', 'Sun')) or int(HOUR) < 600) else False
                if not SNOOZE:
                    print BEEPS
                RETRY = False
            else:
                print HOUR + ' is not a valid time. Try again.'
    else:
        print DAY + ' is not a valid day of the week. Try again.'