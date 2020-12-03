import math
import sys
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    action_count = int(input())  # the number of spells and recipes in play
    tab_command= []  
    tab_sort = []
    tab_inv = []
    for i in range(action_count):
        # action_id: the unique ID of this spell or recipe
        # action_type: in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        # delta_0: tier-0 ingredient change
        # delta_1: tier-1 ingredient change
        # delta_2: tier-2 ingredient change
        # delta_3: tier-3 ingredient change
        # price: the price in rupees if this is a potion
        # tome_index: in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax
        # tax_count: in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell
        # castable: in the first league: always 0; later: 1 if this is a castable player spell
        # repeatable: for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        action_id, action_type, delta_0, delta_1, delta_2, delta_3, price, tome_index, tax_count, castable, repeatable = input().split()
        action_id = int(action_id)
        delta_0 = int(delta_0)
        delta_1 = int(delta_1)
        delta_2 = int(delta_2)
        delta_3 = int(delta_3)
        price = int(price)
        tome_index = int(tome_index)
        tax_count = int(tax_count)
        castable = castable != "0"
        repeatable = repeatable != "0"
        etat = 0
        
        
        if action_type == "BREW" :  #tableau pour stocker toutes les commandes

            tab_command.append((price,action_id,[delta_0,delta_1,delta_2,delta_3]))
            tab_command.sort()

        
        if action_type == "CAST" : #tableau pour stocker les sorts
            
            tab_sort.append((action_id,castable,(delta_0,delta_1,delta_2,delta_3)))
    
   
    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        tab_inv.append([inv_0, inv_1, inv_2, inv_3])
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    best_id = tab_command[2]
    el_b = best_id[2][0] + tab_inv[0][0]
    el_v = best_id[2][1] + tab_inv[0][1]
    el_o = best_id[2][2] + tab_inv[0][2]
    el_j = best_id[2][3] + tab_inv[0][3]

    
    if el_b <= 0 :


        if tab_sort[0][1] == 1 :  
            a = "CAST"
            b = tab_sort[0][0]

        else : 
            a = "REST"
            b = ""

    
    if el_v <= 0 and tab_inv[0][0] > 0:


        if tab_sort[1][1] == 1 : 
            a = "CAST"
            b = tab_sort[1][0]

        else : 
            a = "REST"
            b = ""
    
        
    
    if el_o <= 0 and tab_inv[0][1] > 0:
       
        
        if tab_sort[2][1] ==1:
            a = "CAST"
            b = tab_sort[2][0]
        else : 
            a = "REST"
            b = ""



    if el_j <= 0 and tab_inv[0][2] > 0:

        
        if tab_sort[3][1]==1:
            a = "CAST"
            b = tab_sort[3][0]

        else :
            a = "REST"
            b = ""

  
    tab_res = [el_b,el_v,el_o,el_j]
    if (el_b) >=0 and (el_v) >=0 and (el_o) >=0 and (el_j) >=0 :
        a = "BREW"
        b = best_id[1]
    

    
    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
    #print("WAIT")
    
    print(a,b)
    print(tab_sort[0][0], file=sys.stderr, flush=True)
    print(tab_res, file=sys.stderr, flush=True)
    

