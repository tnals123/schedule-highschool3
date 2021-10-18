import tkinter
import random
import math
trival=0
window=tkinter.Tk()
window.title('몬티홀 딜레마')
window.resizable(False,False)
window.geometry('740x600+200+200')
image=tkinter.PhotoImage(file='C:\\Users\\sumin\\Desktop\\몬티홀 딜레마 실험\\sheep.png')
image2=tkinter.PhotoImage(file='C:\\Users\\sumin\\Desktop\\몬티홀 딜레마 실험\\car.png')
image3=tkinter.PhotoImage(file='C:\\Users\\sumin\\Desktop\\몬티홀 딜레마 실험\\download.png')
# 버튼 세개에 숨겨진 이미지 세개를 랜덤으로 넣어야돼
# 셋 중에 하나를 선택하면 선택한 것을 제외한 다른것들중에 염소가 있는것 나타내기



f=open('C:/Users/sumin/Desktop/Python 3.7/몬티홀 딜레마 실험.txt','w')
data='''몬티홀 딜레마 실험.당신은 3개의 문 중 하나를 골라 그 문 뒤에 있는 상품을 받는다.
하나의 문 뒤에는 포르쉐 자동차가 있고 나머지 2개 뒤에는 염소가 있다.
당신이 문을 선택하면 진행자는 나머지 2개 중 염소가 있는 문을 연다.
이제 당신은 처음 고른 문을 계속 선택하거나 아직 닫혀 있는 다른 문으로 바꿀 수 있다.'''

f.write(data)
f.close()

