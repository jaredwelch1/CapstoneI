you need to run it in python3 (not compatible with python2), and it needs the newspaper library + dependencies installed:  
http://newspaper.readthedocs.io/en/latest/user_guide/install.html

the program lets you scrape all the articles from any news site, but be careful - some sites don't like that and might ban  
your IP if you go overboard with it. You can figure out if it's allowed from the site's <homepage>/robots.txt or terms of  
service (cnn is a safe place to try it out)  


# TO DO

- Make script receive URL from command line
- Give optional flag in command line for number of articles? 
- Create bash script
  - should have a list of URLS
  - should call script for each URL and save output into a log file (script can just output errors to STDOUT)
 
