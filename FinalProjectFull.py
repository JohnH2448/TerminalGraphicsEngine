# AI statement: Statues and Pillars are AI generated. The AI simply wrote pixel locations using my render function. This is doable by hand
# however I am no artist and it's time consuming to do manually. The formula for update_render() also used math help from AI, although I wrote it.

# I put more effort into this game than required because I do need a good EGR grade for my scholarship! I'm new to programming
# as of this semester, but I wanted to try slightly more advanced concepts. I hope you enjoy the game!

# This engine can support any game that you can simulate physics for. Feel free to mess around with the engine, I'll attach a blank version
# with no game code in case you want to try it yourself. 

import random
import time
import sys
import keyboard
import math

Dev=input("Dev Code? (Press Enter)")
if Dev=="1" or Dev=="3":
    cheats=True
else:
    cheats=False
validate=0
if cheats==False and Dev!="2":
    for i in "0Install Keyboard Commands ('pip install keyboard' in Teminal)00Controls:0A = Left0D = Right0Space = Double Jump00Bugs:0- Python side: Color pallete can be unpredictably offset permenantly0- Hitboxes are not accurate0- Inconsistent performence even with same IDE and hardware0- Can fail to render all pixels each frame (restart and reduce pixels/s)00Notes:0- Game should smoothly run and render with reccomended settings0- Must have keyboard module installed0- Dev code 1 for quick start0- Dev code 2 for idle screen0- Dev code 3 for developer mode0- Fullscreen only0- Reccomended FOV is 6Ox3O0- Recommended FPS is 2O0":
            if i=="0":
                print("")
            else:
                print(i, end="", flush=True)
                time.sleep(0.01)
    input("(Press Enter)")
    while validate==0:
        displayX=input("\nScreen Width? (10-80): ")
        displayY=input("Screen Height? (10-30): ")
        framerate=input("Frame Rate? (5-50): ")
        if displayX.isdigit() and displayY.isdigit() and framerate.isdigit():
            displayX=int(displayX)
            displayY=int(displayY)
            framerate=int(framerate)
            if displayX>80 or displayX<10 or displayY>30 or displayY<10 or framerate>50 or framerate<5:
                print("Invalid! Out of Range")
            else:
                validate=1
        else:
            print("Invalid! Enter Numbers Only")
    print(displayX*displayY*framerate,"Pixels/S")
    input("Press Enter to Start...")
else:
    displayX=60
    displayY=30
    framerate=20


# Modifiables
idle=True
gameOn=True
fakeVariable=True

# Frame Rate Calculator
frameExecute=1
time1=time.perf_counter()
def calculateFPS():
    global time3 
    global time1
    global frameExecute
    time2=time.perf_counter()
    time3=time2-time1
    if (1/framerate) <= time3:
        time1=time.perf_counter()
        frameExecute=1

# Physics Frame Rate Calculator
physicsExecute=1
Ptime1=time.perf_counter()
def calculatePFPS():
    global Ptime3 
    global Ptime1
    global physicsExecute
    Ptime2=time.perf_counter()
    Ptime3=Ptime2-Ptime1
    if (1/50) <= Ptime3:
        Ptime1=time.perf_counter()
        physicsExecute=1

# Rendering Translator
def update_render(x_coord, y_coord, pixel):
    if 0 <= x_coord < displayX and 0 <= y_coord < displayY:
        y_row = displayY - y_coord - 1
        x_col = x_coord
        output = (displayX * y_row) + x_col
        display[output][0] = pixel[0]
        display[output][1] = pixel[1]
        display[output][2] = pixel[2]

# Reverse Translator
def reverse_render(index):
    index=int(index)
    y_row = index // displayX  
    x_col = index % displayX  
    y_coord = displayY - 1 - y_row  
    x_coord = x_col  
    return (x_coord, y_coord)

