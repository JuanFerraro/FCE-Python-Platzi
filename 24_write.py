with open('./23_text.txt', 'r+') as file: # Cuando se hace el opne solo se tiene permisos de lectura
    for line in file:
        print(line)
    file.write('\nNueva linea en archivo\n') # \n para new line
    file.write('Nueva linea en \n') # \n para new line
    file.write('Nueva linea\n') # \n para new line
