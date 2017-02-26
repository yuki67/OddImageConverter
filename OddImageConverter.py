converters = [
    ["excel", [1024, 1024], None],
    ["shell script", [50, 50], None],
    ["html", [300, 300], None]
]


def convert(img):
    """ imgを変換する """
    # 画像が大きすぎるときは縮小する
    # 長い方の辺が1024pxになるようにする
    if max(img.size) > 1024:
        factor = 1024 / max(img.size)
        img = img.resize((int(i * factor) for i in img.size))
    # 色配列を作成
    img_array = list(img.getdata())

    for _, _, converter in converters:
        converter(img_array)
