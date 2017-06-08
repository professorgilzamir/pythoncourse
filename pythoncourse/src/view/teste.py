import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.grid(sticky=tk.NSEW)
 
 
frame.set_content("""
<html>
<body>
<h1>Hello world!</h1>
<p>First para</p>
<ul>
    <li>first list item</li>
    <li>second list item</li>
</ul>
<img src="http://findicons.com/files/icons/638/magic_people/128/magic_ball.png"/>
</body>
</html>    
""")
 
frame.set_content(urllib.request.urlopen("http://thonny.cs.ut.ee").read().decode())
#print(frame.html.cget("zoom"))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()