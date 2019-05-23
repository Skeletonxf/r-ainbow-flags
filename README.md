# LGBT and GSM Flag flair for Reddit communities

This was a fork of `r-ainbow-flags` to maintain a few additional flags and many extra cominbations.

As of 2018 Reddit introduced a new site design, and with it came emoji flags.
Shortly after they added emoji support to the old design. Now we can support an arbitrary number of flag combinations with no additional work and 10x less CSS. Adding flag flair to your subreddit is now much much easier than ever.

All CSS has now been rewritten since the fork and this should be considered a seperate project.

## Instructions

1. Go to http://new.reddit.com/r/yoursubreddit.
   Go to mod tools -> community tools -> emojis. Enable emojis in this subreddit. Then click add new emoji and navigate to the `/flag-images` folder. Upload each emoji as an image to reddit using **the same name** as its file name. Reddit will display these names with a `:` on each side.
   [Reference screenshot](https://github.com/Skeletonxf/r-ainbow-flags/raw/master/emoji-flags.png)

2. Go to http://old.reddit.com/r/yoursubreddit/about/stylesheet.
   Paste the CSS from "flags.css" into the bottom of your stylesheet and click the save button.

3. Go to http://old.reddit.com/r/yoursubreddit/about/flair.
   Click on the "User Flair Templates" tab. Add a new row for each flag, check "user can edit?" and fill in the flair text with the name of the emoji putting `:` on each side. Leave the "CSS class" field blank - we no longer need this. The order of the templates does not matter, so choose whatever makes most sense for your subreddit. /r/Demisexuality for instance puts the Demi flag first and then all others alphabetically.
   [Reference screeshot](https://github.com/Skeletonxf/r-ainbow-flags/raw/master/flair-page-reference.png) (Note: Screenshot is not updated to include the Aromantic flag)  
   As you can see in the screenshot it may also be useful for you to include the most common pairs of flags users in your subreddit might want below the list of individual flags.
4. Check off the "allow users to assign their own flair" box atop the page so people can select their own flags and create their own combinations of flags.

Congratulations, you're done!
