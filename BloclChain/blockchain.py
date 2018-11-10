#coding UTF-8#

class blockchain(object):
    def __init__(self):
        self.chain = []
        self.currentTrunsactions = []

    def new_block(self):
        #新しいブロックチェーンを作り、チェーンに加える
        pass

    def new_transaction(self):
        #新しいトランザクションをリストに加える
        pass

    @staticmethod
    def hash(block):
        #ブロックをハッシュ化する
        pass

    @property
    def last_block(self):
        #チェーンの最後のブロックを返す
        pass