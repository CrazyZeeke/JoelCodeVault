#####################################################################
#
# Script to scan folders and check the supplied file types for a string:
# working.  need to add line numbers.
# \\NYPMYAPPPRD16B.SIS.NYP.ORG\Apps\Root

import time
import os

search_string = "https://"
ignored = {"two", "three", "seven"}  #folders to be ignored during search

start_time = time.time() # We want to see how long the script executes.
print("starting scan: ")
#rootdir=('u:\\) # Mapped a Network Share to a local Drive (Z)
rootdir=('\\\\JOEL-11787\\temp')
#rootdir=('\\\\nypmynypuat16.sis.nyp.org\\D_SHARE_FULL\\sa') # Mapped a Network Share to a local Drive (Z)
#rootdir=('\\\\NYPMYAPPPRD16B.SIS.NYP.ORG\\Apps\\Root') # Mapped a Network Share to a local Drive (Z)


for folder, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith(('.json','.xml','.htm','.html','.txt','.config','.cshtml','.asax','.asc','.ashx','.css','.js','.asmx','.aspx','.cs','.vb','.webinfo','.soap','.shtml')):
			#fullpath = os.path.join(folder,file)
			fullpath = [x for x in fullpath.join(folder,file) if x not in ignored]
			with open(fullpath, 'r',errors='ignore') as f:

				line_count = 0 # initialize

				for line in f.readlines():

					line_count += 1
					if search_string in line:
						print(fullpath)	#print path of folder and file containing search_string
						print("\"https://\" Found on  line: %d \n" % line_count)

print("Script Took : --- %s seconds --- " % round( (time.time() - start_time)))
#######################################################################
# folders = [x for x in os.listdir(path) if x not in ignored]
#
#