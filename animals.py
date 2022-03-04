class Dog :

    def __init__(self , height , weight , color, voiceText):
        self.voiceText= voiceText
        self.height= height
        self.weight= weight
        self.color= color

    def voice(self):
        print(f'{self.voiceText}')


d = Dog(60,15,'White','gafgaf')
d.voice()

class Cat :

    def __init__(self , height , weight , color, voiceText):
        self.voiceText= voiceText
        self.height= height
        self.weight= weight
        self.color= color

    def voice(self):
        print(f'{self.voiceText}')

d = Cat(30,5,'Black','Mya-Mya')
d.voice()

class Cow :

    def __init__(self , height , weight , color, voiceText):
        self.voiceText= voiceText
        self.height= height
        self.weight= weight
        self.color= color

    def voice(self):
        print(f'{self.voiceText}')
d = Cow(140,60,'White and Black','Suuuuuuu')
d.voice()


class Bear :

    def __init__(self , height , weight , color, voiceText):
        self.voiceText= voiceText
        self.height= height
        self.weight= weight
        self.color= color

    def voice(self):
        print(f'{self.voiceText}')

d = Bear(180,120,'Brown','Ffffff')
d.voice()
