from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered list"
    ORDERED_LIST = "Ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    block_strings = []
    for block in blocks:
        striped_block = block.strip()

        if striped_block != "":
            block_strings.append(striped_block)
    return block_strings

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n"):
        lines = block.split("\n")
        if lines[-1] != "```":
            return BlockType.PARAGRAPH
        return BlockType.CODE
    elif block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if line.startswith(">") != True:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if line.startswith("- ") != True:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        lines = block.split("\n")
        counter = 1
        for line in lines:
            if line.startswith(f"{counter}. ") != True:
                return BlockType.PARAGRAPH
            counter +=1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH