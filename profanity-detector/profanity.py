import urllib.request

def read_text(file_name):
  ''' Read text from a given file and find curse word '''
  
  # Read the contents of the file
  file = open(file_name)
  content = file.read()
  file.close()
  
  # Remove spaces, new-line etc before using it as a query parameter  in the url
  # Reference https://en.wikipedia.org/wiki/Query_string & https://www.w3schools.com/tags/ref_urlencode.ASP
  content = content.replace("\n", " ")
  text = content.replace(' ','%')

  # Invoke profanity check function
  check_profanity(text)


def check_profanity(text_to_check):
    ''' Checks wether the input text contains curse word '''
    
    # Connect to the endpoint which provides an api to do profanity check and provide the text as query parameter
    connection = urllib.request.urlopen( "http://www.wdylike.appspot.com/?q=" + text_to_check)
    response = connection.read()
    connection.close()
    
    # Convert the response from bytes to string 
    output = response.decode()

    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("Good to go")
    else:
        print("Unusual")


if __name__ == "__main__":
    read_text("quotes.txt")