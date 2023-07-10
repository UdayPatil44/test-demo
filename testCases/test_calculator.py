import time
import pyautogui as pag
from pywinauto import Desktop
import logging
from Utilities.customLogger import logGen



# Sleep Durations
SEARCH_DELAY = 0.5
CALCULATION_DELAY = 1


def test_calculator_multiplication():
    logger = logGen.loggen()

    # Pressing the Window's icon
    pag.press("winleft", _pause=True)
    time.sleep(SEARCH_DELAY)
    # Typing calaculator
    pag.typewrite("calculator", interval=0.2)
    time.sleep(SEARCH_DELAY)
    # Open calculator
    pag.press("enter")
    time.sleep(SEARCH_DELAY)
    logger.info("We are Opening the calculator")

    # From here actual calculation starts

    pag.press("9")
    time.sleep(SEARCH_DELAY)
    pag.press("*")
    time.sleep(SEARCH_DELAY)
    pag.press("9")
    time.sleep(SEARCH_DELAY)
    pag.press("9")
    time.sleep(SEARCH_DELAY)
    pag.press("enter")
    time.sleep(CALCULATION_DELAY)

    dlg = Desktop(backend="uia").Calculator
    dlg.type_keys('9*99=')

    result = (dlg.static3.window_text())
    num = ""
    for c in result:
        if c.isdigit():
            num = num + c
    expected_result = 9 * 99

    assert int(num) == expected_result, f"Expected result: {expected_result}, Actual result: {num}"
    logging.info("Result of 9 x 99 = " + num)

    # For closing the calculator app
    calculator_title = "Calculator"
    calculator_window = pag.getWindowsWithTitle(calculator_title)[0]
    calculator_window.close()
