# GoogleTexttoSpeech

1. 필요한 라이브러리들 설치
* pip install gTTS
* pip install speechrecognition
* pip install playsound

2. 실행
* python gtts_test.py

3. 참고

* filename이 같을 경우 음성 파일이 덮여쓰여저서 저장됨.
단순히 음성 출력만 할 경우 지장없음. 프로젝트에 있는 gttsMP3, gttsWAV는 테스트용으로 만들어놓음. text를 수정해서 실행하면 파일이름은 같지만 음성은 달라짐. 
* 영어는 여자 성우, 한글은 남자 성우 (변경 불가능)
* 'en'으로 지정했을 때 한글이 text에 포함되어 있으면 이를 무시하지만, 
'ko'일때 text내의 영문은 무시되지 않고 음성합성을 수행



