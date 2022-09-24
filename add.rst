add
-------------------------------

.. py:function:: paddle.add(x, y, name=None)

输入 :attr:`x` 与输入 :attr:`y` 逐元素相加，并将各个位置的输出元素保存到返回结果中。计算公式为：

.. math::
    out = x + y

.. note::
   ``paddle.add`` 遵守广播机制，如您想了解更多，请参见 :ref:`cn_user_guide_broadcasting`。

参数
:::::::::
	- **x** (Tensor) - 输入的 Tensor，数据类型为 float32、float64、int32 或 int64。
	- **y** (Tensor) - 输入的 Tensor，数据类型为 float32、float64、int32 或 int64。
	- **name** (str，可选) - 具体用法请参见 :ref:`api_guide_Name`，一般无需设置。默认值为 None。

返回
:::::::::
	Tensor，维度和数据类型都与 :attr:`x` 相同，存储运算后的结果。

代码示例
::::::::::
	COPY-FROM: paddle.add
