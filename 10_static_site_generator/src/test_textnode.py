import unittest

from textnode import TextNode, TextType

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


if __name__ == "__main__":
    unittest.main()
