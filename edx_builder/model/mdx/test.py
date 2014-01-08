import markdown
import pprint
import re
# from ext_scribd import ScribdExtension
from ext_image import ImageExtension
# from ext_link import LinkExtension

# ext = ScribdExtension()
ext2 = ImageExtension()
# ext3 = LinkExtension()

# print markdown.markdown(u'[[pdf:http://www.scribd.com/doc/185064084/melissa-pdf]]', [ext])
# print markdown.markdown(u'![description](http://test.com)', [ext2])
# print markdown.markdown(u'![description:left](http://test.com)\ntestde text', [ext3, ext2])
# print markdown.markdown(u'![description:right](http://test.com)', [ext2])
# print markdown.markdown(u'[link text](http://test.com)', [ext3])
print markdown.markdown(u'![description](http://test.com)', [ext2])
print markdown.markdown(u'![description:right](http://test.com)', [ext2])
print markdown.markdown(u'![description:left](http://test.com)', [ext2])
print markdown.markdown(u'![description:height(300)](http://test.com)', [ext2])
print markdown.markdown(u'![description:height](http://test.com)', [ext2])
print markdown.markdown(u'![description:height:left](http://test.com)', [ext2])


''' <iframe class="scribd_iframe_embed" src="//www.scribd.com/embeds/185064084/content?start_page=1&view_mode=scroll&access_key=key-2oshwm8ft80hr8f9r6gq&show_recommendations=false" data-auto-height="false" data-aspect-ratio="0.256541524459613" scrolling="no" id="doc_96072" width="409" height="546" frameborder="0"></iframe> '''
''' <iframe class="scribd_iframe_embed" src="//www.scribd.com/embeds/184845262/content?start_page=1&view_mode=scroll&access_key=key-1x3ijo3i55yniljagm8c&show_recommendations=false" data-auto-height="false" data-aspect-ratio="0.772922022279349" scrolling="no" id="doc_32978" width="100%" height="600" frameborder="0"></iframe> '''

# import scribd

# scribd.api_key = '35in3j745bkni3hy8yz05'
# scribd.api_secret = 'sec-4mu14kmgrpbff4j4tipeerjsin'
# scribd.config('35in3j745bkni3hy8yz05', 'sec-4mu14kmgrpbff4j4tipeerjsin')

# print scribd.api_user.get('184457227').get_attributes()

# for document in scribd.api_user.all():
#     print document.title