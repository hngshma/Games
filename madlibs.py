def madlib():
    body_part = input("Body Part: ")
    verb = input("Verb: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    adj5 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun_plural_1 = input("Noun (plural): ")
    noun_plural_2 = input("Noun (plural): ")

    madlib = f"Computer programming is {adj1}! The path to becoming a \
programmer begins with hard work a vision in your {body_part}. Through the long journey, \
and {noun_plural_1}, the process will never end. However, once you get the hang of {verb}, it becomes \
a part you, transforming you into a super crazy {adj2} coder. Knowledge of programming \
lets you dominate your {noun1}. You can make your own {noun_plural_2}, anything \
from developing {adj3} software to analyzing data and making predictions about the {noun2}. You can \
maybe even remodel a robot and make him {adj4}. I hope you'll begiin your {adj5} road by \
coming along with me :)"
    
    print(madlib)
