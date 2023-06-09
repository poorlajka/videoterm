import sys
import cv2 as cv
import numpy as np
import math

ASCII_LUT = np.array([' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ',
                        ' ', ' ', ' ', ' ', ' ',
                        '@', '#', '%', ')', '-',
                        '@', '#', '%', ')', '-',
                        '@', '#', '%', ')', '-'])

def luminance_to_ascii(luminance: float) -> chr:
    lut_index = math.floor(luminance / 10)
    return ASCII_LUT[lut_index]

def get_pixel_luminance(pixel: np.array) -> float:
    b, g, r = pixel
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def pixel_to_ascii(pixel: np.array) -> chr:
    luminance = get_pixel_luminance(pixel)
    return luminance_to_ascii(luminance)

def main() -> None:
    argc = len(sys.argv) - 1


    match argc:
        case 0:
            print("hello")

    capture = cv.VideoCapture(0)

    if not capture.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            exit()
        
        resized_frame = cv.resize(frame, (90, 90))
        #ascii_frame = "".join([pixel_to_ascii(pixel) + " " for row in resized_frame for pixel in row])
        ascii_frame = ""
        for row in resized_frame:
            for pixel in row:
                ascii_frame += pixel_to_ascii(pixel) + "  "
            ascii_frame += "\n"
        print(ascii_frame)

if __name__ == "__main__":
    main()
