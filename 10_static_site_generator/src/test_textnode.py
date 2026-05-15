import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter

class testTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_link_none(self):
        node = TextNode("Node", TextType.LINK, None)
        node2 = TextNode("Node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_texttype_dif(self):
        node = TextNode("Node", "ougabouga", None)
        node2 = TextNode("Node", "ougabouga", None)
        self.assertEqual(node, node2)

    # Test function text_node_to_html_node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, { "src": "www.image.com", "alt": "This is an image"})

    def test_link(self):
        node = TextNode("Click Here", TextType.LINK, "www.link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, { "href": "www.link.com" })

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

if __name__ == "__main__":
    unittest.main()
