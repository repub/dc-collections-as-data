# get_transcripts.py fetches all of the transcripts it can find for a
# collection, or downloads the transcript for a specific item upon request
#
# bash-3.2$ python get_transcripts.py -h
# usage: get_transcripts.py [-h] [-i ITEM] alias
#
# positional arguments:
#   alias                 The alias of the CONTENTdm collection whose
#                         transcripts we would like
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -i ITEM, --item ITEM  A specific item within the collection whose transcript
#                         we would like

import argparse
import json
import os
import pycdm
import sys

data = {'items': []}
url = "https://digital.libraries.psu.edu/digital/collection"

def get_transcript(alias, id):
    print("get {} {}".format(alias, id))
    try:
        item = pycdm.item(alias, id)
    except Exception as e:
        print("couldn't download {}/{}: {}".format(alias, id, e))

    i = {
        'title': item.info['title'],
        'href': "{}/{}/id/{}".format(url, alias, str(id)),
        'iiif': "https://cdm17287.contentdm.oclc.org/iiif/info/{}/{}/manifest.json".format(alias, str(id)),
        'pages': []
    }
    for idx, page in enumerate(item.pages):
        ptr = str(page.id)
        p = {
            'page_number': idx+1,
            'label': page.label,
            'href': "https://digital.libraries.psu.edu/digital/iiif/{}/{}/info.json".format(alias, ptr)
        }
        if isinstance(page, pycdm.Page):
            print(page.label)
            page.pageinfo()
        p['title'] = page.info['title'] if 'title' in page.info else "{}_{}".format(alias, ptr)
        p['transcript'] = page.info['transc'] if 'transc' in page.info else ""
        i['pages'].append(p)

    return i


def write_file(file, data):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'w') as f:
        f.write(json.dumps(data))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('alias', help="The alias of the CONTENTdm collection whose transcripts we would like")
    parser.add_argument('-i', '--item', help="A specific item within the collection whose transcript we would like")
    args = parser.parse_args()

    collection = pycdm.Collection(args.alias)
    data['title'] = collection.name
    data['alias'] = args.alias
    if args.item:
        data['items'].append(get_transcript(args.alias, args.item))
        write_file("{}_{}.json".format(args.alias, args.item), data)
    else:
        collection.getItems()
        for i in collection.items:
            data['items'].append(get_transcript(args.alias, i))
        write_file("{}.json".format(args.alias), data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(e.message)
