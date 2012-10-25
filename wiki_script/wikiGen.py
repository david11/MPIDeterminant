#!/usr/bin/python

# Copyright (c) <2012>, <Victor Mateevitsi> www.vmateevitsi.com
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by the <organization>.
# 4. Neither the name of the <organization> nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import readline
import re

f = open(sys.argv[1:][0])

lines = f.readlines()
prog = re.compile('(\w){4}')
n = "0"
table = "{| class=\"wikitable\"\n|"
chart = []
index = -1
buf = ""
for line in lines:
	numb = line.split()
	#m = re.search('((\d+)\t){4}((\number)\t){4}', line)
	#m = prog.match(line)
	#print numb[0] + " " + numb[1]
	table += "-\n"
	if not numb[0].isdigit():
		for h in numb:
			table += "! " + h + "\n"
	else :
		for h in numb:
			table += "|" + h + "\n"
	table += "|"
	if n != numb[0] and numb[0].isdigit():
		n = numb[0]
		index += 1
		if index != 0:
			buf += "</pbars>\n"
			chart.append(buf)
		buf = "<pbars size=600x300 title=\"n=" + n + "\" ymin=0 ymax=290 legend decimals=5>\n,Generate Array,Processing,Communication\n"
		n = numb[0]
		p = numb[2]
		k = numb[3]
		ge = numb[4]
		pr = numb[5]
		co = numb[6]
		buf += "p=" + p + " k=" + k + ", " + ge + ", " + pr + ", " + co + "\n"
	elif numb[0].isdigit():
		n = numb[0]
		p = numb[2]
		k = numb[3]
		ge = numb[4]
		pr = numb[5]
		co = numb[6]
		buf += "p=" + p + " k=" + k + ", " + ge + ", " + pr + ", " + co + "\n"
buf += "</pbars>"

chart.append(buf)
table += "}\n"
#print table
for c in chart:
	#print c
	table += c
f.close()

f2 = open("w" + sys.argv[1:][0], "w")
f2.write(table);
f2.close()
