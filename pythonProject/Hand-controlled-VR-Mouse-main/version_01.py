#===== Importing Required Modules ==========================================
from pyautogui import click, moveTo, size
import cv2
import mediapipe as mp

from win32com.client import Dispatch

from math import hypot
from numpy import interp
from time import sleep
import time

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from plyer import notification
from socket import create_connection
from webbrowser import open

from os import startfile

from pygame import mixer
mixer.init()
#================================================================================
class Handdetector:
    def __init__(self,mode=False,max_hands=1,detection_con=0.5,track_confidence=0.5):
        """Used to detect the Hand position, it's Finger-Up state ,and \n To draw the Landmarks of the hand """
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(mode,max_hands,1,detection_con,track_confidence)
        self.mpdraw = mp.solutions.drawing_utils
        
        self.fingerup_list, self.lm_list = [], []
        self.tip_id = [4,8,12,16,20]
        self.close_tip_id = [5,6,10,14,18]
        self.hand_side = None

    def findhand(self,img,draw=False,fliped_img=True):
        #=== Getting the image in BGR format ====================================
        #=== Then flipping the image for better understanding ===================
        self.fliped_img = fliped_img
        RGBimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        if self.fliped_img:
            self.img = img  
        else:
            self.img =  cv2.flip(img,1)
            RGBimg = cv2.flip(RGBimg,1)
        #=== Processing the Hand position and ===================================
        self.result = self.hands.process(RGBimg)
        #=== Drawing the Landmarks of the Hand, if given draw ===================
        if self.result.multi_hand_landmarks:        
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self,handno=0):
        lm_list = [ ]
        if self.result.multi_hand_landmarks:    
            given_hand = self.result.multi_hand_landmarks[handno]
            for id, lm in enumerate(given_hand.landmark):
                    h ,w , c = self.img.shape
                    cx, cy = int(lm.x*w),int(lm.y*h)
                    lm_list.append([id,cx,cy])
        self.lm_list = lm_list
        return lm_list

    def fingersUp(self):
        self.fingerup_list = []
        if len(self.lm_list) != 0:
            #==== Checking whther left hand or right hand =======================
            #==== And then determining the Thumb state:- Open or Close ==========
            if self.lm_list[0][1] > self.lm_list[1][1]:
                self.hand_side = 'right'
                if self.lm_list[self.tip_id[0]][1] < self.lm_list[self.close_tip_id[0]][1]  :
                    self.fingerup_list.append(1)
                else: self.fingerup_list.append(0)
            else :
                self.hand_side = 'left'
                if self.lm_list[self.tip_id[0]][1] > self.lm_list[self.close_tip_id[0]][1]  :
                    self.fingerup_list.append(1)
                else: self.fingerup_list.append(0)
            #==== Checking the state of the Fingers:- Open or Close =============
            for id in range(1,5):
                if self.lm_list[self.tip_id[id]][2] < self.lm_list[self.close_tip_id[id]][2]:
                    self.fingerup_list.append(1)
                else: self.fingerup_list.append(0)
            #====================================================================
        return self.fingerup_list
    
    def findDistance(self,img,F1,F2,draw_f=True,draw_line=True,draw_cntr=False,finger_up=True):
        f1 = self.tip_id[F1]
        f2 = self.tip_id[F2]
        distance = 0
        cx, cy = 0 ,0
        def find():
            f1_x,f1_y = self.lm_list[f1][1:]
            f2_x,f2_y = self.lm_list[f2][1:]
            cx,cy = (f1_x+f2_x)//2, (f1_y+f2_y)//2 
            if draw_line:
                cv2.line(img,(f1_x,f1_y),(f2_x,f2_y),(61,90,128),4)
            if draw_f:
                cv2.circle(img,(f1_x,f1_y),10,(0,29,62),cv2.FILLED)
                cv2.circle(img,(f1_x,f1_y),7,(0,53,102),cv2.FILLED)
                cv2.circle(img,(f2_x,f2_y),10,(0,29,62),cv2.FILLED)
                cv2.circle(img,(f2_x,f2_y),7,(0,53,102),cv2.FILLED)
            if draw_cntr:
                cv2.circle(img,(cx,cy),8,(224,251,252),cv2.FILLED)

            dis = hypot(f2_x - f1_x,f2_y - f1_y)
            return dis, (cx, cy)
        if self.lm_list and self.fingerup_list:
            if finger_up:
                if (self.fingerup_list[F1] == self.fingerup_list[F2] == 1):
                    distance, (cx, cy) = find()
                else:
                    pass 
                    #print("Keep finger up")
            else:
                distance = find()
            return [distance , (cx, cy)]
