from __future__ import annotations

from typing import Optional


class ApiDoc:
    label: str
    name: str
    content: FunctionContent | ClassContent


class FunctionContent:
    description: str
    parameters: list[Parameter]
    ret: Return
    shape: list[Shape]
    code_example: str


class ClassContent:
    description: str
    parameters: list[Parameter]
    ret: Return
    shape: list[Shape]
    methods: list[ClassMethod]
    attributes: list[ClassAttribute]
    code_example: str


class Parameter:
    name: str
    type: list[str]
    optional: bool
    description: str
    default_value: Optional[str]
    default_value_description: Optional[str]  # TODO


class Shape:
    name: str
    description: str


class Return:
    type: list[str]
    description: str


class ClassMethod:
    name: str
    content: FunctionContent


class ClassAttribute:
    name: str
    description: str
