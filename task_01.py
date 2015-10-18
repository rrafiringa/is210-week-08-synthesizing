#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Color choices """


ACCENTS = ('Ceramic Glaze', 'Cumulus Nimbus',
           'Platinum Mist', 'Spartan Sage')
HIGHLIGHTS = ('Basically White', 'White',
              'Off-White', 'Paper White',
              'Bone White', 'Just White',
              'Fractal White', 'Not White')

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"? ')
if BASE == 'Seattle Gray':
    ACCENTS = ACCENTS[:2]
    HIGHLIGHTS = HIGHLIGHTS[:4]
else:
    ACCENTS = ACCENTS[2:]
    HIGHLIGHTS = HIGHLIGHTS[4:]

QUES = 'Which accent color, "{}" or "{}"? '.format(ACCENTS[0], ACCENTS[1])
ACCENT = raw_input(QUES)

for idx, acolor in enumerate(ACCENTS):
    if ACCENT == acolor:
        hstart = idx * 2
        hend = hstart + 2
        HIGHLIGHTS = HIGHLIGHTS[hstart:hend]
        break

QUES = 'Which highlight color, "{}" or \
"{}"? '.format(HIGHLIGHTS[0], HIGHLIGHTS[1])
HIGHLIGHT = raw_input(QUES)
print 'Your selected colors are {}, {}, \
and {}.'.format(BASE, ACCENT, HIGHLIGHT)