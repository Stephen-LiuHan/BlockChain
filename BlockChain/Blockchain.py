#coding UTF-8#

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask

class Blockchain(object):
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
            'index' : len(self.chain) - 1,
            'time_stamp' : time(),
            'transaction' : self.currentTrunsactions,
            'proof' : proof,
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

    def proof_of_work(self,last_proof):
        """
        シンプルなプルーフ・オブ・ワークの説明-
        - hash(p'p)の最初の４つが0となるようなpを探す
        - p'は前のブロックのプルーフ値　pは新しいブロックのプルーフ
        :param last_proof: <int> 前のブロックのプルーフ
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof+=1
            
        return proof

    @staticmethod
    def valid_proof(last_proof,proof):
        """
        プルーフが正しいか確認する:hash(last_proof,proof)の上位4つが０になっているか
        :param last_proof: <int> 前のプルーフ
        :param proof: <int> 現在のプルーフ
        :return: <bool> 正しければTrue、そうでなければFalse
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

#ノードを作る
app = Flask(__name__)

#このノードのグローバルにユニークなアドレスを作る
node_indetifire = str(uuid4()).replace('-','')

#ブロックチェーンクラスをインスタンス化　
blockchain = Blockchain()

@app.route ('/transactions/new',methods=['POST'])
def new_transactions():
    return '新しいトランザクションを追加する'

@app.route('/mine',methods=['GET'])
def mine():
    return '新しいブロックを採掘します'

@app.route('/chain',methods=['GET'])
def full_chain():
    response = {
        'chain' : blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

# port5000でサーバを起動
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)