function _DoStabilo(text) {

  // Purple Highlight
  text = text.replace(/([\W_]|^)(---)(?=\S)([^\r]*?\S[\-]*)\2([\W_]|$)/g,
  '$1<span style="background-color:#FF00FF;">$3</span>$4');

  // Blue Highlight
  text = text.replace(/([\W_]|^)(--)(?=\S)([^\r]*?\S[\-]*)\2([\W_]|$)/g,
  '$1<span style="background-color:#00FFFF;">$3</span>$4');

  // Yellow Highlight
  text = text.replace(/([\W_]|^)(-)(?=\S)([^\r]*?\S[\-]*)\2([\W_]|$)/g,
  '$1<span style="background-color:#BFFA37;">$3</span>$4');

  return text;
}


// (tags that can be opened/closed) | (tags that stand alone)
var basic_tag_whitelist = /^(<\/?(b|blockquote|code|del|dd|dl|dt|em|h1|h2|h3|i|kbd|li|ol|p|pre|s|sup|sub|strong|strike|ul)>|<(br|hr)\s?\/?>)$/i;
// <a href="url..." optional title>|</a>
var a_white = /^(<a\shref="((https?|ftp):\/\/|\/)[-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]+"(\stitle="[^"<>]+")?\s?>|<\/a>)$/i;

// <img src="url..." optional width  optional height  optional alt  optional title
var img_white = /^(<img\ssrc="(https?:\/\/|\/)[-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]+"(\swidth="\d{1,3}")?(\sheight="\d{1,3}")?(\salt="[^"<>]*")?(\stitle="[^"<>]*")?\s?\/?>)$/i;

var stabilo_white = /span/i;

function sanitizeTag(tag) {
    if (tag.match(basic_tag_whitelist) || tag.match(a_white) || tag.match(img_white) || tag.match(stabilo_white))
        return tag;
    else
        return "";
}
