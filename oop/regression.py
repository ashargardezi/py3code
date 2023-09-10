import re
pattren=r"[A-Z]+law"
text="""
. What constitutes a profession?  The Dlaw society defines a profession as follows:  
When a profession is fully developed it may be described as a body of men and women  
(a) Identifiable by reference to some register or record; 
 (b) recognized as having a special skill and learning in some field of activity in which the public needs protection against incompetence, the standards of skill and learning being prescribed by the profession itself; 
 (c) Holding themselves out as being willing to serve the public; 
 (d) Voluntarily submitting themselves to standards of ethical conduct beyond those required of the ordinary citizen by Claw ,Flaw




"""
# match=re.search(pattren,text)
# print(match)
match=re.finditer(pattren,text)
print(match)
for matches in match:
    # print(matches)
    print(matches.span())
    print(text[matches.span()[0]:matches.span()[1]])