import time
import pyautogui

def open_spotify():
    # Użyj kombinacji klawiszy Win + S, aby otworzyć wyszukiwarkę systemową
    pyautogui.hotkey('win', 's')
    time.sleep(1)  # Poczekaj 1 sekundę na otwarcie wyszukiwarki

    # Wpisz "Spotify" i naciśnij Enter
    pyautogui.write("Spotify")
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(5)  # Poczekaj 5 sekund na otwarcie Spotify

def play_playlist(playlist_name):
    # Wyszukaj playlistę
    pyautogui.hotkey('ctrl', 'l')  # Otwórz okno wyszukiwania w Spotify
    time.sleep(1)

    pyautogui.write(playlist_name)  # Wpisz nazwę playlisty
    time.sleep(2)
    pyautogui.press('enter')  # Naciśnij Enter, aby wyszukać playlistę
    time.sleep(2)

    # Wybierz pierwszy wynik (załóżmy, że to playlista)
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Poczekaj 5 sekund na załadowanie playlisty
    time.sleep(5)

    # Kliknij przycisk odtwarzania (play)
    play_button_position = (2276 , 325)  # Wpisz współrzędne przycisku odtwarzania
    pyautogui.click(play_button_position)

if __name__ == "__main__":
    playlist_name = input("Podaj nazwę playlisty: ")
    open_spotify()
    play_playlist(playlist_name)
