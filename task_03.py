#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Loan compound interest calculator """


from decimal import Decimal


def loan_calc(principal, rate, years):
    """
    Calculate the final amount owed on a loan
    Args:
        principal (int): Principal amount of False
        rate (string): Interest rate
        years (int): Number of years to repay loan
    Returns:
        (int): Calculated amount owed
    """
    if rate:
        apr = Decimal(rate) / 100
        total = int(round(principal * ((1 + (apr / 12)) ** (12 * years))))
    else:
        total = None
    return total

INDEX = ''

TABLE = [
    (
        ((True, '3.63'), (False, '4.65')),
        ((True, '4.04'), (False, '4.98')),
        ((True, '5.77'), (False, '6.39'))
    ),
    (
        ((True, '3.02'), (False, '3.98')),
        ((True, '3.27'), (False, '4.08')),
        ((True, '4.66'), (False, None))
    ),
    (
        ((True, '2.05'), (False, None)),
        ((True, '2.62'), (False, None)),
        ((True, None), (False, None))
    )
]

NAME = PRINC = YEARS = PREQ = ''
COL1 = COL2 = COL3 = 0

QUES = ('What is your name? ',
        'What is the amount of your principal? ',
        'For how many years is this loan being borrowed? ',
        'Are you pre-qualified for this loan? ')



while not NAME:
    NAME = raw_input(QUES[0]).strip().title()
    if len(NAME) == 0:
        print 'Name missing'

while not PRINC or int(PRINC) <= 0:
    PRINC = raw_input(QUES[1]).strip()
    if not PRINC.isdigit():
        print 'Invalid principal amount'

while not YEARS:
    YEARS = raw_input(QUES[2]).strip()
    if not YEARS.isdigit() or int(YEARS) not in range(1, 31):
        print 'Entry must be a number between 1 and 30.'

while not PREQ:
    PREQ = str(raw_input(QUES[3])[:1]).upper()
    if PREQ not in ('Y', 'N'):
        print 'Answer Y(es) or N(o)'
        continue

PRINC = int(PRINC)
YEARS = int(YEARS)

if PRINC in range(1, 200000):
    COL1 = 0
elif PRINC in range(200000, 1000000):
    COL1 = 1
elif PRINC > 999999:
    COL1 = 2

if YEARS in range(1, 16):
    COL2 = 0
elif YEARS in range(16, 21):
    COL2 = 1
elif YEARS in range(21, 31):
    COL2 = 2

if PREQ == 'N':
    COL3 = 1

RATE = TABLE[COL1][COL2][COL3][1]

TOTAL = loan_calc(PRINC, RATE, YEARS)

FINAL = TOTAL
if TOTAL is not None:
    FINAL = '${:,}'.format(TOTAL)

REPORT = """
        Loan Report for: {}
        ---------------------------------------------
            Principal:            ${:,}
            Duration:             {}yrs
            Pre-Qualified:        {}
            Total:                {}
         """.format(NAME, PRINC, YEARS, PREQ, FINAL)

print REPORT
