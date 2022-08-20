블루스택에서 실행한 
틀린그림 찾기(아이콘에 쇼파 2개 나오는)
자동화

가상환경 구축
PS C:\git\PythonProject> python -m venv myenv
PS C:\git\PythonProject> .\myenv\Scripts\activate

라이브러리 설치
(myenv) PS C:\git\PythonProject> pip install Pillow
(myenv) PS C:\git\PythonProject> pip install opencv-python
(myenv) PS C:\git\PythonProject> pip install pyautogui
pip list

vscode 인터프리터는 가상환경의 파이썬 선택

블루스택으로 틀린 그림 찾기 실행
F11로 화면 최대화
vscode 밑에 조그맣게 띄우고 find_diff.py실행