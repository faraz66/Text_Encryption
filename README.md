# Text_Encyrption

The Algorithm Encrypt's the User message with the help of Substituion and Transposition Techniques,to a Cipher Text

**Shift Cipher:**

For every letter in the message M :
1. Convert the letter into the number that matches its order in the alphabet starting from 0, and call this number X.
( A=0, B=1, C=2, ...,Y=24, Z=25)
2. Calculate: **Y = (X + K) mod 26**
3. Convert the number Y into a letter that matches its order in the alphabet starting from 0.
(A=0, B=1, C=2, ...,Y=24, Z=25)

For Example: We agree with our friend to use the Shift Cipher with key K=19 for our message. 
We encrypt the message "KHAN", as follows:DATG

**Transposition Cipher:**

**1.Reverse Transposition:**

 Here the Plain-text is just Reversed to generate the cipher text 
 
 example:  
 plain-text: Hello
 
 cipher-text: olleH

**2.Even_Odd Cipher:**

Here we assign a Numbers to the characters(plain-text) from 0 and accordingly separate it as even or odd and add join the strings.

ex:

0 1 2 3 4 5 6 7 8 9 10 11 

G o o d _ m o r n i n  g

even_text= Go_onn

odd_text = odmrig

Now,we Join Both The Strings

Cipher_text = Go_onnodmrig


 


