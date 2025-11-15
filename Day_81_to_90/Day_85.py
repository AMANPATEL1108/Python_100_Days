import argparse
import requests

def download_file(url, filename): 
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return filename

parser = argparse.ArgumentParser()

parser.add_argument("url", help="url of file to download")
# parser.add_argument("output", help="b which name do you want to save you file")

# FIXED: optional argument must start with --
parser.add_argument("--output", "-o", help="name of the file", default=None)

args = parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url, args.output)
