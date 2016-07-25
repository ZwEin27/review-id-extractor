# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-22 17:52:30
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-25 17:49:14

import re

######################################################################
#   Constant
######################################################################

RE_DICT_NAME_IDENTIFIER = 'identifier'
RE_DICT_NAME_SITE = 'site'

RE_DICT_SITE_NAME_NR = 'nr'
RE_DICT_SITE_NAME_TER = 'ter'
RE_DICT_SITE_NAME_411 = '411'
RE_DICT_SITE_NAME_OTHERS = 'others'

RE_DICT_SITE = [
    RE_DICT_SITE_NAME_NR,
    RE_DICT_SITE_NAME_TER,
    RE_DICT_SITE_NAME_411,
    RE_DICT_SITE_NAME_OTHERS
]

punctuations = r'\!\"\!\"\$\%\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~'
keywords = [
    'review',
    'revews',
    'reviews',
    'reviewed',
    'reviewedid'
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
reg_word_gap = r'(?:(?:[a-z]|[a-z].*?[a-z]) ){,3}?' # ?
reg_fc_word_prev = r'(?:'+reg_keywords+r') '+reg_word_gap
reg_fc_word_post = reg_word_gap+r'?(?:'+reg_keywords+r')'
reg_fc_simple = r'#' #r'.{,5}?[#]'
reg_fc_ter = r'(?:\bt\s*?[e3]|\b[e3]\s*?p|\bt\s*?[e3]?\s*?r|\bt\b|\be\b|\br\b)'
reg_fc_id = r'i[\s'+punctuations+r']{,5}?d\s*?'

reg_back_check = r'(?![\s'+punctuations+r']*?(?:\d{4,5}|\d{7,}))'

reg_target = r'.{,2}?(?:\d{6}\b[\s\&]*)+'

reg_rid = [
    r'(?:'+reg_fc_simple+reg_target+reg_back_check+r')',
    r'(?:\b'+reg_fc_ter+reg_target+reg_back_check+r')',
    r'(?:\b'+reg_fc_id+reg_word_gap+reg_target+reg_back_check+r')',
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
        ans = []
        ans += [{RE_DICT_NAME_IDENTIFIER:_, RE_DICT_NAME_SITE: RE_DICT_SITE_NAME_OTHERS} for _ in re_simpleones.findall(text)]

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
    # text = "I am highly reviewed  (135701) ,  411 verified  "
    # text = "Out calls available.WELL REVIEWEDID 259771"
    # text = "my  I'd is 186058"
    # text = "In/Our calls, clean professional gentleman only. Clean,Discreet,Sanctuary for In Calls. Real photos, 100% Independent, Intelligent, and Truly a class above... \nWell Reviewed onID #283603 and Usasexguide(dot)com #2008\n239-321-2063\n8am-8pm, unless arrangements are made in advanced.\nDonation basis but Generousity is always met w Gratitude. Well Reviewed,\nToday only $20 off any session.\nCall Now 2393212063. I offer video/photo also, ask me on my profile before calling...  Adult Finder"
    # text = "I'll have your heart skipping beats. To the point you can't hardly breathe. I'll bring out the FREAK IN ME. I'll have your knees shaking and biting your lips from the way I'd kiss you. Have your hips going all the way with it. Losing control, but staying with it.  Review ID: 159184 p/411: P59111 \n  \n CARTY 7083208795 Avail 24/7   My Pix and Vids"
    # text = "In/Our calls, clean professional gentleman only. Clean,Discreet,Sanctuary for In Calls. Real photos, 100% Independent, Intelligent, and Truly a class above... \nWell Reviewed onID #283603 and Usasexguide(dot)com #2008\n239-321-2063\n8am-8pm, unless arrangements are made in advanced.\nDonation basis but Generousity is always met w Gratitude. Well Reviewed,\nToday only $20 off any session.\nCall Now 2393212063. I offer video/photo also, ask me on my profile before calling...  Adult Finder"
    print DIGRIDE.extract(text)