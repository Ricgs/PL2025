import sys
import re

def conversor(header, bold, italic, link, image, list):
    # Headers
    header = re.sub(r'^(#{1,6})\s*(.+)$', lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>', header, flags=re.MULTILINE)
    
    # Bold
    bold = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', bold)
    
    # Italic
    italic = re.sub(r'\*(.*?)\*', r'<i>\1</i>', italic)
    
    # Links
    link = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', link)
    
    # Images
    image = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', image)
    
    # Numbered Lists
    list = re.sub(r'(?m)^(\d+)\.\s+(.*)', r'<li>\2</li>', list)
    if '<li>' in list:
        list = '<ol>' + list + '</ol>'
    
    return header + bold + italic + link + image + list
   

if __name__ == "__main__":
    header = """
# Header 1
# Header 2
# Header 3
"""

    bold = """
This is a **bold** text.
"""

    italic = """
This is a *italic* text.
"""

    link = """
Here is a [link](http://example.com).
"""

    image = """
Here is an image: ![alt text](http://example.com/image.jpg)
"""

    list = """
1. First item
2. Second item
3. Third item
"""

    print(conversor(header, bold, italic, link, image, list))