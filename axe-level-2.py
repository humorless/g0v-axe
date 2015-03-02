# encoding: utf-8
# http://axe.g0v.tw/level/2

import urllib2, re

websites =["http://axe-level-1.herokuapp.com/lv2/?page=%d"% i for i in range(1,13)]
htmls = [urllib2.urlopen(website).read() for website in websites]
pattern = r"<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>"
results = [re.findall(pattern, html)[1:] for html in htmls]
sformat = '{"town": "%s", "village": "%s", "name" : "%s"}'
results = [sformat % tuple(x) for y in results for x in y ]
with open("ans.txt", "w") as f:
	f.write("[%s]" % ",\n".join(results))


