#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


# Remove _
def remove_underline(text):
    """
    Remove _
    :param text:
    :return:
    """
    return text.replace(u"_", u"")
# end remove_underline


# Remove - \n
def remove_line_breaks(text):
    """
    Remove - \n
    :param text:
    :return:
    """
    return text.replace(u"- \n", u"")
# end remove_line_breaks