def restart():
    
    global button
    global button2
    global button3
    global trival
    global count
    
   # 다시 배열해야함
   
    button.destroy()
    button2.destroy()
    button3.destroy()
    
    a=['자동차','염소','염소']
    random.shuffle(a)
    [button,button2,button3]=a
    
    
    
    
    if button=='자동차':
       
        def rhdudwns():
            global trival
            trival=trival+1
            
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            b=[button2,button3]
            x1,x2=random.sample(b,2)
            x1['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')           
            def whtnals1():
                global count
                x2['image']=image
                button['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2),2),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                x2['image']=image
                button['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2),2),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
        def rhdudwns1():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            
            
            button3['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                global count
                button2['image']=image
                button['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                button2['image']=image
                button['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:[0%]'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)

            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()


        def rhdudwns2():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            button2['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                global count
                button3['image']=image
                button['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                button3['image']=image
                button['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
                

            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
                


    #두번째 버튼이 자동차일때
    if button2=='자동차':
        
        def rhdudwns():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            button3['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
           
            def whtnals1():
                global count
                button['image']=image
                button2['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                button['image']=image
                button2['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
        def rhdudwns1():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            b=[button,button3]
            x1,x2=random.sample(b,2)
            x1['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                global count
                x2['image']=image
                button2['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                x2['image']=image
                button2['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
        def rhdudwns2():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            button['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                button2['image']=image2
                button3['image']=image
                global count
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                button2['image']=image2
                button3['image']=image
                global count
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
    #세 번째 버튼이 자동차일 때
    if button3=='자동차':
        def rhdudwns():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            button2['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                global count
                button['image']=image
                button3['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                button['image']=image
                button3['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
        def rhdudwns1():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            button['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')
            def whtnals1():
                global count
                button2['image']=image
                button3['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                button2['image']=image
                button3['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
        def rhdudwns2():
            global trival
            trival=trival+1
            root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
            root.place(x=20,y=400)
            b=[button,button2]
            x1,x2=random.sample(b,2)
            x1['image']=image
            window2=tkinter.Tk()
            window2.resizable(False,False)
            window2.geometry('100x100+100+100')           
            def whtnals1():
                global count
                x2['image']=image
                button3['image']=image2
                count=count+1
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            def whtnals2():
                global count
                x2['image']=image
                button['image']=image2
                
                root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
                root1.place(x=20,y=500)
                window2.destroy()
                root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
                root3.place(x=500,y=400)
            button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
            button4.pack()      
            button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
            button5.pack()
            window2.mainloop()
    button =tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns)
    button.place(x=50,y=50)
    button2=tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns1)
    button2.place(x=280,y=50)
    button3=tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns2)
    button3.place(x=510,y=50)
    button4=tkinter.Button(window,text='다시 하기!',font='Helvetica 18 bold',bg='white',relief='groove',command=restart)
    button4.place(x=500,y=500)
    
        
   
    

    
    
    


count=0

a=['자동차','염소','염소']
random.shuffle(a)
[button,button2,button3]=a

# 첫번째 버튼이 자동차일때
if button=='자동차':
    trival=trival+1
    def rhdudwns():
        global trival
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        b=[button2,button3]
        x1,x2=random.sample(b,2)
        x1['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')           
        def whtnals1():
            global count
            x2['image']=image
            button['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            x2['image']=image
            button['image']=image2
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    def rhdudwns1():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        
        
        button3['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            global count
            button2['image']=image
            button['image']=image2            
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            button2['image']=image
            button['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)

        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()


    def rhdudwns2():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        button2['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            global count
            button3['image']=image
            button['image']=image2           
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            button3['image']=image
            button['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
            

        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
            


#두번째 버튼이 자동차일때
if button2=='자동차':
    
    def rhdudwns():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        button3['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
       
        def whtnals1():
            global count
            button['image']=image
            button2['image']=image2 
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            button['image']=image
            button2['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    def rhdudwns1():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        b=[button,button3]
        x1,x2=random.sample(b,2)
        x1['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            global count
            x2['image']=image
            button2['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            x2['image']=image
            button2['image']=image2
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    def rhdudwns2():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        button['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            button2['image']=image2
            button3['image']=image
            global count
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            button2['image']=image2
            button3['image']=image
            global count
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
#세 번째 버튼이 자동차일 때
if button3=='자동차':
    def rhdudwns():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        button2['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            global count
            button['image']=image
            button3['image']=image2 
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            button['image']=image
            button3['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    def rhdudwns1():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        button['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')
        def whtnals1():
            global count
            button2['image']=image
            button3['image']=image2 
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            button2['image']=image
            button3['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    def rhdudwns2():
        global trival
        trival=trival+1
        root=tkinter.Label(window,text='%s 번 시도 하셨습니다.'%trival,font='Helvetica 18 bold')
        root.place(x=20,y=400)
        b=[button,button2]
        x1,x2=random.sample(b,2)
        x1['image']=image
        window2=tkinter.Tk()
        window2.resizable(False,False)
        window2.geometry('100x100+100+100')           
        def whtnals1():
            global count
            x2['image']=image
            button3['image']=image2
            count=count+1
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        def whtnals2():
            global count
            x2['image']=image
            button['image']=image2
            root1=tkinter.Label(window,text='%s 번 성공 하셨습니다.'%count,font='Helvetica 18 bold')
            root1.place(x=20,y=500)
            window2.destroy()
            root3=tkinter.Label(window,text='성공률:{:.0%}'.format(round(count/trival,2)),font='Helvetica 18 bold')
            root3.place(x=500,y=400)
        button4=tkinter.Radiobutton(window2,text='선택 유지!',value=1,indicatoron = 0,command=whtnals1)
        button4.pack()      
        button5=tkinter.Radiobutton(window2,text='선택 변경!',value=2,indicatoron = 0,command=whtnals2)
        button5.pack()
        window2.mainloop()
    
    

   
        


                
            
            

    
            
        

button=tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns)
button.place(x=50,y=50)
button2=tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns1)
button2.place(x=280,y=50)
button3=tkinter.Button(window,text='asdf',width='150',height='300',image=image3,bg='white',relief='groove',command=rhdudwns2)
button3.place(x=510,y=50)
button4=tkinter.Button(window,text='다시 하기!',font='Helvetica 18 bold',bg='white',relief='groove',command=restart)
button4.place(x=500,y=500)

window.mainloop()




