#convert.py
#IPO or program description

from graphics import *

def main():
    # create a window object
    win = GraphWin('Celsius Converter', 400, 300)

    # creat text objects
    celsiusTempString =    "Celsius Temerature:        "
    fahrenheitTempString = "Fahrenheit Temperature:    "

    # creat Text boxes
    Text(Point(150,50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheitTempString).draw(win)

    # create center box
    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    # create button text
    buttonText = Text(Point(200, 150), "Convert It")
    buttonText.draw(win)

    # create input and out fields
    inputCelsiusFied = Entry(Point(300, 50), 5)
    inputCelsiusFied.setText("0.0")
    inputCelsiusFied.draw(win)

    outputFahrenheitField = Text(Point(300,250), "")
    outputFahrenheitField.draw(win)

    win.getMouse()

    celsiusTemperature = float(inputCelsiusFied.getText())
    fahrenheit = 9.0/5.0 * celsiusTemperature + 32

    # display results
    outputFahrenheitField.setText(round(fahrenheit, 2))

    buttonText.setText('Quit')

    win.getMouse()

main()