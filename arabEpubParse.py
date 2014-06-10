from HTMLParser import HTMLParser
import htmlentitydefs
import os #, subprocess

import sys, getopt

import re

 
#currString = ''
file_to_write = ''#open('/Applications/djangostack-1.5.8-0/apps/django/django_projects/Project/tester.rtf', 'w')

class EpubHTMLParser(HTMLParser):
	ignore = "DON'T SAVE"
	gloss = "GLOSS"
	explanations = "EXPLANATION"
	save_state = ignore
	sentence_count = 0
	curr_proverb_number = 0

	#debugging
	prev_data = ""

	def isInt(self, letters):
		try:
			return type(int(letters)) == int
		except ValueError:
			return False

	#the following function was written by Frederik Lundh and published on January 15, 2003
	def unescape(self, text):
		def fixup(m):
			text = m.group(0)
			if text[:2] == "&#":
            	# character reference
				try:
					if text[:3] == "&#x":
						return unichr(int(text[3:-1], 16))
					else:
						return unichr(int(text[2:-1]))
				except ValueError:
					pass
			else:
            	# named entity
				try:
					text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
				except KeyError:
					pass
			return text # leave as is
		return re.sub("&#?\w+;", fixup, text)
	#End borrowed code

	def handle_starttag(self, tag, attrs):
		#global file_to_write
		print "attrs: ", attrs


	def handle_charref(self, name):
		if self.isInt(name):
			file_to_write.write(self.unescape("&#"+name+";").encode("utf8"))
		else:
			file_to_write.write(self.unescape("&"+name+";").encode("utf8"))


	def handle_data(self, data):
		global file_to_write
		final_punct = ['.', '!', '?']
		

############# Command line initialization #############

def print_to_file(folder, output_file_name):
	global file_to_write
	try:
		file_to_write = open(folder+output_file_name, 'w')
		for doc in os.listdir(folder):
			epubParse(folder+doc)
			print "Successfully processed document: " + doc
	except OSError:
		print "Problems arose in the print to file function. Change your directory."

def reprocess_file(folder, output_file_name):
	with open(folder+output_file_name, 'r') as output:
		for line in output:
			if line[0] == "#":
				r = 0
				#wait until the next period, then check to see how long the next passage is. If it's ridiculously long (>3),
				#flag it as strange-looking
			continue
		return

def main(argv = None):
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
	except getopt.error, msg:
		print msg
		print "for help use --help"
		sys.extit(2)

	for o in opts:
		if o in ("-h", "--help"):
			print "The only argument needed is the location of the directory of the html files you'd like to parse."
			sys.exit(0)
	if len(args) == 1:
		print "Yay, you only gave one argument! Now we can process it."
		for arg in args:
			process(arg)
	else:
		print "Please try to limit yourself to one directory and start over."
		sys.exit(0)

def process(arg):
	try:
		print_to_file(arg, 'parsed_data.txt')
	except OSError:
		print "This directory doesn't work: ", arg


#if __name__ == "__main__":
#	main()

path = '/Applications/djangostack-1.5.8-0/apps/django/django_projects/Project/Arabic_Proverbs/OEBPS/__1/'
#filename = 'content-0009.xml'

#print_to_file(path, 'concat_output.txt')