# Physics Engine (Physics are ran 50 FPS)
charX=5
charY=5
yVelocity=0
xVelocity=0
grounded=False
charX=round(displayX/2)
centerX=charX
enemyMove=0
Enemyoffset=0
EnemyAlive=True
hurt=False
m=0
meteorY=20
RealmeteorX=5
DarkProg=0
Dark=0
sky2 =0
sky1 =0
sky3 =0
night=False
health=3
def Physics_Tick():
    global charX
    global charY
    global physicsExecute
    global xVelocity
    global yVelocity
    global grounded
    global centerX
    global enemyMove
    if physicsExecute==1:

        centerX=centerX+xVelocity
        charY=charY+yVelocity
        yVelocity=yVelocity - 0.02

        if abs(xVelocity) < 0.01:
            xVelocity = 0
        else:
            xVelocity = xVelocity * 0.9

        if keyboard.is_pressed('d'):
            xVelocity=xVelocity+0.06
        if keyboard.is_pressed('a'):
            xVelocity=xVelocity-0.06
        if charY<5:
            grounded=True
            yVelocity=0.35
        if keyboard.is_pressed(' ') and grounded==True:
            yVelocity=0.35
            grounded=False
        physicsExecute=0
        enemyMove=1

# Generates Default Display
pixel=[72,111,56]
print(str(displayX)+"x"+str(displayY), "Display")
display=[]
i=0
while i<displayX*displayY:
    display.append(pixel.copy())
    i=i+1


# Rendering Engine
def Render_Frame():
    global frameExecute
    if frameExecute==1:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        v=0
        for i in display:
            r,g,b=i[0],i[1],i[2]
            v=v+1
            print(f"\033[38;2;{r};{g};{b}m{"\u2588"}\033[0m", end="")
            print(f"\033[38;2;{r};{g};{b}m{"\u2588"}\033[0m", end="")
            if v==displayX:
                if Dev=="3":
                    print("",xVelocity)
                else:
                    print("")
                v=0
        frameExecute=0
        if Dev=="3":
            print(Dark,yVelocity,centerX,Enemyoffset,grounded,enemyMove,EnemyAlive,hurt,meteorY,)

