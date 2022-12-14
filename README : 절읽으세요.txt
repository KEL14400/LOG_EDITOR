
This tool reforms CCFOLIA log into a HTML codes that's easier to read in Tistory blog. It does not add character portrait.


<Procedures>
1. Copy and paste the replay you'll backup into a txt file. It assumes that it only contains texts from the main tab. Make sure the txt file and Log Editor are located in same folder.
2. Open CLI and execute Log Editor by typing "python LOG_EDITOR.py".
3. Skip an language option (anything other than "k" will display english) and enter the name of txt file (without .txt)
4. Log Editor will read the file and print out every character's name. If you wish to assign colour for that character's text, enter 6-digit colour code (without #). Pressing enter or any other input that's not 6-digit will automatically assign grey colour.
5. Log Editor will automatically terminate itself once the writing's completed. There will be a new file called "output_(original_name).txt' that contains HTML code for the replay. Copy and paste them into Tistory HTML page.

---

티스토리의 테이블(투명선) 기능을 써서 코코포리아 세션 로그를 읽기 편하게 편집해주는 툴입니다. 이미지는 추가해주지 않습니다.


<사용법>
1. 백업할 코코포리아 로그를 (메인탭 로그만 있다고 가정합니다) Ctrl+A 로 전체선택 → 복사해서 txt 파일을 만듭니다. 이 떄 해당 txt 파일이 로그 에디터와 같은 폴더에 있도록 합니다.
2. CLI(커맨드라인) 을 실행해서 python LOG_EDITOR.py 로 프로그램을 실행합니다.
3. 언어 옵션에 'k'를 입력해서 한글 설정으로 바꾼 뒤, 1번에 저장한 txt 파일의 제목을 입력합니다. 이 때 확장자(.txt)는 반드시 제외해주세요.
4. 프로그램이 txt 파일을 읽고 캐릭터 이름마다 컬러 코드를 지정하게 할겁니다. 글자색을 지정하고 싶은 캐릭터의 경우 #을 제외한 코드를 입력하고, 그럴 필요가 없는 경우는 엔터를 누르면 됩니다. 엔터로 스킵할 경우 자동으로 회색이 지정됩니다. (시스템 메세지의 경우엔 옅은 회색으로 이미 지정되어 있습니다) 딱 6자가 입력되지 않은 경우 역시 자동으로 회색이 지정됩니다.
5. 컬러 코드 지정이 끝나고 변환이 완료되면 프로그램이 자동으로 종료됩니다. 폴더에 생긴 'output_(오리지널파일이름).txt' 파일을 열어 Ctrl+A 로 전체선택 → 티스토리 글쓰기 창의 HTML 화면으로 복붙해주면 완성입니다.