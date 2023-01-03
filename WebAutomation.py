from selenium import webdriver
from time import sleep


def update_html(example_text):
    html_beginning = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    ' \
                     '<title>Reddit</title>\n   <style>\n\n body { background-color: #19191a; }\n\n div {\n ' \
                     'width: 540;\nfont-family:Noto Sans,Arial,sans-serif;\nfont-size:12px;font-weight:700;\n' \
                     '   letter-spacing:unset;\n    line-height:16px;\n    text-transform:unset;\n    ' \
                     'min-height:24px;\n    padding:4px 16px;\n    text-align: left\n    }\n    h1, p { color: ' \
                     '#d7dadc; }\n    </style>\n</head>\n<body>\n<div>\n    <p>'
    html_end = "</p>\n</div>\n</body>\n</html>"
    example_text = texts[i]
    f = open('C:/Users/sammy/PycharmProjects/AutoVideoGenerator/RedditClone.html', 'w')
    f.write(html_beginning + example_text + html_end)
    f.close()


def screenshot_web_renders(screenshot_number):
    driver = webdriver.Firefox()
    driver.accept_untrusted_certs = True
    driver.get('file:///C:/Users/sammy/PycharmProjects/AutoVideoGenerator/RedditClone.html')
    sleep(1)
    driver.get_screenshot_as_file("screenshot" + screenshot_number + ".png")
    driver.quit()


texts = ['lorem ipsum', '1 lorem ipsum', '2 lorem ipsum']
for i in range(len(texts)):
    update_html(texts[i])
    screenshot_web_renders(str(i))

print("end...")
