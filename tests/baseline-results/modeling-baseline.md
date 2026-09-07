# 基线建模与验证建议

## M1：24 个观测、单预测变量、近线性且方差齐性

**基线**：报告均值预测（所有样本都预测因变量的训练均值），并给出其 MAE/RMSE，作为“不使用预测变量”的参照。

**主模型**：使用一元普通最小二乘线性回归
\[
y=\beta_0+\beta_1x+\varepsilon.
\]
这是数据特征和目标下最合适的首选：散点近线性、残差方差齐性，并且 \(\beta_1\) 能直接解释为“在其他条件不变（此处无其他协变量）时，\(x\) 每增加 1 单位，\(y\) 的平均变化量”。报告系数估计、95% 置信区间、p 值、调整 \(R^2\)、RMSE，并用原始单位解释效应大小。不要因样本仅 24 个而把复杂非线性或高参数模型作为主结论。

**验证**：由于不能假定还有额外数据，采用留一交叉验证（LOOCV）或重复 5 折交叉验证（折数受样本量限制时以 LOOCV 为主），报告交叉验证 RMSE/MAE 及其相对均值基线的改进。补充残差对拟合值图、Q-Q 图、杠杆值/Cook 距离，检查线性、正态性是否严重偏离及单点影响；必要时作稳健回归敏感性分析，但仍以 OLS 为主模型。若预测用途明确，可同时报告预测区间，避免把均值响应的置信区间误作个体预测区间。

## M2：60 个月、趋势与年度季节性

按时间顺序切分，绝不随机打乱。一个实用设计是：第 1--36 个月为训练集，第 37--48 个月为验证集，第 49--60 个月为最终测试集。训练期至少覆盖 3 个完整年度，可识别 12 个月季节性和趋势；验证、测试期各覆盖一个完整年度，可比较每个月份的预测表现，且测试集完全不参与模型、特征、超参数和方案选择。

在训练集上拟合候选模型，例如季节性朴素法（预测等于去年同月）、带趋势和季节项的 ETS/Holt-Winters、带季节项的 SARIMA 或季节回归。用验证集选择模型、季节处理和超参数；确定后用前 48 个月重新拟合一次，仅在最后 12 个月评估。主指标使用 MAE、RMSE 和 sMAPE/MASE；MASE 应以季节性朴素法为缩放基准，便于判断是否真正超过“去年同月”的简单方法。

为降低单一切分偶然性，可在模型筛选阶段加做滚动起点（expanding-window）回测：例如以 36 个月起训，每次向前滚动 1 个月，预测未来 1、3、6、12 个月并汇总误差。最终测试集仍保持封存。此切分有效，因为每一次训练都只使用预测时点之前可获得的信息，验证和测试模拟真实的向前预测，也避免季节信息泄漏。

## M3：六个备选方案、八个部分相关指标

先建立“方案 × 指标”决策矩阵，统一指标方向和量纲：

- 效益型指标按“越大越好”处理；
- 成本型指标按“越小越好”处理；
- 区间最优型指标以目标区间 \([L,U]\) 为中心，区间内得满分，区间外按到最近边界的标准化距离递减；不能简单当作效益或成本型。

对极端值敏感时，采用稳健的 min--max 标准化（可先温莎化）；同时保留原始值、方向和变换公式，保证可复核。主排序可使用加权 TOPSIS：先加权标准化，计算至正、负理想解的距离，再以贴近度排序。TOPSIS 直观地把“接近最佳、远离最差”结合起来，适合少量方案、多维指标的综合比较。

权重不应完全由指标波动决定。建议以 AHP/专家成对比较获得政策与业务偏好权重，并用熵权法作为数据驱动的第二套权重；主结果可取经一致性检验后的 AHP 权重，熵权和等权作为敏感性对照。对高度相关指标，应先报告相关矩阵与潜在重复计量；若两个指标实质上测量同一概念，可合并为一个一级维度后再分配维度权重，或在该相关指标组内限制总权重，避免同一信息被重复加权。

稳定性检验至少包括：(1) 等权、AHP、熵权三套权重下的名次；(2) 各权重在基准值附近如 ±20% 扰动后重新归一化的蒙特卡洛模拟；(3) 原始数据在测量误差/区间范围内扰动后的重复排序；(4) 与加权和法或 VIKOR 的方法交叉检验。报告每个方案的平均名次、第一名概率、名次区间和 Spearman/Kendall 名次相关。若第一名频繁变化，应如实表述为“优势不稳健”，而非强行给出唯一最优。

