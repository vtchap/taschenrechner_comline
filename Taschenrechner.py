# Modul Toolkit interface importieren
import tkinter       
                                                    

# Neues Fenster mit seinen Eigenschaften anlegen
window = tkinter.Tk()
window.geometry('200x270')
window.title('Taschenrechner')


# Leere Liste zum Sammeln von Elementen für Userinterface
gui_items = list()


#Buttons, die gebraucht werden, in einer Liste schreiben
button_values = ['(',')', '<--', 'C', '7', '8', '9', '/', '4', '5',
                 '6', '*', '1', '2', '3', '-', '0', ',', '=', '+']

#Zeichenkette für die Rechnungen, die aus den Buttons besteht
calculation = str()


#Funktion, die den Wert des Buttons an die Zeichenkette weitergibt
def add_button_text_to_calculation(value):
    global calculation

    # C löscht die Rechnungen
    if value == 'C':
        calculation = str()
        output_label['text'] = ''
        return

    # = berechnet die Zeichenkette 
    if value == '=':
        calculate(calculation)
        calculation = str()
        return

    calculation = calculation + value
    output_label['text'] = calculation


# Funktion, die aus der Zeichenkette eine Berechnung macht und das Ergebnis berechnet
def calculate(calc):
    try:
        result = eval(calc)             #Die "eval"-Funktion macht, dass Python die Zeichen aus der Zeichenkette wie Pythonbefehle behandelt
        print(result)
        output_label['text'] = result

    #Wenn eine nicht-richtige Berechnung getippt wird, wird es als Fehler (Error) angezeigt
    except Exception as e:
        print(e)
        output_label['text'] = 'Error'




# Funktion, die aus jedem der Elemente in unserer Liste einen Button erstellt und diesen Button in die Liste unserer GUI-Items ablegt.
def create_button(value):
    button = tkinter.Button(text=value, command=lambda: add_button_text_to_calculation(value))
    gui_items.append(button)


for val in button_values:
    create_button(val)


#Anzeige, wo das Ergebnis der Rechnungen angezeigt werden 
output_label = tkinter.Label(text='23*(57+18)')
output_label.grid(row=0, columnspan=10)

# Alle Schaltflächen werden automatisch in einem Raster mit 4 Spalten und so viele Reihen wie möglich platziert
column_count = 0
row_count = 1
maximum_columns = 4

# Python geht jetzt durch die Liste der GUI-Elemente und richtet die Elemente im Gitter aus
for item in gui_items:
    item.grid(row=row_count, column=column_count)

#Wenn Python in der 4. Palten ist, dann in der nächsten Zeile springen
    column_count += 1
    if column_count == maximum_columns:
        column_count = 0
        row_count += 1


if __name__ == '__main__':
    window.mainloop()