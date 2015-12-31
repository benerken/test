#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, getopt


def main(argv):
    source=""
    outputfile = ""
    inputfile  = ""
    path=""

    for arg in argv:
        source += arg + " "
        ### Find the output filename
        if ("OutputFile" in arg):
            tmp=arg.split("=",1)
            outputfile=tmp[1]

    inputfile=argv[-1]
    path,tail = os.path.split(inputfile)
    print "Path   => "+path
    print "Input  => "+inputfile
    print "Output => "+outputfile

    ### Call Apache Tika to convert to XML
    print "[command] java -jar /opt/apache-tika/tika-app-1.11.jar -x "+inputfile+" > "+outputfile.replace("PDF_","XHTML_PDF_")
    cmd="java -jar /opt/apache-tika/tika-app-1.11.jar -x "+inputfile+" > "+outputfile.replace("PDF_","XHTML_PDF_")
    os.system(cmd)

    ### Call GhostScript to convert to PDF/A
    print "[command] gs " + source
    cmd="gs "+source
    os.system(cmd)
    
    ### list all files in working directory
    print "[command] ls -l " + path
    cmd="ls -l "+path
    os.system(cmd)


if __name__ == "__main__":
    main(sys.argv[1:])
    
