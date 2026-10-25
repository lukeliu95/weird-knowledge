---
name_zh: "面向对象编程（类与子类继承）"
name_en: "Object-oriented programming (class and subclass inheritance)"
proposer: "Ole-Johan Dahl、Kristen Nygaard（Simula 67）；受 Tony Hoare 1966 年“记录子类”想法影响"
year: "1967"
type: 方法论
verified: true
---

# 面向对象编程（类与子类继承）（Object-oriented programming (class and subclass inheritance)）

## 一句话

把程序组织成类：子类继承父类的数据和行为，只覆盖或增加自己特有的部分，共有的行为写一次、处处复用；继承最早在 Simula 67 里实现。

## 原始出处

- Class and Subclass Declarations，Ole-Johan Dahl、Kristen Nygaard，1967 年 IFIP 模拟语言工作会议（Springer《Software Pioneers》2002 年重印），https://doi.org/10.1007/978-3-642-59412-0_7
- The Development of the SIMULA Languages，Kristen Nygaard、Ole-Johan Dahl，ACM History of Programming Languages，1978，https://doi.org/10.1145/800025.1198392
- Inheritance (object-oriented programming)，维基百科（Hoare 1966 提出记录子类，Dahl 与 Nygaard 1967 提出类与子类，首先被 Simula 67 采用），https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)
- 争议：继承有前身：维基百科说 Tony Hoare 1966 年在技术报告 Record Handling 里提出“记录子类”，Dahl 与 Nygaard 受其影响在 1967 年提出类与子类声明，并首先在 Simula 67 实现。“面向对象”这个叫法和它后来的推广另有来历，这里只记继承这一机制的出处。

## 更底层的源头

- [模块化编程](modular-programming.md) · 关系：相近
- [信息隐藏](information-hiding.md) · 关系：相近

## 指向它的新知识

| 新知识 | 关系 | 强弱 |
|---|---|---|
| [agent 的外壳代码按"类继承"分家：按任务的共同毛病长出一族专用外壳，先跑一遍通用版看出毛病再挑；比只练一个全局外壳分数高、搜索快](../clips/2026-10-25-li-object-oriented-harness.md) | 直接源自 | 强 |
