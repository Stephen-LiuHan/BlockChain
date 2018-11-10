#coding UTF-8#

class blockchain(object):
    def __init__(self):
        self.chain = []
        self.currentTrunsactions = []

    def new_block(self):
        #新しいブロックチェーンを作り、チェーンに加える
        pass

    def new_transaction(self,sender,recipient,amount):
        """
        新しいトランザクションをリストに加える
        
        次に発掘されるブロックに加える新しいトランザクションを作る
        :param sender: <str> 送信者のアドレス
        :param recilient: <str> 受信者のアドレス
        :param amount: <int> 量
        :return: <int> このトランザクションを含めたブロックのアドレス
        """

        self.currentTrunsactions.append({
            "sender":sender,
            "recipient":recipient,
            "amount":amount,
        })
        return self.last_block["index"]+1

    @staticmethod
    def hash(block):
        #ブロックをハッシュ化する
        pass

    @property
    def last_block(self):
        #チェーンの最後のブロックを返す
        pass