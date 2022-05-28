# DouZero_For_Happy_DouDiZhu: 将DouZero用于欢乐斗地主实战
<img width="500" src="https://raw.githubusercontent.com/kwai/DouZero/main/imgs/douzero_logo.jpg" alt="Logo" />

*   本项目基于[DouZero](https://github.com/kwai/DouZero)
*   环境配置请移步项目DouZero
*   模型默认为WP，更换模型请修改start.py中的模型路径
*   运行main.py即可
*   SL (`baselines/sl/`): 基于人类数据进行深度学习的预训练模型
*   DouZero-ADP (`baselines/douzero_ADP/`): 以平均分数差异（Average Difference Points, ADP）为目标训练的Douzero智能体
*   DouZero-WP (`baselines/douzero_WP/`): 以胜率（Winning Percentage, WP）为目标训练的Douzero智能体

## 说明
*   欢乐斗地主窗口模式最大化运行，屏幕分辨率1920x1080。由于设计像素级操作，运行出错请检查截图区域坐标（位于`MyPyQT_Form`类中的`__init__`函数内）
*   窗口移至右下角，避免遮挡手牌，历史牌，底牌区域。
*   **本项目仅供学习以及技术交流，请勿用于其它目的，否则后果自负。**

## 使用步骤
1. 确认环境正常，等待手牌出现、底牌出现、地主角色确认后，点击**开始**，耗时几秒完成识别。
2. 窗口内显示识别结果，地主角色使用淡红色标出。识别完成自动开始记录出牌。
3. 观察AI建议的出牌，在游戏中手动选择并打出。
4. 游戏结束后弹出对话框提示输赢。
5. 识别错误或无反应可通过**结束**按钮停止本局。至于游戏，就自己手动打完吧。
6. 坐标自行调整请使用pos_debug.py

## 潜在Bug
*   王炸时出牌特效时间较长，有一定几率导致只能识别出一个王。


## 鸣谢
*   本项目基于[DouZero](https://github.com/kwai/DouZero)
*   借鉴了[cardRecorder](https://github.com/ZDZX-T/cardRecorder)项目的部分代码以及模板图片，用于识别扑克牌

## 相关链接
*   博客链接：[天启的博客](https://tqraf.cn/2021/07/DouZero-For-HappyDouDiZhu.html)
*   文章链接：[知乎专栏](https://zhuanlan.zhihu.com/p/389439772)
*   演示视频链接：[视频](https://b23.tv/9WFP5F)
*   欢迎加入QQ交流群：754619468，入群口令：DouZero
