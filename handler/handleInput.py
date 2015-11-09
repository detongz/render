#!coding:utf-8
# /usr/bin/python


def qn(s):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", " "]
    for stuff in dirty_stuff:
        if s.find(stuff) >= 0:
            s = s.replace(stuff, "")
            raise TypeError
    return s


def qndes(s):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%"]
    for stuff in dirty_stuff:
        if s.find(stuff) >= 0:
            s = s.replace(stuff, "")
            raise TypeError
    return s


def text2Html(content):
    def escape(txt):
        """将txt文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示"""
        txt = txt.replace('&', '&#38;')
        txt = txt.replace(' ', '&#160;')
        txt = txt.replace('<', '&#60;')
        txt = txt.replace('>', '&#62;')
        txt = txt.replace('"', '&#34;')
        txt = txt.replace('\'', '&#39;')
        return txt

    content = escape(content)
    lines = content.split('\n')
    for i, line in enumerate(lines):
        lines[i] = '<p>' + line + '</p>'
    content = ''.join(lines)
    return content
