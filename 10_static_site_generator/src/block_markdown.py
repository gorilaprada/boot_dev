
def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdown = markdown.split("\n\n")
    return [text.strip() for text in split_markdown if text != ""]

md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

"""

blocks = markdown_to_blocks(md)
print(blocks)

