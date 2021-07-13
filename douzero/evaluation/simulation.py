from douzero.env.game import GameEnv
from .deep_agent import DeepAgent

EnvCard2RealCard = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q',
                    13: 'K', 14: 'A', 17: '2', 20: 'X', 30: 'D'}

RealCard2EnvCard = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
                    'K': 13, 'A': 14, '2': 17, 'X': 20, 'D': 30}

AllEnvCard = [3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
              8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12,
              12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 17, 17, 17, 17, 20, 30]


def evaluate(landlord, landlord_up, landlord_down):
    # 输入玩家的牌
    user_hand_cards_real = input("请输入你的手牌, 例如 333456789TJQKA2XD:")
    # user_hand_cards_real = "34666777899TJJKA22XD"
    use_hand_cards_env = [RealCard2EnvCard[c] for c in list(user_hand_cards_real)]
    # 输入玩家角色
    user_position_code = int(input("请输入你的角色[0：地主上家, 1：地主, 2：地主下家]:"))
    # user_position_code = 1
    user_position = ['landlord_up', 'landlord', 'landlord_down'][user_position_code]
    # 输入三张底牌
    three_landlord_cards_real = input("请输入三张底牌, 例如 2XD:")
    # three_landlord_cards_real = "2XD"
    three_landlord_cards_env = [RealCard2EnvCard[c] for c in list(three_landlord_cards_real)]

    # 整副牌减去玩家手上的牌，就是其他人的手牌,再分配给另外两个角色（如何分配对AI判断没有影响）
    other_hand_cards = []
    for i in set(AllEnvCard):
        other_hand_cards.extend([i] * (AllEnvCard.count(i) - use_hand_cards_env.count(i)))

    card_play_data_list = [{}]
    card_play_data_list[0].update({
        'three_landlord_cards': three_landlord_cards_env,
        ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 0) % 3]: use_hand_cards_env,
        ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 1) % 3]: other_hand_cards[0:17] if (user_position_code + 1) % 3 != 1 else other_hand_cards[17:],
        ['landlord_up', 'landlord', 'landlord_down'][(user_position_code + 2) % 3]: other_hand_cards[0:17] if (user_position_code + 1) % 3 == 1 else other_hand_cards[17:]
    })
    # 生成手牌结束，校验手牌数量
    if len(card_play_data_list[0]["three_landlord_cards"]) != 3:
        print("底牌必须是3张\n")
        return
    if len(card_play_data_list[0]["landlord_up"]) != 17 or \
        len(card_play_data_list[0]["landlord_down"]) != 17 or \
        len(card_play_data_list[0]["landlord"]) != 20:
        print("初始手牌数目有误\n")
        return

    # print(card_play_data_list)
    card_play_model_path_dict = {
        'landlord': landlord,
        'landlord_up': landlord_up,
        'landlord_down': landlord_down}

    print("创建代表玩家的AI...")
    players = {}
    players[user_position] = DeepAgent(user_position, card_play_model_path_dict[user_position])

    env = GameEnv(players)
    for idx, card_play_data in enumerate(card_play_data_list):
        env.card_play_init(card_play_data)
        print("开始出牌\n")
        while not env.game_over:
            env.step()
        print("{}胜，本局结束!\n".format("农民" if env.winner == "farmer" else "地主"))
        env.reset()



