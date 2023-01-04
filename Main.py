import ImageProcessing as ip
import WebAutomation as wa

texts = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ut imperdiet enim. Proin ultricies magna '
         'eget pharetra sodales. Sed interdum neque et turpis auctor molestie. Quisque pulvinar porttitor efficitur. '
         'Donec congue massa neque, sit amet congue orci fringilla ut. In viverra odio posuere, tincidunt sem in, '
         'pellentesque nibh. Donec at dictum elit, at faucibus arcu. Donec tincidunt dapibus dolor, ac laoreet massa '
         'porttitor in. Fusce ac ullamcorper dolor, ac imperdiet augue. Aliquam lobortis metus tristique turpis '
         'auctor, non fringilla urna euismod. Morbi mattis massa ac erat faucibus, id imperdiet nulla posuere. Nam '
         'ullamcorper, sapien sed porta sodales, velit eros feugiat urna, a sollicitudin risus tortor vitae '
         'metus.</p>\n    <p>Maecenas sed feugiat turpis, nec tempor tellus. Sed scelerisque arcu vel dui dapibus '
         'consectetur. Proin vehicula consectetur nibh, nec molestie risus mattis ut. Vestibulum eget nulla lacinia, '
         'tincidunt mauris at, pharetra metus. Vivamus lacinia nulla viverra diam laoreet efficitur. Sed fringilla '
         'purus in leo viverra, non iaculis erat gravida. Vestibulum ante ipsum primis in faucibus orci luctus et '
         'ultrices posuere cubilia curae; Quisque varius venenatis justo vitae interdum. Donec pellentesque aliquam '
         'rhoncus. Sed accumsan volutpat ligula, vel aliquet risus iaculis quis. Interdum et malesuada fames ac ante '
         'ipsum primis in faucibus. Quisque sed laoreet diam. Aenean a lorem sed felis rutrum vulputate et hendrerit '
         'nisl. Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Lorem ipsum dolor sit amet, consectetur '
                                                                           'adipiscing elit. Fusce ut imperdiet enim. '
                                                                           'Proin ultricies magna '
         'eget pharetra sodales. Sed interdum neque et turpis auctor molestie. Quisque pulvinar porttitor efficitur. '
         'Donec congue massa neque, sit amet congue orci fringilla ut. In viverra odio posuere, tincidunt sem in, '
         'pellentesque nibh. Donec at dictum elit, at faucibus arcu. Donec tincidunt dapibus dolor, ac laoreet massa '
         'porttitor in. Fusce ac ullamcorper dolor, ac imperdiet augue. Aliquam lobortis metus tristique turpis '
         'auctor, non fringilla urna euismod. Morbi mattis massa ac erat faucibus, id imperdiet nulla posuere. Nam '
         'ullamcorper, sapien sed porta sodales, velit eros feugiat urna, a sollicitudin risus tortor vitae '
         'metus.</p>', '2 lorem ipsum']
for i in range(len(texts)):
    wa.update_html(texts[i])
    wa.screenshot_web_renders("screenshot" + str(i))
    ip.crop_image("screenshot" + str(i) + ".png")

print("end...")
