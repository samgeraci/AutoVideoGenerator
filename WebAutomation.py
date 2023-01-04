from selenium import webdriver
from time import sleep


def update_html(example_text):
    html_beginning = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    ' \
                     '<title>Reddit</title>\n    <style>\n\n    body { background-color: #19191a; }\n\n    div.ex1 {' \
                     '\n    width:540px;\n    margin: auto;\n    }\n\n    h1, p {\n    color: #d7dadc;\n    ' \
                     'font-family:Noto Sans,Arial,sans-serif;\n    font-size:12px;\n    font-weight:700;\n    ' \
                     'letter-spacing:unset;\n    line-height:16px;\n    text-transform:unset;\n    ' \
                     'min-height:24px;\n    padding:4px 16px;\n    text-align: left;\n    }\n    ' \
                     '</style>\n</head>\n<body>\n<div class="ex1">\n    <p> '
    html_end = "</p>\n</div>\n</body>\n</html>"
    f = open('C:/Users/sammy/PycharmProjects/AutoVideoGenerator/RedditClone.html', 'w')
    f.write(html_beginning + example_text + html_end)
    f.close()


def screenshot_web_renders(filename):
    driver = webdriver.Firefox()
    driver.accept_untrusted_certs = True
    driver.get('file:///C:/Users/sammy/PycharmProjects/AutoVideoGenerator/RedditClone.html')
    sleep(1)
    driver.get_screenshot_as_file(filename + ".png")
    driver.quit()
