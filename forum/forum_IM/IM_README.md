
# Chat Program for Flask based forum in Python3(.8.9)
## Developed for ZCW Deta Zeta group 

## General Decisions to be made

#### How to handle user authentication?

#### How to store user information?

### Generic features: Status' (Op, Mod, User, etc)
There are several modes that can be set on a user:
- o = Owner, all privileges 
- a = Admin, most privileges (except for changing Admin flags)
- m = Moderator, most Admin privileges except for changing Admin and Banned flags 
- t = Trusted, just a mark of respect 
- q = Quiet, can only speak in asides 
- s = Silent, cannot talk at all 
- b = Banned. 
Banning capability (By Username, IP Address, etc)
Connect DB Back to Forum DB 
?? Add More Here ??
#### Determine how many and what kinds of back ends (Telnet, SSH, HTTP, etc)
    Currently have local net back end
    ideal would probably be HTTPs://
    ?? Open for expansion ??
#### Determine how many and what kinds of front ends (Telnet, SSH, HTTP, Pygame, Tkinter, etc)
    Currently Tkinter Pop-out Front end
    Inspiration is from AOL AIM

?? Add more front/back ends ??

?? Add more general decisions to be made ??

