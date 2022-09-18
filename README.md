# Next-Generation-Paddle-Docs

本分支用于生成下一代paddlepaddle文本格式。

相对于之前的paddle/docs仓库，本仓库的变更点如下：

1. 新增 switch_codes 文件夹用于存放转换格式相关的代码
2. 新增 struct 路径，用于存放和 docs 一一对应的格式化文件，如存在 docs/api/paddle/add_cn.rst ，则对应存在 struct/api/paddle/add_cn.rst，目前仅考虑构建 docs/api/paddle 和 struct/api/paddle的对应关系
3. struct中存储文件的格式未定

Liyulingyue
2022/9/18
