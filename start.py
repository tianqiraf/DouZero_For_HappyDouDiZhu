import os
from douzero.evaluation.simulation import evaluate

if __name__ == '__main__':

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    print("\n【3 4 5 6 7 8 9 10 J Q K A 2 小王 大王】分别对应【3 4 5 6 7 8 9 T J Q K A 2 X D】,T表示Ten，X表示小，D表示大\n")
    print("出牌请按照 TTTJJJQQQ345 这样的形式输入，要不起请直接按Enter\n")
    while 1:
        evaluate('baselines/douzero_WP/landlord.ckpt',
                 'baselines/douzero_WP/landlord_up.ckpt',
                 'baselines/douzero_WP/landlord_down.ckpt')
