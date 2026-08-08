import cv2
import numpy as np
import time
import handTrackingModule as htm
import pyautogui
import warnings


warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="google.protobuf.symbol_database"
)


# -----------------------------
# Camera Configuration
# -----------------------------

wCam, hCam = 1080, 720

frameR = 200
smoothening = 8


# -----------------------------
# Camera Initialization
# -----------------------------

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)


# -----------------------------
# Mouse Configuration
# -----------------------------

pTime = 0

plocX, plocY = 0, 0
clocX, clocY = 0, 0


# -----------------------------
# Hand Detector
# -----------------------------

detector = htm.handDetector(
    maxHands=1
)


# Screen resolution

wScr, hScr = pyautogui.size()

print(
    f"Screen Resolution: {wScr} x {hScr}"
)


# -----------------------------
# UI Configuration
# -----------------------------

font = cv2.FONT_HERSHEY_SIMPLEX

fontScale = 1

run_button_x = 200
run_button_y = 70
run_button_width = 350
run_button_height = 100

stop_button_x = 600
stop_button_y = 70
stop_button_width = 150
stop_button_height = 100

button_color = (255, 0, 0)
text_color = (255, 255, 255)


# -----------------------------
# Main Loop
# -----------------------------

while True:

    success, img = cap.read()

    if not success:
        print("Unable to access webcam.")
        break


    # Flip webcam horizontally

    img = cv2.flip(
        img,
        1
    )


    # Hand detection

    img = detector.findHands(
        img
    )

    lmList, bbox = detector.findPosition(
        img
    )


    # Interaction frame

    cv2.rectangle(
        img,
        (frameR, frameR),
        (wCam - frameR, hCam - frameR),
        (255, 0, 255),
        2
    )


    # ---------------------------------
    # Stop Button Detection
    # ---------------------------------

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        cx, cy = 0, 0

        if (
            abs(x1 - x2) < 40
            and
            abs(y1 - y2) < 40
        ):

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2


        length, img, lineInfo = detector.findDistance(
            8,
            12,
            img
        )


        if (
            stop_button_x
            <
            cx
            <
            stop_button_x + stop_button_width
            and
            stop_button_y
            <
            cy
            <
            stop_button_y + stop_button_height
        ):

            print(
                "Closing Virtual Mouse ..."
            )

            break


    # ---------------------------------
    # Gesture Processing
    # ---------------------------------

    if len(lmList) != 0:

        x0, y0 = lmList[4][1:]
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        x3, y3 = lmList[16][1:]
        x4, y4 = lmList[20][1:]


        fingers = detector.fingersUp()


        if len(fingers) == 5:

            # ---------------------------------
            # Volume Up
            # ---------------------------------

            if fingers == [0, 1, 1, 1, 1]:

                pyautogui.press(
                    "volumeup"
                )

                cv2.circle(
                    img,
                    (x1, y1),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.circle(
                    img,
                    (x2, y2),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.circle(
                    img,
                    (x3, y3),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.putText(
                    img,
                    "Volume Up",
                    (500, 55),
                    font,
                    fontScale,
                    (255, 0, 0),
                    3,
                    cv2.LINE_AA
                )

                print(
                    "Volume Increase"
                )


            # ---------------------------------
            # Volume Down
            # ---------------------------------

            elif fingers == [0, 0, 0, 0, 0]:

                pyautogui.press(
                    "volumedown"
                )

                cv2.circle(
                    img,
                    (x1, y1),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.circle(
                    img,
                    (x2, y2),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.circle(
                    img,
                    (x3, y3),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.circle(
                    img,
                    (x4, y4),
                    15,
                    (255, 255, 255),
                    cv2.FILLED
                )

                cv2.putText(
                    img,
                    "Volume Down",
                    (500, 55),
                    font,
                    fontScale,
                    (255, 0, 0),
                    3,
                    cv2.LINE_AA
                )

                print(
                    "Volume Decrease"
                )


            # ---------------------------------
            # Cursor Movement
            # ---------------------------------

            elif (
                fingers[0] == 1
                and
                fingers[1] == 1
                and
                fingers[2] == 1
                and
                fingers[3] == 0
                and
                fingers[4] == 0
            ):

                x3 = np.interp(
                    x1,
                    (
                        frameR,
                        wCam - frameR
                    ),
                    (
                        0,
                        wScr
                    )
                )

                y3 = np.interp(
                    y1,
                    (
                        frameR,
                        hCam - frameR
                    ),
                    (
                        0,
                        hScr
                    )
                )


                clocX = (
                    plocX
                    +
                    (
                        x3 - plocX
                    )
                    /
                    smoothening
                )

                clocY = (
                    plocY
                    +
                    (
                        y3 - plocY
                    )
                    /
                    smoothening
                )


                pyautogui.moveTo(
                    clocX,
                    clocY
                )


                cv2.circle(
                    img,
                    (x1, y1),
                    15,
                    (255, 0, 255),
                    cv2.FILLED
                )


                cv2.putText(
                    img,
                    "Moving Mouse",
                    (460, 55),
                    font,
                    fontScale,
                    (255, 0, 0),
                    3,
                    cv2.LINE_AA
                )


                plocX = clocX
                plocY = clocY


                print(
                    "Cursor Movement"
                )


            # ---------------------------------
            # Left Click
            # ---------------------------------

            elif (
                fingers[1] == 1
                and
                fingers[2] == 1
            ):

                length, img, lineInfo = detector.findDistance(
                    8,
                    12,
                    img
                )


                if length < 40:

                    cv2.circle(
                        img,
                        (
                            lineInfo[4],
                            lineInfo[5]
                        ),
                        15,
                        (0, 255, 0),
                        cv2.FILLED
                    )


                    cv2.putText(
                        img,
                        "Left Click",
                        (500, 55),
                        font,
                        fontScale,
                        (255, 0, 0),
                        3,
                        cv2.LINE_AA
                    )


                    pyautogui.click()


                    print(
                        "Left Click"
                    )


            # ---------------------------------
            # Right Click
            # ---------------------------------

            elif (
                fingers[0] == 0
                and
                fingers[1] == 0
                and
                fingers[2] == 1
                and
                fingers[3] == 1
                and
                fingers[4] == 1
            ):

                length, img, lineInfo = detector.findDistance(
                    4,
                    8,
                    img
                )


                if length < 40:

                    cv2.putText(
                        img,
                        "Right Click",
                        (500, 55),
                        font,
                        fontScale,
                        (255, 0, 0),
                        3,
                        cv2.LINE_AA
                    )


                    pyautogui.rightClick()


                    print(
                        "Right Click"
                    )


    # ---------------------------------
    # FPS
    # ---------------------------------

    cTime = time.time()

    if cTime != pTime:

        fps = 1 / (cTime - pTime)

    else:

        fps = 0


    pTime = cTime


    cv2.putText(
        img,
        str(int(fps)),
        (20, 50),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255, 0, 0),
        3
    )


    # Display

    cv2.imshow(
        "Virtual Mouse",
        img
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ---------------------------------
# Cleanup
# ---------------------------------

cap.release()

cv2.destroyAllWindows()
