from button_callback import Btn

class Bt(object):
    btn=Btn()
    def __init__(self,*args,**kwargs):
        super(Bt,self).__init__(*args,**kwargs)
        self.btn.got_value=self.halo
    def halo(self,data):
        print(data)


Bt()