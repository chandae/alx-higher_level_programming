
""" script fetches https://intranet.htbn.io/status """
import urllib.request


if __name__ == '__main__':
    url = 'https://d6b4436ad043.413a0140.alx-cod.online:5000'
    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf8')))
