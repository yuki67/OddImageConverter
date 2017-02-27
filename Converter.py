import math


class Converter(object):
    """ 色配列を描画するための基底クラス """

    def convert(self, color_array, size, filename):
        """ color_arrayを使って辺の長さが最高でもsizeの絵を描く """
        # 長い方の辺の長さからdx, dyを求める
        d = max(1, max(len(color_array), len(color_array[0])) / size)
        x = y = 0
        self.open(color_array, size, filename)
        while y < len(color_array[0]):
            x = 0
            while x < len(color_array):
                self.put_pixel(color_array[int(x)][int(y)])
                x += d
            self.new_line()
            y += d
        self.close()

    def open(self, color_array, size, filename):
        """
        ファイルを(おそらくはself.fileに)開いて、初期設定を行う
        初期設定に使う情報を得るためにcolor_arrayも渡される
        """
        assert False, "Override me!"

    def put_pixel(self, color):
        """
        座標(x, y)をcolorで塗る
        描かれる順番は
        (0,0)->(0,1)->...->(0,n)->
        (1,0)->(1,1)->...->(1,n)->
        .................->(m,n)
        で決まっている(シェルに出力するときにこの順番の方が良いため)
        書かれる順番が決まっているので座標は渡されない
        """
        assert False, "Override me!"

    def new_line(self):
        """
        ファイルに改行を加える
        文字が記録される場合を想定した関数なので、何もしなくて済むこともあると思う
        """
        assert False, "Override me!"

    def close(self):
        """
        ファイルを閉じ、セーブする
        """
        assert False, "Override me!"
