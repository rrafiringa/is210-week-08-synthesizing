#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Loan compound interest calculator """


from decimal import Decimal

QUES = ('What is your name? ',
        'What is the amount of your principal? ',
        'For how many years is this loan being borrowed? ',
        'Are you pre-qualified for this loan? ')

NAME = raw_input(QUES[0])
PRINC = int(raw_input(QUES[1]))
YEARS = int(raw_input(QUES[2]))
PREQ = raw_input(QUES[3])[:1].upper()

TABLE = [
    (
        (('Y', '3.63'), ('N', '4.65')),
        (('Y', '4.04'), ('N', '4.98')),
        (('Y', '5.77'), ('N', '6.39'))
    ),
    (
        (('Y', '3.02'), ('N', '3.98')),
        (('Y', '3.27'), ('N', '4.08')),
        (('Y', '4.66'))
    ),
    (
        (('Y', '2.62')),
        (('Y', '2.62'))
    )
]

MSG = []
COL1 = 0
COL2 = 0
COL3 = 0

PRINCFLAG = True
YEARSFLAG = True
PREQFLAG = True
REPORT = None

if NAME.strip():

    if PRINC in range(1, 200000):
        COL1 = 0
    elif PRINC in range(200000, 999999):
        COL1 = 1
    elif PRINC > 999999:
        COL1 = 2
    else:
        PRINCFLAG = False
        MSG.append('Error: Principal entered out of range.')
    if YEARS in range(1, 16):
        COL2 = 0
    elif YEARS in range(16, 21):
        COL2 = 1
    elif YEARS in range(21, 31):
        COL2 = 2
    else:
        YEARSFLAG = False
        MSG.append('Error: Years specified out of range.')

    if PREQ == 'Y':
        PREQ = 'Yes'
        COL3 = 0
    elif PREQ == 'N':
        PREQ = 'No'
        COL3 = 1
    else:
        PREQFLAG = False
        MSG.append('Error: Pre-qualification is Y(es) or N(o).')

    if PRINCFLAG and YEARSFLAG and PREQFLAG:
        RATE = Decimal(TABLE[COL1][COL2][COL3][1])/100
        TOTAL = int(round(PRINC * ((1 + Decimal(RATE / 12)) ** (12 * YEARS))))
        REPORT = """
        Loan Report for: {}
        ---------------------------------------------
            Principal:            ${:,}
            Duration:             {}yrs
            Pre-Qualified:        {}

            Total:                ${:,}
        """.format(NAME, PRINC, YEARS, PREQ, TOTAL)
        print REPORT
else:
    MSG.append('Error: No name entered.')

if MSG:
    for item in MSG:
        print '- ' + item + '\n'