## M4：五个设施的整数分配、线性约束

将决策量定义为整数 \(x_i\)（设施 \(i=1,\ldots,5\) 的分配量），以线性目标和线性容量、需求、预算约束建立整数线性规划（ILP/MILP）：
\[
\max \sum_i c_i x_i,\quad
0\le x_i\le \text{cap}_i,\quad
\sum_i a_{ki}x_i\le b_k,\quad
\sum_i d_i x_i\ge D,\quad
\sum_i p_i x_i\le B,\quad x_i\in\mathbb Z.
\]
目标可为最小总成本、最大服务量或最大收益；若目标未指定，应把它明确为待决策方确认的业务目标，不能暗自替换。需求既可能是总量下限，也可能是逐设施/逐区域约束，应按实际业务含义建模。

**求解策略**：优先使用成熟 MILP 求解器的 branch-and-bound/branch-and-cut（如 HiGHS、CBC、SCIP、Gurobi 或 CPLEX），设定可复现的时间限制、最优性 gap 和随机种子。五个设施且约束线性时，这会给出可证明最优解或明确的最优性缺口，优于先用启发式法。

**基线**：给出可行的规则法，例如按单位收益/成本或单位服务成本排序后贪心分配，并在每一步检查容量、预算和需求；如允许，也报告线性规划松弛解作为整数性成本的下界/上界参照。比较 MILP 与贪心的目标值、可行性和计算时间。验证包括逐条代回所有约束、单位核查、边界情形测试（预算很紧、容量饱和、需求不可行）以及对成本/需求的情景敏感性分析；对不可行情形由求解器给出诊断或最小违约松弛模型。

## M5：非凸路径规划启发式

不能凭单次最好结果证明有效。证据包应包括：

- **重复运行**：在同一实例上以不同随机种子独立运行至少 30 次（若成本允许可更多），固定代码、参数和停止条件，记录每次目标值、运行时间、可行性和种子。
- **基线比较**：至少比较最近邻/贪心构造法，以及局部搜索（如 2-opt/3-opt）；小规模实例可增加精确 MILP/动态规划最优解作真值，大规模实例可与公认启发式或已有方法在相同预算下比较。
- **可行性证据**：每次运行均自动核验起终点、每个节点访问约束、车辆容量、时间窗、连通性、重复/遗漏访问、路线长度和其他业务约束；违规解不应参与“最佳目标”比较。报告可行解比例和违反约束的最大/平均程度（若采用软约束）。
- **收敛证据**：保存目标值随迭代或时间变化的轨迹，绘制中位数与四分位带，并报告达到最终值 95% 所需迭代/时间。注意这只能说明算法在给定停止准则下趋于稳定，不能证明全局最优。
- **稳定性证据**：报告最优、均值、中位数、标准差、变异系数、分位数、最差值和相对基线/最优解的最优性缺口；以箱线图或经验分布显示结果。对关键超参数做小型网格/单因素敏感性分析，并在规模、密度、约束紧度不同的实例族上重复实验。

所有方法必须使用同一实例、硬件环境、时间预算和目标定义。若启发式的均值显著优于基线、可行率接近 100%、方差可接受且在多类实例上一致，才能声称其具有实用优势；“找到更短路径一次”不足以构成结论。

## M6：训练集 \(R^2=0.99\)

**结论**：仅凭训练集 \(R^2=0.99\) 不能判断模型可靠。它可能反映真实强信号，也可能来自过拟合、数据泄漏、目标泄漏、异常值、过多自由度或不恰当的评估方式。尤其在复杂模型或样本小、特征多时，训练拟合度几乎不提供泛化保证。

下一步检查：

