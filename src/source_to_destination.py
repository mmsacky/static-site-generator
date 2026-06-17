import os, shutil
from markdown_to_blocks import markdown_to_blocks
from markdown_to_html import markdown_to_html_node

def source_to_destination(source, destination):
    abs_source = os.path.abspath(source)
    abs_destination = os.path.abspath(destination)

    if os.path.exists(abs_destination):

        shutil.rmtree(abs_destination)

    os.mkdir(abs_destination)    

    
    source_content = os.listdir(abs_source)

    for item in source_content:
        src_path = os.path.join(abs_source, item)
        dst_path = os.path.join(abs_destination, item)
            
        if os.path.isfile(src_path):
            shutil.copy(src_path,dst_path)
        else:
            source_to_destination(src_path,dst_path)
            
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
           return block.removeprefix("# ")
    raise Exception("The markdown contains no H1 header")
        

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} ...")
    
    with open(from_path, "r") as content_file:
        content = content_file.read()
        
    with open(template_path, "r") as template_file:
        template = template_file.read()
        
    content_as_html = markdown_to_html_node(content).to_html()

    page_title = extract_title(content)
    print(basepath)
    template = (
        template
        .replace("{{ Title }}",page_title)
        .replace("{{ Content }}",content_as_html)
        .replace('href="/',f'href="{basepath}')
        .replace('src="/',f'src="{basepath}')
    )

    dest_dir = os.path.dirname(dest_path)

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as web_page:
        web_page.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    content_dir = os.listdir(dir_path_content)
    
    for item in content_dir:

        item_path = os.path.join(dir_path_content, item)
        
        
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item_path)
            if extension.lower() == ".md":
                html_file = item.removesuffix(".md") + ".html"
                dest_path = os.path.join(dest_dir_path, html_file)
                generate_page(item_path, template_path, dest_path, basepath)
        else:
            new_dest_dir_path = os.path.join(dest_dir_path,item)
            generate_pages_recursive(item_path, template_path, new_dest_dir_path, basepath)