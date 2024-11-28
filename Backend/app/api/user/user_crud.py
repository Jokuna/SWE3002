import os
import random 
from datetime import datetime
import smtplib  # SMTP 사용을 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈

def create_passkey() -> str:
    """ 6자리 임의의 인증번호를 생성

    Returns:
        str: 임의로 생성된 6자리 인증번호
    """
    random_number = str(random.randint(0, 999999))
    
    if len(random_number) < 6:
        random_number = random_number.zfill(6)
    
    return random_number # 6자리 랜덤 인증번호

def send_passkey_email(to_email: str, passkey: str) -> datetime:
    """ 주어진 이메일 주소로 인증번호 발송하기
    
    Args:
        to_email (str): 인증번호를 받을 이메일 주소
        passkey (str): 발송할 6자리 인증번호
    
    Returns:
        datetime: 인증번호가 발송된 시간
    """
    
    # smpt 서버와 연결
    gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
    gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
    
    # 로그인
    from_email = os.getenv("FROM_EMAIL")
    from_email_password = os.getenv("FROM_EMAIL_PASSWORD")
    smtp.login(from_email, from_email_password)
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = f"Dormie 인증번호"  # 메일 제목
    msg["From"] = from_email
    msg["To"] = to_email
    
    # 메일 본문 내용
    content = f"""안녕하세요.\n\n
    Dormie Web Service입니다.\n\n
    인증번호는 다음과 같습니다.\n\n
    {passkey}
    """
    
    content_part = MIMEText(content, "plain")
    msg.attach(content_part)
    
    smtp.sendmail(from_email, to_email, msg.as_string())

    return datetime.now()