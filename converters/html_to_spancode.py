#!/bin/bash
# -*- coding: utf-8 -*-

### Generate spancode from HTML ###
def gen_a_line(html):
	# Split line into tags
	tags = html.split('<')
	new_tags = []
	for i in range(1, len(tags)):
		new_tags.append(["&lt;" + str(tags[i].split('>')[0]) + "&gt;"])
		# new_tags[len(new_tags) - 1].append(tags[i].split('>')[1]) #

	# Convert html tags to spancode tags, with contents
	code_to_return = ""
	for i in range(0, len(new_tags)-1):
		line = "<li><span class='keyword'>" + new_tags[i][0]
		line += "</span>"
		line += tags[i + 1].split('>')[1]
		line += "</li>\n"

		code_to_return += line

	return code_to_return

print gen_a_line("""
<!DOCTYPE html>
<html>
	<body class="page">
		<h1>Test!</h1>
	</body>
</html>""")