import os,requests
### Download.py

# Note: This function was found and reused to help with the Error 406 I was getting from the Natural Earth download
# It requires the request to send a header first so the server can interpret the request
def download_file(url,local_filename):
    #local_filename = url.split('/')[-1]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # NOTE the stream=True parameter below
    with requests.get(url, headers=headers,stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename
  
#print (GetdayRange(0,minusdays=0))

