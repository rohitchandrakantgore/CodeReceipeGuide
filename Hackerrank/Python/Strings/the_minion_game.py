def minion_game(string):
    sub = string.strip()
    player_1, player_2 =0,0 
    for i in range(len(string)):
        if sub[i] in 'AEIOU':
            player_1 += len(string)-i
        else:
            player_2 += len(string)-i
    
    if player_1 > player_2:
        print("Kevin", player_1)
    elif player_2> player_1:
        print('Stuart', player_2)
    else:
        print('Draw') 
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)


# >python Hackerrank/Python/Strings/the_minion_game.py
# BANANA
# Stuart 12