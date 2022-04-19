import pyautogui
correct_pass = "IdoNotKnow"

password = pyautogui.password(text='Hmm what could it be?', title='Enter Password', default='', mask='*')
print(password)

 