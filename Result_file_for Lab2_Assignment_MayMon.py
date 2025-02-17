Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/User/Downloads/test.py
hello
>>> 
=================== RESTART: C:/Users/User/Downloads/test.py ===================
King has been added to the zoo!
EE has been added to the zoo!
Baki has been added to the zoo!

Animals in the zoo:
King is a Lion aged 5 years
EE is a Eagle aged 3 years
Baki is a Snake aged 2 years

Zoo animals are making sounds:
King says: Roar!
EE says: Screech!
Baki says: Hiss!

Feeding all animals:
Traceback (most recent call last):
  File "C:/Users/User/Downloads/test.py", line 112, in <module>
    main()
  File "C:/Users/User/Downloads/test.py", line 109, in main
    my_zoo.feed_all_animals()
  File "C:/Users/User/Downloads/test.py", line 88, in feed_all_animals
    print(animal.feed())
AttributeError: 'Lion' object has no attribute 'feed'
