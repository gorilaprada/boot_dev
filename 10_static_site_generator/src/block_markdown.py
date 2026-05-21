import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    if re.match(r"^```\n.*```$", block, re.DOTALL):
        return BlockType.CODE
    if re.match(r"^(>.*\n?)+$", block, re.MULTILINE):
        return BlockType.QUOTE
    if re.match(r"^(- .*\n?)+$", block, re.MULTILINE):
        return BlockType.UNORDERED_LIST
    lines = block.split("\n")
    pattern = "".join(rf"^{i}\. .+\n?" for i, _ in enumerate(lines, 1))
    if re.match(pattern, block, re.MULTILINE):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdown = markdown.split("\n\n")
    return [text.strip() for text in split_markdown if text != ""]

