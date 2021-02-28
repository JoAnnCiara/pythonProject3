# pythonProject3

A program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each of the messages.
I pulled the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon; 
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008.
Then I accumulated the counts for each hour, printed out the counts,
and sorted by hour.
