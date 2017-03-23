    
def add (x, y): return x + y

def extract_filename(filename):
    arr = filename.split('.')
    arr.pop()
    str = ""
    for x in arr:
    	str = str + x + "."

    return str[:len(str)-1]

print (extract_filename("this.is.mega.unstoppable"))   
