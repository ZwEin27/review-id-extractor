# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-22 17:52:30
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-25 14:10:32

import re

######################################################################
#   Constant
######################################################################

punctuations = r'\!\"\!\"\$\%\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~'
keywords = [
    'review',
    'reviews',
    'reviewed'
]


######################################################################
#   Regular Expression
######################################################################

re_tokenize = re.compile(r'[\s'+punctuations+r']')
re_seperator = re.compile(r'[\n]')

reg_simpleones = [
    r'(?<=\n\n)\d{6}$'
]
re_simpleones = re.compile(r'(?:'+r'|'.join(reg_simpleones)+r')', re.IGNORECASE)

reg_keywords = r'|'.join(keywords)
reg_fc_word_prev = r'(?:'+reg_keywords+r') (?:(?:[a-z]|[a-z].*?[a-z]) ){,3}?'
# reg_fc_word_prev = r'(?:'+reg_keywords+r') T '
reg_fc_word_post = r'(?:(?:[a-z]|[a-z].*?[a-z]) ){,3}?(?:'+reg_keywords+r')'
reg_fc_simple = r'#' #r'.{,5}?[#]'
reg_fc_ter = r'(?:\bt\s*?[e3]|\b[e3]\s*?p|\bt\s*?[e3]?\s*?r|\bt\b|\be\b|\br\b)'
reg_fc_id = r'i[\s'+punctuations+r']{,5}?d'

reg_back_check = r'(?![\s'+punctuations+r']*?(?:\d{4,5}|\d{7,}))'

reg_target = r'.{,2}?(?:\d{6}[\s\&]*)+'

reg_rid = [
    r'(?:'+reg_fc_simple+reg_target+reg_back_check+r')',
    r'(?:\b'+reg_fc_ter+reg_target+reg_back_check+r')',
    r'(?:\b'+reg_fc_id+reg_target+reg_back_check+r')',
    r'(?:\b'+reg_fc_ter+r'.{,5}?'+reg_fc_id+reg_target+reg_back_check+r')',
    r'(?:'+reg_fc_word_prev+reg_target+reg_back_check+r')'
]
re_rid = re.compile(r'(?:'+r'|'.join(reg_rid)+r')', re.IGNORECASE)
# print reg_rid
re_digits = re.compile(r'(?:\d{6})')


######################################################################
#   Main Class
######################################################################


class DIGRIDE(object):

    @staticmethod
    def extract(text):
        # ans = []
        ans = re_simpleones.findall(text)
        # print 'ans', ans
        text = re_seperator.sub(' sep ', text)
        text = ' '.join([_.strip() for _ in re_tokenize.split(text) if _.strip() != ''])
        # print text.encode('ascii', 'ignore')
        potentials = re_rid.findall(text)
        # print potentials
        for p in potentials:
            ans += re_digits.findall(p)
        return list(set(ans))


if __name__ == '__main__':
    # text = "My I.D.267101"
    # text = "Reviewed #229512 T.e. R"
    # text = "Hey guys! I'm Heidi!!! I am a bubbly, busty, blonde massage therapist and only provide the most sensual therapeutic experience! I love what I do and so will YOU!!! I am always learning new techniqes and helping other feel relaxed. Just send Me an email and lets meet!!!  I am reviewed! #263289 \nheidishandsheal@gmail.com"
    # text = "Reviewed TER 202567 "
    # text = "EXCEPTION TRiD:263865.Call  404-599-8674"
    # text = "VIP. Sexy Escort Girls. High Class Pune Escorts agency CALL ROBIN- 096997 37222 / 09767 303000 "
    # text = "Highly reviewed on , 178352 "
    # text = "HIGHLY REVIEWED id number 195001 & 260255 OUTCALL/INCALL"
    # text = " # 257884"
    # text = "??TER ID: 207787 "
    # text = "Super 8314063130 tr 203337 Habla espanol.Call"
    # text = "? #609418-0946"
    # text = "guys  Ep 161566 & Te 192110"
    # text = "??T/ E/ R ID: 207787"
    # text = "Check out my reviews T-212440  *82 619 219 1734"
    # text = "Check out my reviews T 212440"
    # text = "Well Reviewed #185826"
    # text = "*AVAILABLE NOW. *\n100% Real/Recent Pics.\n5'1105lbs34B\nYES. I Have A Reviews. TER_ID:[[227083]]\nCome Fall In Love with Orlando's Top ProVider. \n MERCEDES 4074596026.  Me and my friends are on Adult Finder  soooo you can find us all on there if you want... smooth_thigh"
    text = "I am highly reviewed  (135701) ,  411 verified  "
    print DIGRIDE.extract(text)