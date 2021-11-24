#英文转中文
class EN_CN_Word :
    def __init__(self,word='',phonetic='',definition='',translation='',pos='',collins='',oxford='',tag='',bnc='',frq='',exchange='',detail='',audio=''):
        self.word=word
        self.phonetic=phonetic
        self.definition=definition
        self.translation=translation

        self.pos=pos
        self.collins=collins
        self.oxford=oxford
        self.tag=tag
        self.bnc=bnc
        self.frq=frq
        self.exchange=exchange
        self.detail=detail
    def __str__(self):
        a=self.word,self.definition,self.translation,'/'+self.phonetic+'/'
        return str(a)
#中文转英文
class CN_EN_Word:
    def __init__(self,word='',pronouciation='',translation=''):
        self.word=word
        self.pronouciation=pronouciation
        self.translation=translation
    def __str__(self):
        a=self.word,'/['+self.pronouciation+'/',self.translation
        return str(a)
    
    
