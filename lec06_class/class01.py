"""
클래스(class):
프로그램에서 만들려고 하는 대상(객체)이 가져야 할
속성(데이터)과 기능(함수)을 묶은 "데이터 타입"

메소드(method): 클래스가 가지고 있는 함수
"""

# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원
# TV 기능: 채널 변경, 음량 변경, 전원 on/off

# 클래스 설계(정의)
class BasicTV:
    """
    BasicTV 클래스
    """
    max_channel, min_channel = 5, 0
    max_volume, min_volume = 5, 0

    def __init__(self, power, channel, volume):
        print('BasicTV 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume

    def powerOnOff(self):
        if self.power:
            self.power = False
            print('TV OFF')
        else:
            self.power = True
            print('TV ON')

    def channelup(self):
        if self.power == True:
            if self.channel < self.max_channel:     # 현재 채널 값이 채널의 최대값보다 작으면
                self.channel += 1
            else:
                self.channel = self.min_channel     # 현재 채널 값이 채널 최대값과 같으면 0으로 순환
            print('channel:', self.channel)

    def channeldown(self):
        if self.power == True:
            if self.channel > self.min_channel:
                self.channel -= 1
            else:
                self.channel = self.max_channel
            print('channel:', self.channel)

    def volumeup(self):
        if self.power == True:
            if self.volume < self.max_channel:
                self.volume += 1
            print('volume:', self.volume)

    def volumedown(self):
        if self.power == True:
            if self.volume > self.min_volume:
                self.volume -= 1
            print('volume:', self.volume)




tv1 = BasicTV(power=False, channel=0, volume=0)

print(tv1)
tv1.powerOnOff()
tv1.volumeup()
tv1.volumeup()
tv1.volumedown()
tv1.volumedown()
tv1.volumedown()

for _ in range(10):
    tv1.channeldown()
