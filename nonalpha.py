#-*- coding: utf-8 -*-
import string
import sys

class esalpha(object):
    def logo(self):
        print r"""-------------
 _____     _ _   _____ _
|  ___|   (_) | /  ___| |
| |____  ___| |_\ `--.| |_ __ _ _ __ ___
|  __\ \/ / | __|`--. \ __/ _` | '__/ __|
| |___>  <| | |_/\__/ / || (_| | |  \__ \
\____/_/\_\_|\__\____/ \__\__,_|_|  |___/

-------------
Cyber-Warrior | Bug Researchers | ExitStars"""

    def check(self,getme):
        if getme.isalnum() != False:
            target = string.ascii_letters + string.digits
        else:
            target = string.ascii_letters + string.digits + string.punctuation
        getme = [x for x in getme]
        Nonalphanumeric = [ord(x) for x in string.punctuation]
        del Nonalphanumeric[23]
        emptylist = []

        for x in xrange(20, 127):
            for y in xrange(20, 127):
                test = ord(chr(x)) ^ ord(chr(y))
                if chr(test).lower() in target or chr(test).upper() in target:
                    if ord(chr(x)) in Nonalphanumeric and ord(chr(y)) in Nonalphanumeric:
                        if chr(test) in getme:
                            dump = "('%s'^'%s')||%s" % (chr(x),chr(y),chr(test))
                            emptylist.append(dump)
                    else:
                        if "(" == chr(test) or ")" == chr(test):
                            if chr(test) in getme:
                                dump = "('%s'^'%s')||%s" % (chr(x),chr(y),chr(test))
                                emptylist.append(dump)
                        else:
                            if chr(test) in string.punctuation:
                                if chr(test) in getme:
                                    dump = "('%s'^'%s')||%s" % (chr(x),chr(y),chr(test))
                                    emptylist.append(dump)

        for x in set(emptylist):
            if x.split("||")[1] in getme:
                padding = x.split("||")[0]
                getme[getme.index(x.split("||")[1])] =  padding
                if chr(32) in getme:
                    getme[getme.index(chr(32))] = "('~'^'^')"

        fix = str('.'.join(getme))
        fix = fix.replace(".l", "").replace(" ", "").replace("..", ".");
        self.logo();
        print "\n\n"+fix+"\n\n",


if __name__ == '__main__':
    esalpha().check(sys.argv[1])
