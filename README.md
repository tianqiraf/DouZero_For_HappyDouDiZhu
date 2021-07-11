# DouZero_for_JJ: 将DouZero用于JJ斗地主
<img width="500" src="https://gitee.com/daochenzha/DouZero/raw/main/imgs/douzero_logo.jpg" alt="Logo" />

*   本项目基于[DouZero](https://github.com/kwai/DouZero)
*   环境配置请移步项目DouZero
*   模型默认为WP，更换模型请修改start.py中的模型路径
*   运行start.py即可
*   SL (`baselines/sl/`): 基于人类数据进行深度学习的预训练模型
*   DouZero-ADP (`baselines/douzero_ADP/`): 以平均分数差异（Average Difference Points, ADP）为目标训练的Douzero智能体
*   DouZero-WP (`baselines/douzero_WP/`): 以胜率（Winning Percentage, WP）为目标训练的Douzero智能体

## 说明
*   将玩家角色设置为AI，需开局时手动输入**玩家角色、初始手牌、三张底牌**。
*   每轮手动输入其他两位玩家出的牌，AI给出**出牌建议**以及**预计胜率**
*   暂未设计可视化界面，正考虑通过截屏自动识别开局手牌。
