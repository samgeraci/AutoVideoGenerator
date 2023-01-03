import ImageProcessing as ip
import WebAutomation as wa

texts = ['lorem ipsum', '1 lorem ipsum', '2 lorem ipsum']
for text in texts:
    wa.update_html(text)
    wa.screenshot_web_renders(text)
    ip.crop_image(text + ".png")

print("end...")
