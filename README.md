# 客户信用度评估模型
中文 | [英文](./readme_en)
## 课题背景
某银行拥有2000行关于客户是否失信的相关特征数据，该银行销售想通过构建模型预测未来的目标客户是否符合自家银行的失信标准，以方便决定接受该客户的信用卡申请。
 ## 数据特征解释

|  |  |
|--|--|
|**ExternalRiskEstimate** |**MSinceOldestTradeOpen** |
| 外部风险预估值| 距离最初交易开始月份 |
| **MSinceMostRecentTradeOpen** | **AverageMInFile** |
|  距离最近一次交易月份| 平均交易月份 |
| **NumSatisfactoryTrades** |**NumTrades60Ever2DerogPubRec** |
|被接受的交易总数量| 60天内贬损性交易记录的数量 |
| **NumTrades90Ever2DerogPubRec** | **PercentTradesNeverDelq** |
|   60天内贬损性交易记录的数量| 从未拖欠债务交易的平均数量 |
| **MSinceMostRecentDelq** | **MaxDelq2PublicRecLast12M** |
|   最近一次拖欠债务月份| 12个月内最大拖欠债务数量 |
| **MaxDelqEver** | **NumTotalTrades** |
|   最大拖欠债务额| 总交易量 |
| **NumTradesOpeninLast12M** | **PercentInstallTrades** |
|   12个月内交易量| 平均分期交易量 |
| **MSinceMostRecentInqexcl7days** | **NumInqLast6M** |
|   最近一次已被调查7天的月份| 6个月内被调查的数量 |
| **NumInqLast6Mexcl7days** | **NetFractionRevolvingBurden** |
|   6个月内已被调查7天的数量| 涉及财务危机的净分数 |
| **NetFractionInstallBurden** | **NumRevolvingTradesWBalance** |
|   分期账户财务危机的净分数| 涉及未偿余额的数量 |
| **NumInstallTradesWBalance** | **NumBank2NatlTradesWHighUtilization** |
|   分期交易的未偿还余额| 有高利用价值银行账户的数量|
| **PercentTradesWBalance** |  |
|   平均交易中的未偿余额| |

## 模型选择
本次课题任务属于二元分类任务，即分类结果只有**拒绝（rejected）**或者**接受（accepted）**，考虑到数据集比较负责，用决策树会有过拟合风险，于是我们决定选择使用基于决策树的高级模型来训练本数据集。
我们使用了梯度提升与随机森林两个模型进行训练，通过比较我们发现梯度提升算法的准确率更高，达到72.73%。

## 交互界面搭建
我们为用户搭建了一个便于预测客户信用额度是否达标的交互界面，如下图所示：
打开界面方法

 - 在interface.py文件中命令行输入指令：`streamlit run interface.py`
 - [点击链接打开](https://fent1-advancedpython-interface-evd5ob.streamlit.app/)
