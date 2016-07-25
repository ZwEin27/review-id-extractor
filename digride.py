# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-22 17:52:30
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-25 10:15:59

import re

######################################################################
#   Constant
######################################################################

punctuations = r'\!\"\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~'

######################################################################
#   Regular Expression
######################################################################

reg_back_check = r'(?!['+punctuations+r']*?\d))'
reg_target = r'.{,5}?\d{6}'

reg_rid = [
    r'(?:\b(?:t\b\s*?e\b\s*?r|\bt\b|\be\b|\br\b)'+reg_target+reg_back_check,
    r'(?:\bi[\s'+punctuations+r']{,5}?d'+reg_target+reg_back_check,
    r'(?:\b(?:t\s*?e\s*?r|\bt\b|\be\b|\br\b).{,5}i[\s'+punctuations+r']{,5}?d'+reg_target+reg_back_check
]
re_rid = re.compile(r'(?:'+r'|'.join(reg_rid)+r')', re.IGNORECASE)

re_digits = re.compile(r'(?:\d{6})')


######################################################################
#   Main Class
######################################################################


class DIGRIDE(object):

    @staticmethod
    def extract(text):
        ans = re_rid.findall(text)
        # print ans
        ans = [re_digits.search(_).group(0) for _ in ans]
        return ans


if __name__ == '__main__':
    text = "My I.D.267101"
    print DIGRIDE.extract(text)