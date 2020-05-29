# InstaBot

One of the perks of freelancing is the joy of working on all kinds of weird, wonderful, and pretty impressive projects.

My client this time was definitely a unique, determined, and hardworking individual. From my client's words, the Instagram algorithm will recommend users and posts that get a lot of attention from other users. The more comments are posted on an Instagram post, the more likely the Instagram recommendation algorithm will recommend post and user to other users.

My client went ahead and:

- Created, or somehow acquired, over a hundred Instagram accounts, and records the usernames and password to each account in a .txt file
- Created a .txt document containing over a thousand unique comments (yes, I was impressed as well)
- Created a .txt document with links to all his posts

My client requested for an Instagram bot that will:

- Run twice a day, 6am and 11pm,
- Each time, it will iterate through a number of the profiles at random
- Select a unique comment for each of the profiles at random, and...
- Post those comments on a number of my client's Instagram posts.

Such a fun sounding project got me hyped. I immediately got to work working on it and it turned out pretty amazing. The entire program written using Python.

A simple GUI was also created using tkinter to send information about the .txt documents' paths that will be used by the program. These can be altered and swapped out anytime.

The program was made to run on schedule using the Windows Task Scheduler.