# Game On
while gameOn==True:

    # Idle Display
    g=0
    while idle==True:
        calculateFPS()
        if frameExecute==1:
            for i in display:
                i[0] = random.randint(0, 255)
                i[1] = random.randint(0, 255)
                i[2] = random.randint(0, 255) 
            Render_Frame()
            g=g+1
        if g>=15:
            if Dev !="2":
                idle=False
    
    # Day Night Cycle
    if physicsExecute==1:
        if Dark>=0.8 or Dark<0.2:
            DarkProg=DarkProg+0.005
        else:
            DarkProg=DarkProg+0.01
        Dark = round(max(0.1, min(0.9, (math.sin(DarkProg) / 2) + 0.55)),2)
    if Dark>=0.8:
        night=True
    else:
        night=False

    # Background
    j=0
    for i in display:
        x,y=reverse_render(j)
        # day night cycle math was more complex than I wanted, what this does is essentially makes a unit of y so that at the
        # top of the display y=1 and and the bottom y=0, then the multiple of that is = to the weight I want it to take up of
        # the total rgb calculation. Functionally controls how harsh the gradient is and integrates that with "Dark"
        sky1 = round(135-(((y/(displayY))*50)+84*Dark))
        sky2 = round(206-(((y/(displayY))*50)+155*Dark))
        sky3 = round(235-(((y/(displayY))*50)+184*Dark))
        if y==4:
            pixel=[72,111,56]
            update_render(x,y,pixel)
        elif y==3:
            pixel=[210, 180, 140]
            update_render(x,y,pixel)
        elif y==2:
            pixel=[200, 170, 130]
            update_render(x,y,pixel)
        elif y==1:
            pixel=[190, 160, 120]
            update_render(x,y,pixel)
        elif y==0:
            pixel=[180, 150, 110]
            update_render(x,y,pixel)
        else:
            pixel = [sky1,sky2,sky3]
            update_render(x,y,pixel)
        j=j+1
    

    # AI Generated "Roman Pillars" Art
    if fakeVariable==True:
        pilX=round(0-centerX)
        pilY=5
        # Render 10 Roman-style pillars spaced 8 blocks apart with connected tops
        for i in range(10):  # Render 10 pillars
            current_pilX = pilX + i * (5 + 8)  # Calculate the x-coordinate of each pillar
            # Render the pillar itself
            for y in range(pilY, pilY + 20):  # Height of 20 units
                for x in range(current_pilX, current_pilX + 5):  # Width of 5 units
                    # Base of the pillar (first 2 units)
                    if y < pilY + 2:
                        update_render(x, y, [180, 140, 100])  # Darker color for the base
                    # Shaft of the pillar (middle section)
                    elif pilY + 2 <= y < pilY + 18:
                        if (x - current_pilX) % 2 == 0:  # Fluting effect (alternating light and dark stripes)
                            update_render(x, y, [200, 200, 200])  # Light gray
                        else:
                            update_render(x, y, [160, 160, 160])  # Darker gray
                    # Capital of the pillar (top 2 units)
                    else:
                        update_render(x, y, [220, 200, 180])  # Decorative capital color
                # Top-left corner decoration
        update_render(pilX - 1, pilY + 19, [220, 200, 180])  # Top-left corner pixel
        update_render(pilX - 1, pilY + 18, [220, 200, 180])  # Below the top-left corner
        update_render(pilX - 2, pilY + 19, [220, 200, 180])  # Left of the top-left corner
        update_render(pilX, pilY + 19, [220, 200, 180])      # Right of the top-left corner

        # Top-right corner decoration
        rightmost_pilX = pilX + (9 * (5 + 8)) + 4  # Adjust for the rightmost pillar
        update_render(rightmost_pilX + 1, pilY + 19, [220, 200, 180])  # Top-right corner pixel
        update_render(rightmost_pilX + 1, pilY + 18, [220, 200, 180])  # Below the top-right corner
        update_render(rightmost_pilX + 2, pilY + 19, [220, 200, 180])  # Right of the top-right corner
        update_render(rightmost_pilX, pilY + 19, [220, 200, 180])      # Left of the top-right corner
        # Connect the tops of pillars
        for i in range(9):  # Connect between each pair of pillars (9 gaps between 10 pillars)
            beam_startX = (pilX + i * (5 + 8) + 5)-1  # Start where the current pillar ends
            beam_endX = (pilX + (i + 1) * (5 + 8))+1  # End where the next pillar begins
            for x in range(beam_startX, beam_endX):  # Horizontal beam spans the gap
                for y in range(pilY + 18, pilY + 20):  # Beam height (aligned with capitals)
                    update_render(x, y, [220, 200, 180])  # Same color as the capital for consistency

    # AI Generated "Statue" Art
    if fakeVariable==True:
        statueX=round(-10-centerX)
        statueY=7
        pixel = [160,160,160]
        update_render(statueX-1, statueY+9, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+9, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+9, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+8, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+8, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+8, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+7, pixel)
        pixel = [160,160,160]
        update_render(statueX-2, statueY+6, pixel)
        pixel = [120,120,120]
        update_render(statueX-1, statueY+6, pixel)
        update_render(statueX, statueY+6, pixel)
        update_render(statueX+1, statueY+6, pixel)
        pixel = [80,80,80]
        update_render(statueX+2, statueY+6, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+5, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+5, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+5, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+4, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+4, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+4, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+3, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+2, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+2, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+2, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+1, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+1, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+1, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY, pixel)
        pixel = [160,160,160]
        update_render(statueX-2, statueY-1, pixel)
        pixel = [120,120,120]
        update_render(statueX-1, statueY-1, pixel)
        update_render(statueX, statueY-1, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY-1, pixel)
        update_render(statueX+2, statueY-1, pixel)
        for dx in range(-3, 4):
            pixel = [160,160,160] if dx < 0 else [80,80,80] if dx > 0 else [120,120,120]
            update_render(statueX + dx, statueY - 2, pixel)
        # Statue 2
        statueX=round(131-centerX)
        statueY=7
        pixel = [160,160,160]
        update_render(statueX-1, statueY+9, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+9, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+9, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+8, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+8, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+8, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+7, pixel)
        pixel = [160,160,160]
        update_render(statueX-2, statueY+6, pixel)
        pixel = [120,120,120]
        update_render(statueX-1, statueY+6, pixel)
        update_render(statueX, statueY+6, pixel)
        update_render(statueX+1, statueY+6, pixel)
        pixel = [80,80,80]
        update_render(statueX+2, statueY+6, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+5, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+5, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+5, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+4, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+4, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+4, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+3, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+2, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+2, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+2, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY+1, pixel)
        pixel = [120,120,120]
        update_render(statueX, statueY+1, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY+1, pixel)
        pixel = [160,160,160]
        update_render(statueX-1, statueY, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY, pixel)
        pixel = [160,160,160]
        update_render(statueX-2, statueY-1, pixel)
        pixel = [120,120,120]
        update_render(statueX-1, statueY-1, pixel)
        update_render(statueX, statueY-1, pixel)
        pixel = [80,80,80]
        update_render(statueX+1, statueY-1, pixel)
        update_render(statueX+2, statueY-1, pixel)
        for dx in range(-3, 4):
            pixel = [160,160,160] if dx < 0 else [80,80,80] if dx > 0 else [120,120,120]
            update_render(statueX + dx, statueY - 2, pixel)

    # AI Generated "Greek God" Art
    if fakeVariable==True:
        # Starting position below the statue base
        decorationX = round(-20 - centerX)
        decorationY = 8

        # Colors for the decoration
        stone_color = [170, 170, 170]  # Light grey for the marble
        dark_stone_color = [120, 120, 120]  # Dark grey for damaged stone
        column_base_color = [140, 130, 90]  # Earthy column base color
        shadow_color = [90, 90, 90]  # Shadow color for depth

        # Top section of the decorative art (near statue)
        for x in range(decorationX - 2, decorationX + 3):
            update_render(x, decorationY + 9, stone_color)  # Top outline
        for x in range(decorationX - 1, decorationX + 2):
            update_render(x, decorationY + 8, dark_stone_color)  # Second row of decoration

        # Slight shading and detailing in the middle
        update_render(decorationX - 2, decorationY + 7, shadow_color)
        update_render(decorationX + 2, decorationY + 7, shadow_color)
        for x in range(decorationX - 1, decorationX + 2):
            update_render(x, decorationY + 7, stone_color)  # Central decoration

        # Adding column-like structures and shadows
        for x in range(decorationX - 3, decorationX + 4, 2):  # Columns in the background
            update_render(x, decorationY + 6, column_base_color)
            update_render(x, decorationY + 5, dark_stone_color)

        # Lower section of the decoration to add layers and richness
        for x in range(decorationX - 3, decorationX + 4, 2):
            update_render(x, decorationY + 4, stone_color)  # Lower decoration
        for x in range(decorationX - 3, decorationX + 4, 2):
            update_render(x, decorationY + 3, dark_stone_color)  # Further detail for depth

        # Shadow effects around the bottom edge
        for x in range(decorationX - 2, decorationX + 3):
            update_render(x, decorationY + 2, shadow_color)

        # Detailing the rubble and base using lighter colors for ground texture
        update_render(decorationX - 2, decorationY + 1, shadow_color)
        update_render(decorationX + 2, decorationY + 1, shadow_color)
        for x in range(decorationX - 1, decorationX + 2):
            update_render(x, decorationY + 1, stone_color)  # Adding texture to the rubble section

        # Base of the decoration, adding depth and broken column effect
        update_render(decorationX - 1, decorationY, dark_stone_color)
        update_render(decorationX + 1, decorationY, dark_stone_color)

        # Scatter some additional rubble or stone fragments
        update_render(decorationX, decorationY - 1, stone_color)
        update_render(decorationX, decorationY - 2, dark_stone_color)
        update_render(decorationX - 1, decorationY - 2, shadow_color)
        update_render(decorationX + 1, decorationY - 2, shadow_color)

        # Extra details: Broken fragments of columns and decorative stone details
        for dx in range(-2, 3, 1):
            update_render(decorationX + dx, decorationY - 3, dark_stone_color if dx % 2 == 0 else stone_color)

    # Oceans
    if fakeVariable==True:
        oceanX=round(150-centerX)
        oceanY=1
        for a in range(15, 100):
            update_render(a+oceanX, oceanY, [0, 0, 139])
        for a in range(10, 100):
            update_render(a+oceanX, oceanY+1, [0, 0, 139])
        for a in range(5, 100):
            update_render(a+oceanX, oceanY+2, [0, 0, 139])
        for a in range(1, 100):
            update_render(a+oceanX, oceanY+3, [0, 0, 139])
    
    # Ocean 2
    if fakeVariable==True:
        oceanX2=round(-50-centerX)
        oceanY2=1
        for a in range(15, 100):
            update_render(oceanX2-a, oceanY2, [0, 0, 139])
        for a in range(10, 100):
            update_render(oceanX2-a, oceanY2+1, [0, 0, 139])
        for a in range(5, 100):
            update_render(oceanX2-a, oceanY2+2, [0, 0, 139])
        for a in range(1, 100):
            update_render(oceanX2-a, oceanY2+3, [0, 0, 139])
    
    # Meteor
    if fakeVariable==True:
        meteorX=round(RealmeteorX-centerX)
        update_render(meteorX-1, round(meteorY)+2, [128,128,128])
        update_render(meteorX-1, round(meteorY), [128,128,128])
        update_render(meteorX, round(meteorY)-1, [128,128,128])
        update_render(meteorX-2, round(meteorY)-1, [128,128,128])
        update_render(meteorX+2, round(meteorY)-1, [128,128,128])
        update_render(meteorX, round(meteorY), [100, 100, 100])
        update_render(meteorX, round(meteorY)+1, [100, 100, 100])
        update_render(meteorX, round(meteorY)+2, [100, 100, 100])
        update_render(meteorX, round(meteorY)-2, [100, 100, 100])
        update_render(meteorX+1, round(meteorY)+1, [100, 100, 100])
        update_render(meteorX+2, round(meteorY), [100, 100, 100])
        update_render(meteorX-2, round(meteorY), [100, 100, 100])
        update_render(meteorX-2, round(meteorY)+1, [100, 100, 100])
        update_render(meteorX+1, round(meteorY)-1, [100, 100, 100])
        update_render(meteorX+1, round(meteorY)-2, [100, 100, 100])
        update_render(meteorX-1, round(meteorY)-2, [100, 100, 100])
        update_render(meteorX-1, round(meteorY)-1, [103, 14, 16])
        update_render(meteorX-1, round(meteorY)+1, [103, 14, 16])
        update_render(meteorX+1, round(meteorY), [103, 14, 16])
        update_render(meteorX+2, round(meteorY)+1, [103, 14, 16])
        update_render(meteorX+1, round(meteorY)+2, [103, 14, 16])
        update_render(meteorX+random.randint(-2, 2), round(meteorY)+random.randint(2, 5), [255, 165, 0])
        update_render(meteorX+random.randint(-1, 1), round(meteorY)+random.randint(3, 5), [255, 165, 0])
        update_render(meteorX+random.randint(-1, 1), round(meteorY)+random.randint(3, 5), [255, 165, 0])



    # Enemy Logic
    if EnemyAlive==True:
        if enemyMove==1:
            if enemyX>charX:
                Enemyoffset=Enemyoffset-0.15
            if enemyX<charX:
                Enemyoffset=Enemyoffset+0.15
            enemyMove=0
        enemyX=round(-20-centerX)+Enemyoffset
        enemyY=5
        update_render(round(enemyX), round(enemyY), [255,0,0])
        update_render(round(enemyX), round(enemyY+1), [255,0,0])
        update_render(round(enemyX), round(enemyY+2), [255, 218, 185])
    else:
        enemyX=round(-20-centerX)+Enemyoffset
        enemyY=5
        update_render(round(enemyX), round(enemyY), [255,0,0])
        update_render(round(enemyX+1), round(enemyY), [255,0,0])
        update_render(round(enemyX+2), round(enemyY), [255, 218, 185])
    if round(enemyX)==round(charX) and round(charY)==round(enemyY)+3 and EnemyAlive==True:
        EnemyAlive=False
        ressurect=0
    if (round(enemyX)==round(charX) or round(enemyX)-1==round(charX) or round(enemyX+1)==round(charX)) and (round(enemyY)==round(charY) or round(enemyY)+1==round(charY) or round(enemyY)+2==round(charY)):
        if EnemyAlive==True:
            centerX=random.randint(-10, 10)
            hurt=True
            cooldown=0
            health=health-1
    if EnemyAlive==False:
        if physicsExecute==1:
            ressurect=ressurect+1
            if ressurect>=150:
                EnemyAlive=True
                Enemyoffset=0


    # Character Damage Check
    if (charX > oceanX and charY<5) or (charX < oceanX2 and charY<5):
            centerX=random.randint(-10, 10)
            hurt=True
            cooldown=0
            health=health-1
    if (meteorX+2 >=charX >= meteorX-2) and (meteorY+2 >=charY >= meteorY-2):
            centerX=random.randint(-10, 10)
            hurt=True
            cooldown=0
            health=health-1
    
    # Cheat
    if keyboard.is_pressed('k'):
        EnemyAlive=False
        ressurect=0

    # Character Render
    update_render(round(charX), round(charY), [1,1,1])

    # Metor Motion
    if physicsExecute==1:
        if night==True:
            meteorY=meteorY-0.8
            if meteorY<=0:
                meteorY=40
                RealmeteorX=random.randint(-60, 60)
        else:
            meteorY=50
    
    if health>=1:
        update_render(3, displayY-5, [255,0,0])
        update_render(4, displayY-5, [255,0,0])
        update_render(5, displayY-5, [255,0,0])
        update_render(3, displayY-4, [255,0,0])
        update_render(5, displayY-4, [255,0,0])
        update_render(4, displayY-6, [255,0,0])
    if health>=2:
        update_render(3+5, displayY-5, [255,0,0])
        update_render(4+5, displayY-5, [255,0,0])
        update_render(5+5, displayY-5, [255,0,0])
        update_render(3+5, displayY-4, [255,0,0])
        update_render(5+5, displayY-4, [255,0,0])
        update_render(4+5, displayY-6, [255,0,0])
    if health>=3:
        update_render(3+10, displayY-5, [255,0,0])
        update_render(4+10, displayY-5, [255,0,0])
        update_render(5+10, displayY-5, [255,0,0])
        update_render(3+10, displayY-4, [255,0,0])
        update_render(5+10, displayY-4, [255,0,0])
        update_render(4+10, displayY-6, [255,0,0])
    
    # Generates Border
    j=0
    for i in display:
        x,y=reverse_render(j)
        if y==0 or y==displayY-1 or x==0 or x==displayX-1:
            if hurt==True:
                pixel=[255,0,0]
            else:
                pixel=[65,65,65]
            update_render(x,y,pixel)
        j=j+1
    if physicsExecute==1:
        m=m+1
    if m>=10:
        hurt=False
        m=0
    Physics_Tick()
    Render_Frame()
    calculateFPS()
    calculatePFPS()

    # Damage Frame Freeze
    if hurt==True and cooldown==0:
        #time.sleep(0.1)
        cooldown=1
    if health==0:
        gameOn=False
        j=0
        for i in display:
            x,y=reverse_render(j)
            j=j+1
            update_render(x,y,[255,0,0])
        frameExecute=1
        Render_Frame()



