LGBT-Themed Flair for Reddit communities
========================================

**This fork replaces the split flags over at [/r/ainbow](http://www.reddit.com/r/ainbow/) 
for flags side by side in the user's flair, saving on the number of images 
counting towards reddit's cap and making it easier to add new flags into the project.
Thus this fork only contains 8 images of flags, but still supports many 
combinations by placing each flag image in the user's flair together**


Instructions
------------

Steps 1-2 will happen on this page: 
http://www.reddit.com/r/yoursubreddit/about/stylesheet

Steps 3-5 will happen on this page: 
http://www.reddit.com/r/yoursubreddit/about/flair

1. Under the "images" section, upload each of the PNG's in this folder. 
   Reddit will suggest a name in the "new image name" box. Keep that 
   name, or you'll have to change the CSS a bit. 
2. Paste the CSS from "flags.css" into the bottom of your stylesheet.
3. Go to the flair page mentioned above, and click on the "Edit Flair
   Templates" tab. There are 16 CSS classes to enter by default; all 
   will have "user can edit?" checked. The class names are listed below, 
   and the order listed below is preferred but not required. 
4. In the "Flair Text" box next to 'noflag', enter the word "Custom". 
   All other templates may leave the "Flair Text" blank. 
5. Check off the "allow users to assign their own flair" box atop the 
   page so people can select their own flags. 
   
Congratulations, you're done!
   
CSS Class Names
---------------

These are the CSS classes you will add to the flair template page. For 
reference, this is /r/demisexuality's order as of July 2016: 

 * ainbow
 * pan
 * bi
 * het
 * ace
 * demi
 * genderqueer
 * trans
 * ally
 * noflag
 * demi-ainbow
 * demi-pan
 * demi-bi
 * demi-het
 * trans-ainbow
 * trans-pan
 * trans-bi
 * trans-ace
 * trans-demi
 * trans-demi-ainbow
 * trans-demi-pan
 * trans-demi-bi
 * trans-demi-het
 * genderqueer-ainbow
 * genderqueer-pan
 * genderqueer-bi
 * genderqueer-ace
 * genderqueer-demi
 * genderqueer-demi-ainbow
 * genderqueer-demi-pan
 * genderqueer-demi-bi
 * genderqueer-demi-het

Notes
-----

The CSS class names are invisible to the end user. 

Position 9 in the template list used to be the 'none' class, which removed 
the flag. Now that reddit has a 'Remove Flair' option, we've repurposed 
this positon for the 'noflag' class, which allows for freeform text in the 
standard style of reddit flair.

The original implementation supported custom text as hover text rather 
than static text. We later decided that showing text alongside the flag at 
all times was preferable, and as of the latest update, hover text is 
incompatible with the new noflag template. Nonetheless: if you want the old 
hover text style, replace the span.flair rule with the following: 

	span.flair
	{
	   text-indent: -30000px;
	}
	
	span.flair:hover
	{ 
	   text-indent: 22px;
	   width: auto;
	   min-width: 15px;
	   padding-right: 3px;
	}

Original Acknowledgments
---------------

Custom text was initially implemented by reddit user kkress, and the 
blended flags were conceived and designed by WTFcannuck. RES NightMode
optimizations were added by nekosune. Thanks so much to you all! 

If you have any questions or issues about the origional version of this fork, 
message joeycastillo on reddit. For questions or issues about this forked 
version message skeletonxf on reddit.
