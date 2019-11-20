# Beajar keyword argumen list


def create_html(tag, text, href=""):
    html=f"<{tag} href='{href}'>{text}</{tag}>"
    return html

html = create_html("p","Hello Python")
print(html)
html = create_html("a","Hello Python", "www.w3schools/python")

print(html)