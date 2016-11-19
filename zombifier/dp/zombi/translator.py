#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on Mar 8, 2016

@author: graham
'''
import codecs

# ZOMBI_KEY  = {
#         'e': 'r',
#         's': 'rr',
#         'a': 'rrr',
#         'i': 'a',
#         't': 'h',
#         'n': 'g',
#         'r': 'o',
#         'u': 'gg',
#         'l': 'aa',
#         'o': 'hh',
#         'd': 'oo',
#         'c': 'R',
#         'p': 'A',
#         'm': 'H',
#         'v': 'G',
#         'q': 'O',
#         'f': 'RR',
#         'b': 'AA',
#         'g': 'HH',
#         'h': 'GG',
#         'j': 'OO',
#         'x': 'rrrr',
#         'y': 'RRR',
#         'z': 'aaa',
#         'w': 'ggg',
#         'k': 'hhh',
#         }

ZOMBI_KEY  = {
        'e': 'r',
        's': 'rr',
        'a': 'rrr',
        'i': 'a',
        't': 'h',
        'n': 'g',
        'r': 'o',
        'u': u'ù',
        'U': 'U',
        'l': 'aa',
        'o': u'ò',
        'O': u'Ò',
        'd': 'oo',
        'c': 'R',
        'p': 'p',
        'P': 'P',
        'm': 'H',
        'v': 'G',
        'q': 'O',
        'f': 'f',
        'F': 'F',
        'b': 'AA',
        'g': 'HH',
        'h': 'GG',
        'j': 'OO',
        'x': 'rrrr',
        'y': 'RRR',
        'z': 'aaa',
        'w': 'ggg',
        'k': 'hhh',
        }


CONVERT_KEY = {u'é': 'e',
               u'à': 'a',
               u'è': 'e',
               u'ê': 'e',
               u'ç': 'c',
               u'ù': 'u',
               u'î': 'i',
               u'œ': 'e',
               u'ï': 'i',
               u'ë': 'e'}

# Concertit un caractère en lower case et vire les accentuations.
def toCharKey(c):
    if ZOMBI_KEY.get(c) == None:
        return CONVERT_KEY.get(c.lower(), c.lower())
    return c

##
# Traduit un message dans la langage zombi 
def translate(frMessage):
    zombiMessage = ""
    for c in frMessage:
        charKey = toCharKey(c)
        zombiMessage += ZOMBI_KEY.get(charKey, charKey)
    return zombiMessage


def test():
    print(translate('a'))
    print(translate("a"))
    print(translate("aa"))
    print(translate("Ceci"))
    print(translate("Manger.... viande......"))
    print(toCharKey("è"))
    print(translate(u"Bèèèh"))
    print(translate(u"è"))
    print(translate("Un machinu"))

if __name__ == '__main__':
    #with open ("inputFr.txt", "r") as myfile:
    with codecs.open("inputFr.txt", "r", encoding='utf-8') as myfile:
        lines = myfile.readlines()
        for l in lines:
            print(translate(l))
    #test()
