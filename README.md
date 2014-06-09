#Pyramid-base

This is a base for a pyramid project in python3

It should work with any environnement, but it was only test with :
 * openshift online

##Openshift Online Integration

###Creation of the openshift application
	
	rhc app create APPNAME python-3.3
	cd YOUR_WORKSPACE
	rhc git-clone APPNAME
	cd APPNAME

###Add the base of pyramid

	git remote add upstream -m master https://github.com/SabatierBoris/Pyramid-base.git
	git pull -s recursive -X theirs upstream master
	git push

###Enjoy !!!

#Help
Until wsgi.py it run, it's should work with it. But I don't have time for testing every environements.
So do not hesitate to add your integration's procedure.
