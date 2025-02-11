import serial, time, argparse, sys, traceback
import logging_c, stuff
import cv2

parser = argparse.ArgumentParser(prog="PROJECT Hindsight - All can be done with focus", description="Reap the seeds you sow", epilog="Use wisely")

parser.add_argument("-l", "--logLevel", help="see log level")
parser.add_argument("-ty", '--type', help="Type of display")
args = parser.parse_args()

#------- SIG
def cleanUp(type, value, tb):
    traceback_details = "\n".join(traceback.extract_tb(tb).format())
    msg = f"\ncaller: {' '.join(sys.argv)}\n{type}: {value}\n{traceback_details}"
    
    logging_c.log.critical(msg)
    
    capturedVideo.release()
    cv2.destroyAllWindows()

    logging_c.log.info("No words more can be said to such a looser")
    sys.exit()


sys.excepthook = cleanUp
#-------- END
logging_c.setDebugLevel("vv")
logging_c.log.info("And so it begins")

processType = None
if args.type:
    processType = args.type

else:
    processType = input("Process type: ")


capturedVideo = cv2.VideoCapture("./img/oi.mp4")
count = 0
while capturedVideo.isOpened():
    data, readFr = capturedVideo.read()
    
    readFr = cv2.resize(readFr, (540, 380), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
    cv2.putText(readFr, f'THIS IS COUNT: {count}', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    
    if data:
        cv2.imshow("Orginal", readFr)

        if processType in ['tr', 'all']:
            gray = cv2.cvtColor(readFr, cv2.COLOR_BGR2GRAY)
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            cv2.imshow('thresh', thresh)

        elif processType in ['sm', 'all']:
            gaussianblur = cv2.GaussianBlur(readFr, (5, 5), 0)
            cv2.imshow('blurr', gaussianblur)

        elif processType in ['ed', 'all']:
            edgeDetect = cv2.Canny(readFr, 100, 200)
            cv2.imshow('edgeDetect', edgeDetect)

    
        count += 1
        if (cv2.waitKey(25) & 0xFF) == ord('q'):
            break

else:
    logging_c.log.debug("captured vid is not opened")

# logging_c.log.debug(f"hitting the cv2")
# key = cv2.waitKey(1000)

# logging_c.log.debug(f"Key is: {key}")
cleanUp("Times End", "FINITO", None)