#!/usr/bin/env python
import glob
import os
import ntpath

dirs = ['GSoC-2012', 'GSoC-2013', 'GSoC-2014', 'GSoC-2015']
ignored_f = ['AUTHORS.md', 'README.md']
fdict = {k:{'Accepted':[], 'Proposed':[]} for k in dirs}
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".md") and f not in ignored_f:
             path = ntpath.split(root)
             linkname = path[1]
             path = ntpath.split(path[0])
             gsoc = path[0][2:]
             acc_or_pro = path[1]
             fdict[gsoc][acc_or_pro].append('[{}]({}/{})'.format(linkname, root[2:], f))

strtext = ''
for key, value in fdict.iteritems():
    strtext += '- {}\n'.format(key)
    for a, flist in value.iteritems():
        if not flist:
            continue
        strtext += '\t- {}\n'.format(a)
        for fl in flist:
            strtext += '\t\t- {}\n'.format(fl)

print strtext