#=============== Machine Voice ==================================================
voice_engine = Dispatch('SAPI.Spvoice')

def say(audio):
    """Used to Speak the text, given audio parameter"""
    voice_engine.Speak(audio)

say('Machine Voice connected')
#=============== Main Program ===================================================
def main():
    def change_volume(volume_prcnt):
        """Changes the volume of the system using the distance b/w Thumb & Index Finger. \n 
        return volume_prcnt"""
        dis, cntr = Hand_detector.findDistance(Main_img,0,1)    
        change_vol = False
        if cntr and dis :
            cx, cy = cntr
            if dis < 50:
                cv2.circle(Main_img,(cx,cy),16,(233,216,166),cv2.FILLED)
                volume_prcnt -= 3
                change_vol = True
            elif dis > 120:
                cv2.circle(Main_img,(cx,cy),16,(148,210,189),cv2.FILLED)
                volume_prcnt += 3
                change_vol = True
            if change_vol:
                if volume_prcnt>=100: volume_prcnt = 99
                elif volume_prcnt<=0: volume_prcnt = 1
                volum = interp(volume_prcnt,[0,100],[vol_range[0],vol_range[1] ])
                volume.SetMasterVolumeLevel(volum, None)
        return volume_prcnt
    #===========================================================================
    def change_music_state(Music_state,check_music_state_if_paused=False,sys_say=True):
        """Play or Pause the Music with the given 'Music_state' parameter"""
        if Music_state.lower() == 'play':
            if check_music_state_if_paused:
                mixer.music.unpause()
                check_music_state_if_paused = False
            else: mixer.music.play()
            say('playing music')
        elif Music_state.lower() == 'pause': 
            mixer.music.pause()
            check_music_state_if_paused = True
            if sys_say:say('Music is Paused')
        return check_music_state_if_paused
    #===========================================================================
    def check_con():
        """Returns True if internet is connected, else False"""
        try:
            create_connection(("Google.com",80))
            return True
        except OSError:
            return False
    #===========================================================================
    def check_in_fing(point_list=[0,0],box=0):
        """If finger is in box zero, it returns True; else False. \n
           If given box=1, then it returns the box_no on which the finger is."""
        if box==0:
            if start_x < point_list[0] < end_x and start_y < point_list[1] < end_y:
                return True
            return False
        elif box==1:
            if start_x < point_list[0] < mid_x and start_y < point_list[1] < end_y:
                return '1'
            elif mid_x < point_list[0] < end_x and start_y < point_list[1] < end_y:
                return '2'
            return '0'
    #===========================================================================
    def check_swipe_motion(finger_list=[]):
        """Returns the swipe done by the Hand-detected either in +ve direction['pos'] or -ve direction['neg']"""
        fing_len = len(finger_list)
        swipe = None
        if fing_len > 5:
            [x1, y1] = finger_list[0]
            [x2, y2] = finger_list[fing_len - 1]
            #===========================
            x = int(x2 - x1)
            y = int(y2 -y1)
            if x1 > x2: x *= -1
            if y1 > y2: y *= -1
            #===========================
            if x < 30 and y > 100:
                if y2 > y1 : swipe = 'pos'
                else: swipe = 'neg'
            #===========================
            # if x > 100 and y < 30:
            #     if x2 > x1 : swipe = 'right'
            #     else: swipe = 'left'
            return swipe
    #===========================================================================
    def Get_state_swipe(swipe):
        """Returns the state of the Swipe-gesture, and the swipe if fingers are in same box"""
        F1_box = check_in_fing(lm_list[8][1:],1)
        F2_box = check_in_fing(lm_list[12][1:],1)
        if F1_box == F2_box:
            state = 'Quit' if F1_box == '1' else 'To-do'
        else:
            state = 'Swipe'
        finger_pos_for_swipe.append(lm_list[12][1:])
        if len(finger_pos_for_swipe) > 30:
            finger_pos_for_swipe.pop(0)
        if state in ['Quit', 'To-do']:
            swipe = check_swipe_motion(finger_pos_for_swipe)
        return state, swipe
    #===========================================================================
    def mouse_pointer_click(centre, dis, Clicked):
        """Clicks the Pointer at it's place when Index & Middle Fingers are too close to each-other. \n
        Returns Clicked & state values."""
        cx,cy = centre
        Mouse_state = 0
        cv2.circle(Main_img,(cx,cy),15,(181,181,181),cv2.FILLED)   
        if Clicked >= 1: Clicked = 0

        if dis < 40:
            cv2.circle(Main_img,(cx,cy),15,(0,252,51),cv2.FILLED)
            if Clicked==0:
                Mouse_state = Clicked = 1
        elif dis > 55:
            Mouse_state = 0
        if Clicked == 1:
            Clicked += 1
        return Clicked, Mouse_state
    #===========================================================================
    Hand_detector = Handdetector()      # Creating hand-Detector 
    #===========================================================================
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate( IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    vol_range = volume.GetVolumeRange()
    volume_prcnt = 30
    #===========================================================================
    pointer_x, pointer_y = 0, 0
    #===========================================================================
    Thumb = Index_Finger = Middle_Finger = Ring_Finger = Pinky_Finger = 1
    sum_of_finger_state = 0
    finger_up_state = []
    prev_time, cur_time  =  0, 0        # Creating time counter to get the fps
    Clicked = 0
    Quit_confirm = False
    #===========================================================================
    Music_state_to_do = "Play"
    Music_state = 'Pause'
    check_music_state_if_paused = False
    #===========================================================================
    # music_file_loc = 'E:\\Assets & Extras\\New fold\\Twin Musicom - Seven Lives to Live.mp3'
    # mixer.music.load(music_file_loc)
    #===========================================================================
    finger_pos_for_swipe = []
    countdown = 0
    #===========================================================================
    path_to_vscode = "C:\\Users\\gokul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #===========================================================================
    start_x, start_y, end_x, end_y = 200, 60, 500, 230
    mid_x = (start_x + end_x)//2
    scrn_width, scrn_height = size()
    #===========================================================================
    say('Getting Camera')
    cap = cv2.VideoCapture(0)           # Creating Camera object
    cam_width,cam_height = 960,720      # And setiing up it's
    cap.set(3,cam_width)                # Width and Height
    cap.set(4,cam_height)               # According to ourself
    # print('Camera-connected')
    say('Camera connected')
    #===========================================================================
    while True:
        _ , cap_img = cap.read()
        cur_time = time.time()
        Main_img = cv2.flip(cap_img,1)
        #========================================================================
        swipe = 'None'
        state = 'None'
        Hand_Detection_check = False
        Main_img = Hand_detector.findhand(Main_img,True)
        lm_list = Hand_detector.findPosition()
        #========================================================================
        if lm_list:
            finger_up_state = Hand_detector.fingersUp()
            Hand_Detection_check = True
            #=============== Checking & Changing finger's State =====================
            if finger_up_state:
                [Thumb,Index_Finger,Middle_Finger,Ring_Finger,Pinky_Finger] = finger_up_state
                sum_of_finger_state = sum(finger_up_state[1:])
                #================================================================
                Index_finger_in = check_in_fing(lm_list[8][1:])
                Thumb_in = check_in_fing(lm_list[4][1:])
                Middle_finger_in = check_in_fing(lm_list[12][1:])
                # Ring_Finger_in = check_in_fing(lm_list[16][1:])
                #===================================================================
                #== Get Cursor Co-ordinates ====================================
                if (sum_of_finger_state == 1 and Index_Finger == 1):
                    px, py = lm_list[8][1:]                        
                    pointer_x = int(interp(px,(start_x,end_x),(0,scrn_width)))
                    pointer_y = int(interp(py,(start_y,end_y),(0,scrn_height)))
                    #==== Mouse Pointer Movement ===============================
                    state = "Mouse Pointer"
                    cv2.circle(Main_img,(px,py),5,(200,200,200),cv2.FILLED)
                    cv2.circle(Main_img,(px,py),10,(200,200,200),3)
                    if Index_finger_in:
                        moveTo(int(pointer_x),int(pointer_y))
                #== Check Clicked or Not =======================================
                elif sum_of_finger_state == 2 and (Index_Finger == Middle_Finger == 1):
                    [dis , centre ]= Hand_detector.findDistance(Main_img,1,2)
                    if centre and (Index_finger_in and Middle_finger_in) and dis:
                        Clicked, Mouse_clicked = mouse_pointer_click(centre,dis,Clicked)
                        #==== Mouse Click ===========================================
                        state = 'Mouse Pointer Clicked' if Mouse_clicked else 'Mouse Pointer Clickable'
                        if Clicked == 2: click(pointer_x,pointer_y)
                #==== Swipe Gesture & Mouse Control ============================
                if sum_of_finger_state == 3 and (Index_Finger == Middle_Finger == Ring_Finger == 1):
                    cv2.line(Main_img,(mid_x,start_y),(mid_x,end_y),(222,222,222),2)
                    cv2.putText(Main_img,'Quit',(250,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,155,238),2)
                    cv2.putText(Main_img,f'{Music_state_to_do} Music',(195,210),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,155,238),2)
                    cv2.putText(Main_img,'Open Google',(370,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,155,238),2)
                    cv2.putText(Main_img,'Open Vscode',(355,210),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,155,238),2)
                    if (Index_finger_in and Middle_finger_in):
                        state, swipe = Get_state_swipe(swipe)
                #==== Volume Changing by Thumb and Index finger =================
                elif sum_of_finger_state == 2 and (Index_Finger == Pinky_Finger == 1) and (Ring_Finger == Middle_Finger == 0):
                    state = 'Volume Change'
                    cv2.putText(Main_img,f'Vol.:-{volume_prcnt}',(50,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(165,255,214),2)
                    if (Thumb_in and Index_finger_in):
                        volume_prcnt = change_volume(volume_prcnt)
        #======= Swipe Gesture Process ==========================================
        if swipe in ['pos','neg']:
            if state == 'Quit':
                #=== Quit check =================================================
                if swipe == 'pos': Quit_confirm = True
                #=== Music state check ==========================================
                elif swipe == 'neg':
                    countdown = 5
                    Music_state_to_do, Music_state = Music_state, Music_state_to_do
                    # check_music_state_if_paused = change_music_state(Music_state,check_music_state_if_paused)
            elif state == 'To-do':
                #=== To-do Task 1  ==============================================
                if swipe == 'pos':
                    countdown = 5
                    internet_con = check_con()
                    if internet_con:
                        say('Opening google')
                        open('google.com')
                    else:
                        notification.notify(title='Connection Falied',message='Internet Connection is unstable or not connected', timeout=5)
                        say('Connection failed')
                        say('unable to connect gogle')
                #=== To-do Task 1  ==============================================
                elif swipe == 'neg':
                    countdown = 5
                    say('opening Vs code')
                    startfile(path_to_vscode)
        #======= Finger Pos list check for non-swipe work =======================
        if (state not in ['Quit','To-do','Swipe']) or (countdown>0): 
            finger_pos_for_swipe = []
            if countdown>0: countdown -= 1
        #======= Displaying the FPS of the CV Apk ===============================
        fps = 1/(cur_time-prev_time)
        prev_time = cur_time
        cv2.putText(Main_img,f'FPS:- {int(fps)}',(20,60),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(200,250,255),2)
        #========================================================================
        cv2.rectangle(Main_img,(start_x, start_y),(end_x, end_y),(0,0,255),1)
        #========================================================================
        cv2.putText(Main_img,f'Detection :-{Hand_Detection_check}',(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(165,255,214),2)
        cv2.putText(Main_img,f'State :-{state}',(250,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(165,255,214),2)
        #======== Displaying the Main Image =====================================
        cv2.imshow('Flipped Image',Main_img)
        if cv2.waitKey(10) == ord("q"): Quit_confirm = True
        #======= Quiting the apk ================================================
        if Quit_confirm:
            if Music_state == 'Play': 
                change_music_state('Pause',sys_say=False)
            say('Quitting')
            sleep(2)
            break

if __name__== '__main__':
    main()