# Imports
# ---------------------------------------------------------------------------
import subprocess
from sys import argv
from os import path
from lxml import etree

# Constants
# ---------------------------------------------------------------------------
HTML_HEADER: str = "<!DOCTYPE html>\n"

# Main function
# ---------------------------------------------------------------------------
def main() -> None:
    """ Convert Markdown to HTML with your own stylesheet """
    markdown_file: str = get_markdown()
    html: str = get_html(markdown_file)
    html = replace_stylesheet(html)
    export_html(html)

# Helper functions
# ---------------------------------------------------------------------------
def get_markdown() -> str:
    """
        Parse the terminal arguments to get either a proper .md file or 
        an understandable input error
    """
    if len(argv) >= 2:
        if argv[1].endswith(".md"):
            return argv[1]
    error_message("Please specify a markdown file")

def error_message(message: str) -> None:
    print(message)
    exit()

def get_html(arg: str) -> str: 
    """Proccesses an HTML from the .md file and returns it as a string"""
    print("Processing...")
    html: str = subprocess.run(
        ["pandoc", arg, "-s"], 
        capture_output=True, 
        encoding="utf-8"
    ).stdout
    if not(html.startswith(HTML_HEADER)):
        error_message("File does not exist!")
    return html

def replace_stylesheet(html: str) -> str:
    """
        Replaces the default stylesheet with a specialized stylesheet 
        in the HTMLs/styles folder
    """
    root: etree._Element = etree.HTML(html)
    root[0][-1] = etree.Element(
        "link", 
        rel="stylesheet", 
        href="./styles/style.css"
    )
    return HTML_HEADER + etree.tostring(root, 
                         pretty_print=True).decode("utf-8")

def export_html(html: str):
    script_path = "".join(path.split(argv[0])[:-1])
    write_path = path.join(script_path, "HTMLs")
    file_path = path.join(write_path, get_filename())
    print("Writing HTML file...")
    with open(file_path, 'w') as file:
        file.write(html)
    print("HTML file successfully written!")


def get_filename() -> str:
    OUTPUT_ARG = "-o"
    if OUTPUT_ARG in argv:
        try:
            index = argv.index(OUTPUT_ARG)+1
            file_name = argv[index]
        except IndexError:
            pass
    else:
        file_name = input("Input file name: ")
    if not(file_name.endswith(".html")):
        file_name += ".html"
    return file_name

# Import convention
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()