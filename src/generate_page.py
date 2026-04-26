import os
from block_markdown import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    lines = markdown.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path, 'r')
    read_markdown = markdown_file.read()
    markdown_file.close()

    templete_file =open(template_path, 'r')
    read_templete = templete_file.read()
    templete_file.close()

    content = markdown_to_html_node(read_markdown).to_html()
    title = extract_title(read_markdown)
   
    read_templete = read_templete.replace("{{ Title }}", title)
    read_templete = read_templete.replace("{{ Content }}", content)
    read_templete = read_templete.replace('href="/', f'href="{base_path}')
    read_templete = read_templete.replace('src="/', f'src="{base_path}')
    
    dir_path = os.path.dirname(dest_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
        
    html_file = open(dest_path, "w")
    html_file.write(read_templete)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    items_content = os.listdir(dir_path_content)

    for item in items_content:
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            html_file = Path(dest_path).with_suffix(".html")
            generate_page(item_path, template_path, html_file, base_path)
        else:
            generate_pages_recursive(item_path, template_path, dest_path, base_path)


        
    