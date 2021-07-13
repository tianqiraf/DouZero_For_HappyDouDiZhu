
AllEnvCard = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
              8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12,
              12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 17, 17, 17, 17, 20, 30]
'''
played_cards_tmp = []
played_cards = {"a":[], "b":[], "c":[]}
player_hand_cards = [3, 3, 4, 6, 6, 6, 7, 7, 7, 8, 9, 9, 10, 11, 11, 13, 14, 17, 17, 20, 30]
for i in list(played_cards.values()):
    played_cards_tmp.extend(i)
cards_not_in_hand = played_cards_tmp + player_hand_cards
print(AllEnvCard)
print(cards_not_in_hand)
other_hand_cards = []
for i in set(AllEnvCard):
    other_hand_cards.extend([i] * (AllEnvCard.count(i) - cards_not_in_hand.count(i)))
print(other_hand_cards)
'''
user_position_code = 1
user_position = "landlord"
Positions = ['landlord_up', 'landlord', 'landlord_down']


# 整副牌减去玩家手上的牌，就是其他人的手牌,分配给另外两个角色
other_hand_cards = []
for i in set(AllEnvCard):
    other_hand_cards.extend([i] * (AllEnvCard.count(i) - use_hand_cards_env.count(i)))

card_play_data_list = [{}]
card_play_data_list[0].update({
    'three_landlord_cards': three_landlord_cards_env,
    ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 0) % 3]: use_hand_cards_env,
    ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 1) % 3]: other_hand_cards[0:17] if (user_position_code + 1) % 3 != 2 else other_hand_cards[17:],
    ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 2) % 3]: other_hand_cards[0:17] if (user_position_code + 1) % 3 == 2 else other_hand_cards[17:]
})


'''
card_play_data_list = [{}]
card_play_data_list[0].update({
    'three_landlord_cards': three_landlord_cards_env,
    user_position: use_hand_cards_env
})

if user_position == "landlord":
    card_play_data_list[0].update({
        "landlord_up": other_hand_cards[0:17],
        "landlord_down": other_hand_cards[17:]
    })
elif user_position == "landlord_up":
    card_play_data_list[0].update({
        "landlord": other_hand_cards[17:],
        "landlord_up": other_hand_cards[0:17]
    })
elif user_position == "landlord_down":
    card_play_data_list[0].update({
        "landlord": other_hand_cards[17:],
        "landlord_up": other_hand_cards[0:17]
    })
else:
    pass
'''