# -*- coding: utf-8 -*-

from pyth.plugins.xhtml.reader import XHTMLReader
from pyth.plugins.xhtml.writer import XHTMLWriter
import xhtml

from cStringIO import StringIO

# A simple xhtml document with limited features.
content = StringIO(r"""
  <div>
    <p><strong>Simple document</strong></p>
    <p><i>this document has

    </i>no hypertext links yet.</p>
    <p><strong>bold text.</strong> <em>italic text.</em></p>
    <p class=important>bold text from css style
      <em> this is bold and italic</em>
    </p>
    <p class=bold> this is bold too</p>
    <p>unicode characters : 你好</p>
    a list
    <ul>
      <li>hello</li>
      <li>bonjour</li>
      <li>guten tag</li>
    </ul>
    <p>
      <a href=http://www.google.com>a link</a>
    </p>
  </div>
""")

if __name__ == '__main__':
    # Parse the document and then reconstruct it using the xhtml
    # writer.
    doc = XHTMLReader.read(content)
    print xhtml.docTemplate % XHTMLWriter.write(doc).getvalue()
