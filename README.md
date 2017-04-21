# Tools
Author: Arion_Miles

# Introduction
Random set of tools I use on a daily basis.

# Contents
reconnect.py - Made with selenium to automate connect/reconnect routine for my router (TL-WR740N) when there's a connection problem. Doesn't have a telnet interface so had to resort to Selenium. Uses [PhantomJS](http://phantomjs.org/) webdriver for silent/background operation. For windows only, though can be easily ported to other OS (just change the webdriver). 

# Usage
`> reconnect.py` : Checks the status, if disconnected, attempts to reconnect.


`> reconnect.py -r` : Attempts to force disconnect, reconnect, and check status.

Ctrl+C terminates the script.

# License
MIT License

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```