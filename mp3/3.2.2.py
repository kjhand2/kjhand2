#!/usr/bin/python2.7
import dpkt
import sys


def sanity_check():
    if (len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)

    filename = sys.argv[1]
    return


if __name__ == '__main__':
    sanity_check()

print "everything is fine"