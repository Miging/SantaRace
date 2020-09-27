from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.INVENTORY_BUTTON,False)
scene=Scene("산타레이스","images/background.png")

santa=Object('images/santa.png')
santa.x=0
santa.y=500
santa.locate(scene,santa.x,santa.y)
santa.show()


playbutton=Object('images/play.png')
playbutton.locate(scene,610,30)

startbutton=Object('images/start.png')
startbutton.locate(scene,590,70)
startbutton.show()

endbutton=Object('images/end.png')
endbutton.locate(scene,590,20)
endbutton.show()

timer=Timer(10.)
showTimer(timer)
def playButton_onMouse(x,y,action):
    santa.x=santa.x+30
    santa.locate(scene,santa.x,santa.y)

    if santa.x>1280:
        showMessage('선물 배달 성공~~~~')
        playbutton.hide()
        startbutton.setImage("images/restart.png")
        startbutton.show()
        endbutton.show()

        timer.stop( )
        
playbutton.onMouseAction=playButton_onMouse

def startButton_onMouse(x,y,action):
    startbutton.hide()
    endbutton.hide()
    playbutton.show()


    timer.set(10.)
    timer.start()

    santa.x=0
    santa.locate(scene,santa.x,santa.y)
startbutton.onMouseAction=startButton_onMouse

def endButton_onMouse(x,y,action):
    endGame()
endbutton.onMouseAction=endButton_onMouse

def timer_onTimeout():
    showMessage('선물 배달 실패 ㅜ')
    playbutton.hide()
    startbutton.setImage("images/restart.png")
    startbutton.show()
    endbutton.show()
timer.onTimeout=timer_onTimeout


startGame(scene)
