To run this python script you need to have pip installed and then run

pip install selenium

This python script uses Selenium to automate browser tasks, so that it can eventually read from the flags.css file and automatically do the clicking and typing to add all the flairs into reddit's flair selection.

You also need the gecko driver and have Firefox installed. Selenium works with other browsers but the source code would need changing. I choose Firefox because it is available on a lot of different systems and required minimal setup.

To download the gecko driver

https://github.com/mozilla/geckodriver/releases

Problem shooting if your script can't find it

https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#40208762

Add it to your environment path or put it in a place where it can be autodetected like /usr/local/bin for linux, or edit the script to tell python where it is.

Now you can run the python script from cmd prompt or a terminal by typing

python automate.py

when in the same location as the script. The script needs slight configuration for your usage.
