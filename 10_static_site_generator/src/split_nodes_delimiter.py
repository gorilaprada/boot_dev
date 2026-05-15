from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text.count(str(delimiter)) % 2 != 0:
            raise Exception("Invalid MD syntax: delimiter does not have a match")
        list_of_split_str = node.text.split(str(delimiter))
        for i in range(0, len(list_of_split_str)):
            if list_of_split_str[i] == "":
                continue
            elif i == 0 or i % 2 == 0:
                new_node = TextNode(list_of_split_str[i], TextType.TEXT)
            else:
                new_node = TextNode(list_of_split_str[i], text_type)
            new_nodes.append(new_node)
    return new_nodes
