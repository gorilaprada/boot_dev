from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil

def main():
    src = "./static/"
    target = "./public/"
    if os.path.exists(target):
        shutil.rmtree(target)
    static_to_public(src, target)


def static_to_public(src: str, target: str) -> None:
    if not os.path.exists(target):
        os.mkdir(target)
    list_of_dir = os.listdir(src)
    for dir in list_of_dir:
        new_src = os.path.join(src, dir)
        new_target = os.path.join(target, dir)
        if os.path.isfile(new_src):
            shutil.copy(new_src, new_target)
            print(f"{new_src} copied to {new_target}")
        else:
            static_to_public(new_src, new_target)
    return




main()
