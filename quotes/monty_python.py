import numpy as np

quote = {}

quote[1] = '''
    Strange women lying in ponds distributing swords
    is no basis for a system of -------.
    '''

quote[2] = '''
    I am an enchanter. There are some who call me… ----.
    '''

quote[3] = '''
    King Arthur: “Look, you stupid b***ard, you’ve got no arms left!”
    Black Knight: “Yes I have.”
    King Arthur: “Look!”
    Black Knight: “It’s just a ------ ------…”
    '''

quote[4] = '''
    What sad times are these when passing ruffians can say
    ‘-------’ at will to old ladies.
    '''

quote[5] = '''
    Brother Maynard – bring forth the holy ---- ----!
    '''

quote[6] = '''
    Bridgekeeper: “What… is the air-speed velocity of an unladen swallow?”
    King Arthur: “What do you mean? An ------- or a ---- swallow?”
    Bridgekeeper: “I don’t know that. Aaaaaaaaagh!”
    '''

quote[7] = '''
    Bridgekeeper: “What… is your favourite colour?”
    Sir Lancelot: --------
    Bridgekeeper: “Right. Off you go.”
    '''

quote[8] = '''
    Come and see the violence inherent in the system.
    Help! Help! I’m being -----!
    '''

quote[9] = '''
    He's not Quite dead.
    '''
quote[10] = '''
   How can you tell he is a king?
   '''

def holy_grail(num):
    return quote[num]


if __name__ == '__main__':
    num  = np.random.randint(1, 8)
    holy_grail(num)
