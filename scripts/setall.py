#!/usr/bin/env python
########################################################################
# \file setall.py    	                                               #
#                                                                      #
# SETUP              / The goal is to setup the media and the rest     #
#                      for the website project                         #
#                                                                      #
# This program is free software; you can redistribute it and/or modify #
# it under the terms of the associated license. For more information   #
# about these matters, see the file named COPYING.                     #
#                                                                      #
# \date    March 2013                                                  #
# \author  Flavio Tarsetti (tarsetti dot flavio at gmail dot com)      #
#                          or (angeldoescryi at gmail dot com)         #
#                          tarsetti.flavio@gmail.com                   #
#                          or angeldoescryi@gmail.com                  #
#                                                                      #
# Copyright (c) 2013 - Flavio Tarsetti                                 #
########################################################################

#=========================================================
# IMPORTS
#=========================================================
import os
import re
import sys
import optparse
import shutil
import random
import time
from optparse import OptionParser
from time import localtime, strftime
from datetime import datetime


#=========================================================
# GLOBAL VARS
#=========================================================

Version = "1.0"
Project = "Tumblelog"
test = "\ntest\n"
program_description = """--------------------------------------------
**Setup media and other ressources for the project**
Version : %s"""%Version+"""\nProject  : %s"""%Project+"""\n--------------------------------------------"""

#=========================================================
# MAIN
#=========================================================


if __name__ == '__main__':

    print program_description
    usage = "usage: %prog [options]"

    #Experiments specification
    print "\nBegin ressource preparation on :"
    os.system('hostname')
    print strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    print "\n"

    parser = OptionParser(usage)
    parser.set_description("***Package Preparation***")
    
    parser.add_option("--media_dir",dest="media_dir", help = "media/ files",default="")
    parser.add_option("--bootstrap",dest="bootstrap", help = "bootstrap dependencies",default="false")
    parser.add_option("--django-registration",dest="django-registration", help = "django-registration dependencies MongoEngine/templates",default="false")
    parser.add_option("--archive",dest="archive", help = "archive previously working system",default="false")
    parser.add_option("--archive_dir",dest="archive_dir", help = "archive directory name",default="archive")
    parser.add_option("-o","--output_folder",dest="output_folder", help = "output folder where to store files", default=".");
    parser.add_option("-v","--verbose",dest="verbosity", help="need more verbosity?", default="false")

    try:
        (options,args) = parser.parse_args()
    except:
        parser.error("cmdline error")
        sys.exit(-1)

    ##line command creation according to the passed options 
    #if(options.input_file=="empty" and options.input_list=="empty"):
    #    print "No single image or image list specified"
    #elif(options.input_file =="empty" and options.input_list!="empty"):
    #elif(options.input_file !="empty" and options.input_list=="empty"):
    #else :  print "ERROR"
    
    """print len(args)
    if len(args) < 1:
        parser.error("incorrect number of arguments")
    """
    print "--------------------------------------------"
    print "  media directory: %s"% options.media_dir
    print "  bootstrap: %s"% options.bootstrap
    print "  django-registration: %s"% options.django-registration
    print "  archive: %s"% options.archive
    print "  archive directory: %s"% options.archive_dir
    print "  output directory: %s" % (".")
    print "\n";
    print "  verbosity: %s" % options.verbosity
    print "--------------------------------------------\n\n";
    

#=========================================================
# EXPERIMENTS SETTINGS
#=========================================================
    rootPath = os.getcwd()
    
    if options.archive == "true":
        #if directories don't exist - create
        if not os.path.exists(rootPath+"/%s"%(options.archive_dir)):
            os.makedirs(rootPath+"/%s"%(options.archive_dir))
   
        dt = datetime.now()
        shutil.copytree(rootPath+"/media", rootPath+"/%s/media_%s_%s_%s_%s_%s_%s"%(options.archive_dir, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
        os.chdir("%s"%options.archive_dir)
        os.system("tar -zcvf %s.tar.gz %s"%("media_%s_%s_%s_%s_%s_%s"%(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second),
        "media_%s_%s_%s_%s_%s_%s"%(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)))
        os.system("rm -fr media_%s_%s_%s_%s_%s_%s"%(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
        os.chdir("%s"%rootPath)
        #remove directory
        shutil.rmtree(rootPath+"/media")
        #create media directories
        os.makedirs(rootPath+"/media")
        os.makedirs(rootPath+"/media/css")
        os.makedirs(rootPath+"/media/js")
        os.makedirs(rootPath+"/media/img")

    if options.bootstrap == "true":
        #if directories don't exist - create
        if not os.path.exists(rootPath+"/media"):
            os.makedirs(rootPath+"/media")
        #remove directory
        if os.path.exists(rootPath+"/media/css/bootstrap"):
            os.system("rm -fr %s/%s"%(rootPath, "media/css/bootstrap"))
        os.makedirs(rootPath+"/media/css/bootstrap")
        if os.path.exists(rootPath+"/media/js/bootstrap"):
            os.system("rm -fr %s/%s"%(rootPath, "media/js/bootstrap"))
        os.makedirs(rootPath+"/media/js/bootstrap")
        if os.path.exists(rootPath+"/media/img/bootstrap"):
            os.system("rm -fr %s/%s"%(rootPath, "media/img/bootstrap"))
        os.makedirs(rootPath+"/media/img/bootstrap")

        #unzip bootstrap
        os.chdir("dependencies")
        os.system("unzip bootstrap.zip")
        os.chdir("%s"%rootPath)
        os.system("mv dependencies/bootstrap/css/* media/css/bootstrap/.")
        os.system("mv dependencies/bootstrap/js/* media/js/bootstrap/.")
        os.system("mv dependencies/bootstrap/img/* media/img/bootstrap/.")

        #remove directory
        os.system("rm -fr dependencies/bootstrap")

    #TODO: implement option
    #if options.django-registration == "true":

    if options.verbosity == "true":
        sys.stdout.write('.')
        sys.stdout.flush()

    #need verbosity ?
    if options.verbosity == "full":
        print "Copied files"
    elif options.verbosity == "true":
        print('.'),

    print " "

#=========================================================
# EXPERIMENTS LAUNCHED
#=========================================================
    print "End of program\n";
    print strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
