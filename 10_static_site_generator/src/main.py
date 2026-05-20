from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    testNode = TextNode("some text", TextType.TEXT,"www.gorilaprada.com")
    print(testNode)


main()
