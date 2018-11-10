#coding UTF-8#

import hashlib
import json
from time import time

class blockchain(object):
    def __init__(self):
        self.chain = []
        self.currentTrunsactions = []

        #ジェネシスブロックを作る
        self.new_block(proof=100,previous_hash=1)

    def new_block(self,proof,previous_hash=None):
        """
        新しいブロックチェーンを作り、チェーンに加える
        
        :param proof: <int> プルーフ・オブ・ワークから得られるプルーフ
        :param previous_hash: (オプション)<str> 前のブロックからのハッシュ
        :return: <dict> 新しいブロック
        """
        
        block = {
            'index' = len(self.chain) - 1,
            'time_stamp' = time(),
            'transaction' = self.currentTrunsactions,
            'proof' = proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }

        #現在のトランザクションリストをリセット
        self.currentTrunsactions=[]

        self.chain.append(block)
        return block

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
        """
        ブロックをハッシュ化する
        
        ブロックのSHA-256ハッシュを作る
        :param block: <dick> ブロック
        :return: <str> ハッシュ値
        """
        #ディクショナリがソートされてるものとし、ハッシュの一貫性を保つ
        block_string = json.dumps(block,sort_keys=True).encode
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #チェーンの最後のブロックを返す
        return self.chain[-1]