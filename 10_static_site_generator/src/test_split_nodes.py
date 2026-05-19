import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType, text_node_to_html_node

class testSplitNodesFunc(unittest.TestCase):
    # Test function split_nodes_delimiter
    def test_text(self):
        node = TextNode("This is a text node with some `def foo(): return` and more `def foo2(): return`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = TextNode("def foo(): return", TextType.CODE)
        node3 = TextNode("def foo2(): return", TextType.CODE)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[3], node3)

    def test_full_output(self):
        node = TextNode("This is a text node with some _italic1_ and more _italic2_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        node0 = TextNode("This is a text node with some ", TextType.TEXT)
        node1 = TextNode("italic1", TextType.ITALIC)
        node2 = TextNode(" and more ", TextType.TEXT)
        node3 = TextNode("italic2", TextType.ITALIC)
        self.assertEqual(new_nodes, [node0, node1, node2, node3])

    def test_full_output2(self):
        node = TextNode("This is a text node with some **bold1** and **bold2** more ", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        node0 = TextNode("This is a text node with some ", TextType.TEXT)
        node1 = TextNode("bold1", TextType.BOLD)
        node2 = TextNode(" and ", TextType.TEXT)
        node3 = TextNode("bold2", TextType.BOLD)
        node4 = TextNode(" more ", TextType.TEXT)
        self.assertEqual(new_nodes, [node0, node1, node2, node3, node4])

    def test_two_nodes(self):
        big_node = TextNode("This is a text node", TextType.TEXT)
        big_node2 = TextNode("This is a text node with some code: `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([big_node, big_node2], "`", TextType.CODE)
        node0 = TextNode("This is a text node", TextType.TEXT)
        node1 = TextNode("This is a text node with some code: ", TextType.TEXT)
        node2 = TextNode("code", TextType.CODE)
        self.assertEqual(new_nodes, [node0, node1, node2])

    def test_node_with_type_CODE(self):
        big_node = TextNode("`def foo(): return`", TextType.CODE)
        new_nodes = split_nodes_delimiter([big_node], "`", TextType.CODE)
        node0 = TextNode("`def foo(): return`", TextType.CODE)
        self.assertEqual(new_nodes[0], node0)

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
    # Test split_nodes_image and split_nodes_link
    def test_split_images(self):
        node = TextNode(
            "This is a text with an ![image](www.image.com) and another ![image2](www.image2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "www.image.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "www.image2.com"),

            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
