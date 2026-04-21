from textnode import TextNode, TextType

print("hello world")

def main():
    a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev" )
    print(a)

if __name__ == "__main__":
    main()