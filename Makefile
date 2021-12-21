## ********************************************************************* ##
## Copyright 2020-                                                       ##
## Mark Fitch, Univesity of Alaska Anchorage                             ##
##                                                                       ##
## This Makefile provides an easy way to run processes                   ##
## ********************************************************************* ##

XSLDIR = /d/PreTeXt/mathbook/xsl

## Build the html version
## The install commands build the directory structure for the first use
## The rm and cp commands move in the current images needed for html

html: *.ptx
	install -d html
	-rm html/*.html
	-rm -r html/knowl
	-rm -r html/images
	install -d html/images
	-cp -a images/*.svg html/images
	-cp -a images/*.png html/images
	cd html; \
	xsltproc --xinclude $(XSLDIR)/pretext-html.xsl ../techmath.ptx

## Build the pdf version
## The install commands build the directory structure for the first use
## The rm and cp commands move in the current images needed for html

latex: *.ptx
	install -d latex
	-rm latex/*
	-rm -r latex/images
	install -d latex/images
	-cp -a images/*.pdf latex/images
	-cp -a images/*.png latex/images
	cd latex; \
	xsltproc -o techmath.tex --xinclude $(XSLDIR)/pretext-latex.xsl ../techmath.ptx

## Check the PreTeXt schema
schema:
	/c/'Program Files'/Java/jdk-12.0.1/bin/java -classpath ~/xsltproc/jing-trang/build -Dorg.apache.xerces.xni.parser.XMLParserConfiguration=org.apache.xerces.parsers.XIncludeParserConfiguration -jar ~/xsltproc/jing-trang/build/jing.jar ~/xsltproc/mathbook/Schema/pretext.rng /d/Documents/kurse/math251/lessons/techmath.ptx >/d/Documents/kurse/math251/lessons/schemaerrors.txt
