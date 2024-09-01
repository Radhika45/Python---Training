#Write a python script to print the current date in the following format Sun May 29 02:26:23 IST 2017

import time; 
local_time=time.localtime();
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",local_time));  #returns the formatted time 

''' 
 %a : Abbreviated weekday name.
 %b : Abbreviated month name.
 %d : Day of the month as a decimal number [01,31].
 %H : Hour (24-hour clock) as a decimal number [00,23].
 %M : Minute as a decimal number [00,59].
 %S : Second as a decimal number [00,61].
 %Z : Time zone name (no characters if no time zone exists).
 %Y : Year with century as a decimal number.'''