1. 使用未参与开发的时间后测试集、独立测试集或严格交叉验证，报告测试/OOF \(R^2\)、MAE、RMSE；比较训练与测试差距。
2. 审计数据切分和特征生成流程：任何标准化、缺失值填补、特征选择、PCA、目标编码和超参数选择都必须仅在训练折内拟合；检查特征是否包含结果发生后才可得的信息或目标的直接变体。
3. 与均值预测、简单线性模型和领域朴素规则比较；若复杂模型在外样本不胜出，0.99 没有决策价值。
4. 检查残差：残差图、Q-Q 图、异方差、非线性、时间/群组自相关及系统性偏差；按关键子群体分别计算误差。
5. 检查影响点和重复记录，报告杠杆值、Cook 距离及删去高影响点后的敏感性结果。
6. 核对样本量、特征数、有效自由度和正则化强度；对可解释模型报告调整 \(R^2\) 与系数置信区间。
7. 若数据有时间、个体或空间依赖，采用相应的分组/时间块交叉验证，不能随机拆分同一实体的相邻记录。

## C1：PCA 与 XGBoost 的组合是否构成创新

**判断**：把 PCA 接到 XGBoost 前面本身通常不是方法创新，而是常见的降维加预测模型组合。PCA 是无监督线性投影，XGBoost 是能处理非线性和变量交互的树集成；二者的组合是否有价值取决于问题约束、与强基线相比的外样本表现、稳健性和是否带来可验证的新机制。不能因模型名称叠加或训练指标上升就称为创新。若提出了针对特定结构的新特征构造、保留监督信息的降维策略、明确理论性质，或在严格实验中稳定解决了既有方法的限制，才可能形成有限且可证实的创新主张。

**验证设计**：使用嵌套交叉验证（时间/分组数据则使用对应的嵌套时间块或分组切分）。外层折只用于最终比较；每个内层折中独立拟合 PCA、选择主成分数和 XGBoost 超参数，绝不可先在全数据拟合 PCA。比较至少五组：

1. 均值/季节性朴素等任务相关朴素基线；
2. 原始特征的线性或正则化线性模型；
3. 原始特征 XGBoost；
4. PCA 后的线性模型；
5. PCA + XGBoost。

在每个外层测试折报告主损失指标（回归为 MAE/RMSE，分类为 AUROC、PR-AUC、校准等）、运行时间、内存与模型复杂度。用配对的外层折误差差值及其置信区间（或适合重复交叉验证的配对检验）判断 PCA+XGBoost 是否稳定优于“原始特征 XGBoost”，这才是该组合的直接增益检验。进一步改变 PCA 保留方差阈值/成分数、随机种子、噪声水平和样本规模，观察优势是否持续；做消融分析确认收益来自 PCA 而非调参预算不一致。最后在完全封存的独立测试集复现一次。若该组合未显著优于原始 XGBoost，或收益小于不确定性与可解释性损失，则应将它作为备选工程方案，而不是创新贡献。

## Evidence-based scoring

| Scenario | Observable behavior | Pass/Fail | Failure pattern that guidance must address |
|---|---|---|---|
| M1 Simple linear prediction | Chooses a mean-prediction baseline, interpretable OLS main model, and small-sample out-of-sample plus residual/influence checks without assuming more data. | Pass | None observed; do not add redundant guidance. |
| M2 Time-series split | Uses ordered train/validation/test periods, keeps the final year sealed, adds expanding-window backtesting, and explains leakage prevention and seasonal coverage. | Pass | None observed; do not add redundant guidance. |
| M3 Evaluation model | Handles benefit, cost, and interval-preferred indicators separately; addresses correlated indicators, preference-aware weights, and multi-form ranking sensitivity. | Pass | None observed; do not add redundant guidance. |
| M4 Linear integer optimization | Formulates an ILP/MILP, prefers a mature exact solver, supplies greedy and LP-relaxation baselines, and checks feasibility and sensitivity. | Pass | None observed; do not add redundant guidance. |
| M5 Heuristic stability | Requires repeated seeded runs, fair baselines, automated feasibility checks, convergence traces, dispersion statistics, and parameter/instance sensitivity. | Pass | None observed; do not add redundant guidance. |
| M6 High R-squared | Rejects training R-squared alone as reliability evidence and lists out-of-sample evaluation, leakage, baselines, residuals, influence, complexity, and dependency-aware splits. | Pass | None observed; do not add redundant guidance. |
| C1 Innovation claim | Rejects model-name stacking as innovation and proposes leakage-safe nested comparison, ablation, uncertainty, robustness, and a sealed test. | Pass | None observed; do not add redundant guidance. |


