# 原始资料 · 数学基础

> 用法：index.md 是最小补丁。数学直觉想补得更扎实时按下面来；每个都标了「只看哪部分」，别陷进去。

## 视觉直觉类（强烈推荐，有中文字幕）

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 1 | 3Blue1Brown《神经网络》系列 | YouTube/B站官方中文 | 第 3-4 集（梯度下降）：梯度与「沿坡走」的视觉解释，40 分钟 |
| 2 | 3Blue1Brown《微积分的本质》 | 同上 | 第 1-2 集：导数直觉；配合本讲第 4 节 |
| 3 | Seeing Theory（Brown 大学概率可视化） | https://seeing-theory.brown.edu | 「概率与推断」前两章：期望/大数定律的交互演示，30 分钟玩完 |

## 教材类（免费官方 PDF，只查不读）

| # | 资料 | 定位 | 看什么 |
|---|---|---|---|
| 4 | Mathematics for Machine Learning（Deisenroth et al.） | https://mml-book.github.io | Ch.6（概率与分布）：想要熵/期望的严格定义时查；其余章节跳过 |
| 5 | Karpathy《The spelled-out intro to language modeling》 | YouTube 搜标题 + [colab](https://github.com/karpathy/ng-video-lecture) | 看交叉熵损失在代码里长什么样（F.cross_entropy 那几行），代码侧打通 |

## 使用建议

- 本讲第 1、3 节（期望、交叉熵）是硬前置，必须过关；第 4 节（梯度/log/sigmoid）可以在第 2、5 讲卡住时再回来
- 3Blue1Brown 系列 tempting 但很长：只看标注的两三集，**不要**顺着推荐一路看下去（这是补丁，不是数学系课程）
