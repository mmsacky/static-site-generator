import sys
from source_to_destination import source_to_destination, generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
            
    source_to_destination("static/", "docs/")
    generate_pages_recursive("content/","template.html","docs/", basepath)

if __name__ == "__main__":
    main()