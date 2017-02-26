import argparse
from PIL import Image
import OddImageConverter


def prompt():
    """ メイン処理 """
    # 引数を処理
    parser = argparse.ArgumentParser(description="Convert image into odd formats.")
    parser.add_argument("-l", action="store_true", help="list option show the formats into which this program can convert.")
    parser.add_argument(dest="filename", action="store", help="Name of the image.", default=None)
    args = parser.parse_args()

    # list引数を処理
    if args.l:
        for form, size, _ in OddImageConverter.converters:
            print(form, size)

    # 変換を実行
    img = Image.open(args.filename)
    OddImageConverter.convert(img)

if __name__ == "__main__":
    prompt()
