import logging_c
import subprocess

def createDictFromList(listIn=[]):
    createdDict = {**dict.fromkeys(listIn)}
    logging_c.vLog.debug(f"Dictionary Returned: {createdDict}")
    return createdDict

def returnResponse(inputCmd="true", respType="str"):
    output = subprocess.check_output(inputCmd, shell=True)
    logging_c.vLog.debug(f"CMD: {inputCmd} Output: {output}")
    response = output
    
    if respType == "str":
        response = output.decode(encoding="utf-8")

    return response

def intConverter(suspiciousVar):
    logging_c.vLog.info("Confirming variable is an int")
    try:
        confirmedInt = int(suspiciousVar)
        logging_c.vLog.debug(f"Confirmed int: {confirmedInt}")

    except ValueError:
        logging_c.vLog.warning("The variable passed in was not an Int")
        confirmedInt = None

    return confirmedInt
        
def ttyFinder(cmdResponse, lineType="tty"):
    sortedResponse = cmdResponse.split("\n")
    logging_c.vLog.debug(f"Recieved Data Sorted: {sortedResponse}")
    
    availableLines = []
    chosenLine = None

    for i in sortedResponse:
        if lineType in i:
            availableLines.append(i)

    logging_c.vLog.debug(f"Current Available Lines: {availableLines}")
    noAvailableLines = len(availableLines)

    if noAvailableLines < 1:
        logging_c.vLog.critical(f"USB not detected - imminent program death")
    
    elif noAvailableLines > 1:
        logging_c.vLog.info("Multiple tty lines detected, user must select appropriate line")
        for i in availableLines:
            answ = input(f"Confirm if the printed tty line is correct (y/n) > {i}:")
            
            if answ == "y":
                chosenLine = i
                break
    else:
        logging_c.vLog.info("Automagically selecting tty line")
        chosenLine = availableLines[0]

    if chosenLine is None:
        raise Exception("No Chosen/Available lines")
    
    return chosenLine