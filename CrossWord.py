#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import re

def syllabify_gu(text):
        signs = [u'\u0abe',
                u'\u0abf',
                u'\u0ac0', 
                u'\u0ac1', 
                u'\u0ac2', 
                u'\u0ac3', 
                u'\u0ac4', 
                u'\u0ac5',
                u'\u0ac7', 
                u'\u0ac8', 
                u'\u0ac9',
                u'\u0acb',
                u'\u0acc',
                u'\u0a81',
                u'\u0a82',
                u'\u0a83',
                u'\u0acd'] 
        limiters = ['\"', '\'', '`', '!', ';', ', ', '?', '.']
        
        lst_chars = []
        for char in text:
            if char in limiters:
                lst_chars.append(char)
            elif char in signs:
                lst_chars[-1] = lst_chars[-1] + char
            else:
                try:
                    if char == u'\u0ab0' and len(lst_chars) > 0 and lst_chars[-1][-1] == u'\u0acd' and lst_chars[-1][-2] == u'\u0aa4': 
                        lst_chars[-1] = lst_chars[-1] + char
                    else:
                        lst_chars.append(char)
                except IndexError:
                    lst_chars.append(char)

        return lst_chars

print(syllabify_gu("સંગીત એ એવું પવિત્ર ઝરણું છે, જેનાં વહેતા તરંગોથી અંતરનાં તાર રણઝણી ઉઠે છે."))