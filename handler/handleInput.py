#!coding:utf-8
# /usr/bin/python


def qn(s):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", " "]
    for stuff in dirty_stuff:
        if s.find(stuff) >= 0:
            s = s.replace(stuff, "")
            raise TypeError
    return s
