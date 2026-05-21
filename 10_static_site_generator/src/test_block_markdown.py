import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class testBlockMarksdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_skip_empty_blocks(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    # Test block_to_block_type
    def test_heading(self):
        block = "# Heading"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_code(self):
        block = "```\nSome code```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_quote(self):
        block = ">This\n>is\n>a quote"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Lesson\n- learned\n- from boot dev"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Lesson\n2. learned\n3. from boot dev"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)



if __name__ == "__main__":
    unittest.main()
