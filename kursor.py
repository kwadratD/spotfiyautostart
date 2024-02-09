import pyautogui

def print_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            print('X:', x, 'Y:', y)
            pyautogui.sleep(1)  # Aktualizuj co sekundę
    except KeyboardInterrupt:
        print('Zakończono monitorowanie pozycji kursora.')

print('Naciśnij Ctrl+C, aby zakończyć monitorowanie pozycji kursora.')
print_mouse_position()
