from dataclasses import MISSING, dataclass, field
from typing import List, Union, Optional, Any

import json

import marshmallow_dataclass
import marshmallow.validate
from marshmallow import fields

"""
@dataclass
class Point:
    x: float
    y: float
    Schema: ClassVar[Type[Schema]] = Schema

point: Point = Point(4, 2)

print(point.__repr__)
print(type(point))
print(point.Schema)
"""

"""
Object instance example data: {"reason":"build-finished","success":false}

"""
@dataclass
class BuildPass:
  reason: str
  success: bool

  def __init__(self, reason: str, success: bool) -> None:
    self.reason = reason
    self.success = success

# Opening JSON file
data = {}
with open("./check_sample_log.json") as json_file:
    data = json.load(json_file)


obj: Union[float , int] = 3
print(type(obj))

"""
schema = marshmallow_dataclass.class_schema(BuildPass)()
build: Union[BuildPass, int] = schema.load(data)
print(build)
print(type(build))
"""


@dataclass
class Code:
    code: str
    explanation: str

    def __init__(self, code: str, explanation: str) -> None:
        self.code = code
        self.explanation = explanation

@dataclass
class Text:
    highlight_end: int
    highlight_start: int
    text: str

    def __init__(self, highlight_end: int, highlight_start: int, text: str) -> None:
        self.highlight_end = highlight_end
        self.highlight_start = highlight_start
        self.text = text


@dataclass
class Span:
    byte_end: int
    byte_start: int
    column_end: int
    column_start: int
    file_name: str
    is_primary: bool
    label: str
    line_end: int
    line_start: int
    text: List[Text]
    expansion: str = fields.String(allow_none=True)
    suggested_replacement: str = fields.String(allow_none=True)
    suggestion_applicability: str = fields.String(allow_none=True)

    def __init__(self, byte_end: int, byte_start: int, column_end: int, column_start: int, expansion: None, file_name: str, is_primary: bool, label: str, line_end: int, line_start: int, suggested_replacement: None, suggestion_applicability: None, text: List[Text]) -> None:
        self.byte_end = byte_end
        self.byte_start = byte_start
        self.column_end = column_end
        self.column_start = column_start
        self.expansion = expansion
        self.file_name = file_name
        self.is_primary = is_primary
        self.label = label
        self.line_end = line_end
        self.line_start = line_start
        self.suggested_replacement = suggested_replacement
        self.suggestion_applicability = suggestion_applicability
        self.text = text

@dataclass
class Message:
    rendered: str
    children: List[Any]
    code: Code
    level: str
    message: str
    spans: List[Span]

    def __init__(self, rendered: str, children: List[Any], code: Code, level: str, message: str, spans: List[Span]) -> None:
        self.rendered = rendered
        self.children = children
        self.code = code
        self.level = level
        self.message = message
        self.spans = spans

@dataclass
class Target:
    kind: List[str]
    crate_types: List[str]
    name: str
    src_path: str
    edition: int
    doc: bool
    doctest: bool
    test: bool

    def __init__(self, kind: List[str], crate_types: List[str], name: str, src_path: str, edition: int, doc: bool, doctest: bool, test: bool) -> None:
        self.kind = kind
        self.crate_types = crate_types
        self.name = name
        self.src_path = src_path
        self.edition = edition
        self.doc = doc
        self.doctest = doctest
        self.test = test

@dataclass
class CheckSampleLog:
    reason: str
    package_id: str
    manifest_path: str
    target: Target
    message: Message

    def __init__(self, reason: str, package_id: str, manifest_path: str, target: Target, message: Message) -> None:
        self.reason = reason
        self.package_id = package_id
        self.manifest_path = manifest_path
        self.target = target
        self.message = message



schema = marshmallow_dataclass.class_schema(CheckSampleLog)()
build: Union[CheckSampleLog, int] = schema.load(data)
# print(build)
print(type(build))
print(build.message.spans[0].file_name)
