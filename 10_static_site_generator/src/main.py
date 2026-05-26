from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import extract_title, markdown_to_html_node
import os
import shutil

def main():
    src = "./static/"
    target = "./public/"
    if os.path.exists(target):
        shutil.rmtree(target)
    static_to_public(src, target)
    generate_page("content/index.md", "template.html", "public/index.html")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} from {template_path}")
    # Storing md and template file as str
    with open(from_path, "r") as md_file:
        md = md_file.read()
    with open(template_path, "r") as template_file:
        template = template_file.read()
    # Get html to inject in template
    html_node = markdown_to_html_node(md)
    html = html_node.to_html()
    title = extract_title(md)
    # Create HTML to inject from template
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", str(html))
    # Write the new HTML page at destination path
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(full_html)
    return





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
