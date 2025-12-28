import pyautogui
import cv2
import numpy as np

# Output video settings
resolution = (1920, 1080)
filename = "output.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    # Capture screenshot
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert color
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write frame to output file
    out.write(frame)

    # Show live window
    cv2.imshow("Live", frame)

    # Break loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
out.release()
cv2.destroyAllWindows()