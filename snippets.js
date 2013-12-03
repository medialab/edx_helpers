// Beware, refaire le sprite avec fond blanc aussi.
// BEWARE !!!!!

// plus la string blue highlight

// lms/static/js/Markdown.Converter.js

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

// lms/static/js/Markdown.Sanitizer.js

// (tags that can be opened/closed) | (tags that stand alone)
var basic_tag_whitelist = /^(<\/?(b|blockquote|code|del|dd|dl|dt|em|h1|h2|h3|i|kbd|li|ol|p|pre|s|sup|sub|strong|strike|ul)>|<(br|hr)\s?\/?>)$/i;
// <a href="url..." optional title>|</a>
var a_white = /^(<a\shref="((https?|ftp):\/\/|\/)[-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]+"(\stitle="[^"<>]+")?\s?>|<\/a>)$/i;

// <img src="url..." optional width  optional height  optional alt  optional title
var img_white = /^(<img\ssrc="(https?:\/\/|\/)[-A-Za-z0-9+&@#\/%?=~_|!:,.;\(\)]+"(\swidth="\d{1,3}")?(\sheight="\d{1,3}")?(\salt="[^"<>]*")?(\stitle="[^"<>]*")?\s?\/?>)$/i;

// Refine the regex
var stabilo_white = /span/i;

function sanitizeTag(tag) {
    if (tag.match(basic_tag_whitelist) || tag.match(a_white) || tag.match(img_white) || tag.match(stabilo_white))
        return tag;
    else
        return "";
}

// lms/static/js/Markdown.Editor.js
// go to 1435
// mettre des commandes en plus au niveau du clavier?
    commandProto.doYellowHighlight = function (chunk, postProcessing) {
        return this.doYorB(chunk, postProcessing, 1, "yellow highlight");
    };

    commandProto.doBlueHighlight = function (chunk, postProcessing) {
        return this.doYorB(chunk, postProcessing, 2, "blue highlight");
    };

    // chunk: The selected region that will be enclosed with */**
    // nStars: 1 for italics, 2 for bold
    // insertText: If you just click the button without highlighting text, this gets inserted
    commandProto.doYorB = function (chunk, postProcessing, nStars, insertText) {

        // Get rid of whitespace and fixup newlines.
        chunk.trimWhitespace();
        chunk.selection = chunk.selection.replace(/\n{2,}/g, "\n");

        // Look for stars before and after.  Is the chunk already marked up?
        // note that these regex matches cannot fail
        var starsBefore = /(-*$)/.exec(chunk.before)[0];
        var starsAfter = /(^-*)/.exec(chunk.after)[0];

        var prevStars = Math.min(starsBefore.length, starsAfter.length);

        // Remove stars if we have to since the button acts as a toggle.
        if ((prevStars >= nStars) && (prevStars != 2 || nStars != 1)) {
            chunk.before = chunk.before.replace(re("[-]{" + nStars + "}$", ""), "");
            chunk.after = chunk.after.replace(re("^[-]{" + nStars + "}", ""), "");
        }
        else if (!chunk.selection && starsAfter) {
            // It's not really clear why this code is necessary.  It just moves
            // some arbitrary stuff around.
            chunk.after = chunk.after.replace(/^(-*)/, "");
            chunk.before = chunk.before.replace(/(\s?)$/, "");
            var whitespace = re.$1;
            chunk.before = chunk.before + starsAfter + whitespace;
        }
        else {

            // In most cases, if you don't have any selected text and click the button
            // you'll get a selected, marked up region with the default text inserted.
            if (!chunk.selection && !starsAfter) {
                chunk.selection = insertText;
            }

            // Add the true markup.
            var markup = nStars <= 1 ? "-" : "--"; // shouldn't the test be = ?
            chunk.before = chunk.before + markup;
            chunk.after = markup + chunk.after;
        }

        return;
    };



    buttons.bold = makeButton("wmd-bold-button", "Bold (Ctrl+B)", "0px", bindCommand("doBold"));
    buttons.italic = makeButton("wmd-italic-button", "Italic (Ctrl+I)", "-20px", bindCommand("doItalic"));
    buttons.yellowHighlight = makeButton("wmd-yellowhighlight-button", "Yellow Highlight", "-40px",  bindCommand("doYellowHighlight"));
    buttons.blueHighlight = makeButton("wmd-bluehighlight-button", "Blue Highlight", "-60px", bindCommand("doBlueHighlight"));
    makeSpacer(1);
    buttons.link = makeButton("wmd-link-button", "Hyperlink (Ctrl+L)", "-80px", bindCommand(function (chunk, postProcessing) {
        return this.doLinkOrImage(chunk, postProcessing, false);
    }));
    buttons.quote = makeButton("wmd-quote-button", "Blockquote (Ctrl+Q)", "-100px", bindCommand("doBlockquote"));
    buttons.code = makeButton("wmd-code-button", "Code Sample (Ctrl+K)", "-120px", bindCommand("doCode"));
    buttons.image = makeButton("wmd-image-button", "Image (Ctrl+G)", "-140px", bindCommand(function (chunk, postProcessing) {
        return this.doLinkOrImage(chunk, postProcessing, true, imageUploadHandler);
    }));
    makeSpacer(2);
    buttons.olist = makeButton("wmd-olist-button", "Numbered List (Ctrl+O)", "-160px", bindCommand(function (chunk, postProcessing) {
        this.doList(chunk, postProcessing, true);
    }));
    buttons.ulist = makeButton("wmd-ulist-button", "Bulleted List (Ctrl+U)", "-180px", bindCommand(function (chunk, postProcessing) {
        this.doList(chunk, postProcessing, false);
    }));
    buttons.heading = makeButton("wmd-heading-button", "Heading (Ctrl+H)", "-200px", bindCommand("doHeading"));
    buttons.hr = makeButton("wmd-hr-button", "Horizontal Rule (Ctrl+R)", "-220px", bindCommand("doHorizontalRule"));
    makeSpacer(3);
    buttons.undo = makeButton("wmd-undo-button", "Undo (Ctrl+Z)", "-240px", null);
    buttons.undo.execute = function (manager) { if (manager) manager.undo(); };

    var redoTitle = /win/.test(nav.platform.toLowerCase()) ?
        "Redo (Ctrl+Y)" :
        "Redo (Ctrl+Shift+Z)"; // mac and other non-Windows platforms

    buttons.redo = makeButton("wmd-redo-button", redoTitle, "-260px", null);
    buttons.redo.execute = function (manager) { if (manager) manager.redo(); };

    if (helpOptions) {
        var helpButton = document.createElement("span");
        var helpButtonImage = document.createElement("span");
        helpButton.appendChild(helpButtonImage);
        helpButton.className = "wmd-button wmd-help-button";
        helpButton.id = "wmd-help-button" + postfix;
        helpButton.XShift = "-280px";
        helpButton.isHelp = true;
        helpButton.style.right = "0px";
        helpButton.title = helpOptions.title || defaultHelpHoverTitle;
        helpButton.onclick = helpOptions.handler;

        setupButton(helpButton, true);
        buttonRow.appendChild(helpButton);
        buttons.help = helpButton;
    }

    setUndoRedoButtonStates();


// Act of wmd spacers
// 1
// 2
// 3