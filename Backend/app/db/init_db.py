import random
from beanie import init_beanie
from bson import ObjectId

from app.db.session import db
from app.models import *

async def init_db():
    # 테이블 생성
    await init_beanie(
        database=db,
        document_models=[
            ChatRoom,
            Chat,
            Messages,
            UserInfo,
            User,
            UserSettings,
        ]
    )

def generate_random_nickname():
    명사목록 = [
        # 자연 관련 명사
        '바다', '하늘', '나무', '꽃', '돌', '산', '강', '구름', '별', '달', '햇빛', '숲', '바람', '새', '호수', '노을', '풀', '샘', '파도', '봄', '여름', '가을', '겨울',

        # 감정 및 추상 명사
        '사랑', '꿈', '희망', '행복', '기쁨', '빛', '열정', '평화', '고요', '위로', '설렘', '온기',

        # 동물 관련 명사
        '고양이', '강아지', '호랑이', '사자', '곰', '여우', '펭귄', '토끼', '독수리', '공룡', '다람쥐', '새우',

        # 음식 및 사물 명사
        '사과', '딸기', '복숭아', '포도', '바나나', '초코', '우유', '커피', '떡', '빵', '달걀', '밥', '국', '책', '노트', '연필', '가방', '별빛', '시계',

        # 기타
        '추억', '행운', '이야기', '마음', '여행', '길', '달빛', '해변', '바위', '향기', '낮', '밤'
    ]

    def random_pick(arr):
        return random.choice(arr)

    nickname = ''
    while len(nickname) < 6:
        단어 = random_pick(명사목록)
        if len(nickname) + len(단어) <= 6:
            nickname += 단어

    return nickname

async def init_example(): # 더미 데이터 삽입
    # User, UserInfo 2명 추가 

    users = [
        {
            "uid": f"uid_{user['other_userId']}",
            "email": f"user{user['other_userId']}@skku.edu",
            "passkey": "000000",
            "username": f"{generate_random_nickname()}",
            "similarity": f"{user['similarity']}"
        }
        for user in [
            {"other_userId": 265, "similarity": 72},
            {"other_userId": 171, "similarity": 67},
            {"other_userId": 1, "similarity": 61},
            {"other_userId": 283, "similarity": 57},
            {"other_userId": 180, "similarity": 56},
            {"other_userId": 406, "similarity": 55},
            {"other_userId": 327, "similarity": 53},
            {"other_userId": 368, "similarity": 53},
            {"other_userId": 85, "similarity": 52},
            {"other_userId": 313, "similarity": 51},
        ]
    ]

    user_info_data = [
        {
            "isMale": user_data["isMale"],
            "dormitory": user_data["dormitory"],
            "latestGPA": user_data["latestGPA"],
            "isSmoke": user_data["isSmoke"],
            "sleepingTime": user_data["sleepingTime"],
            "wakeTime": user_data["wakeTime"],
            "age": user_data["age"],
            "semester": user_data["semester"],
            "major": user_data["major"],
            "selfIntroduction": user_data["selfIntroduction"],
            "trait": user_data["trait"],
        }
        for user_data in [
            {"isMale": True, "dormitory": 0, "latestGPA": 2.93, "isSmoke": False, "sleepingTime": "22:00", "wakeTime": "6:00", "age": 19, "semester": 1, "major": "Physics", "selfIntroduction": "Physics helps me satisfy my curiosity about how the world works.", "trait": ["Sociable", "Persuasive", "Humorous"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 2.93, "isSmoke": False, "sleepingTime": "22:00", "wakeTime": "6:00", "age": 20, "semester": 4, "major": "Physics", "selfIntroduction": "Exploring the mysteries of nature excites me.", "trait": ["Humorous", "Persuasive", "Sociable"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 2.93, "isSmoke": False, "sleepingTime": "22:00", "wakeTime": "6:00", "age": 18, "semester": 1, "major": "Physics", "selfIntroduction": "I love solving complex physics problems.", "trait": ["Sociable", "Adaptable", "Persistent"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 4.25, "isSmoke": False, "sleepingTime": "1:00", "wakeTime": "8:00", "age": 20, "semester": 2, "major": "Mechanical Engineering", "selfIntroduction": "Engineering innovative solutions excites me.", "trait": ["Introverted", "Sincere", "Meticulous"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 4.31, "isSmoke": False, "sleepingTime": "23:00", "wakeTime": "7:00", "age": 23, "semester": 5, "major": "Physics", "selfIntroduction": "I love understanding the fundamental laws of the universe.", "trait": ["Open-minded", "Witty", "Inventive"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 2.93, "isSmoke": False, "sleepingTime": "22:00", "wakeTime": "6:00", "age": 20, "semester": 2, "major": "Physics", "selfIntroduction": "Physics helps me satisfy my curiosity about how the world works.", "trait": ["Gentle", "Introverted", "Meticulous"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 4.31, "isSmoke": False, "sleepingTime": "23:00", "wakeTime": "7:00", "age": 20, "semester": 4, "major": "Physics", "selfIntroduction": "Physics helps me satisfy my curiosity about how the world works.", "trait": ["Challenging", "Decisive", "Positive"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 3.23, "isSmoke": False, "sleepingTime": "0:00", "wakeTime": "9:00", "age": 19, "semester": 2, "major": "Mathematics", "selfIntroduction": "I love uncovering patterns in numbers and data.", "trait": ["Challenging", "Decisive", "Independent"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 3.23, "isSmoke": False, "sleepingTime": "0:00", "wakeTime": "9:00", "age": 24, "semester": 7, "major": "Mathematics", "selfIntroduction": "I love uncovering patterns in numbers and data.", "trait": ["Decisive", "Independent", "Challenging"]},
            {"isMale": True, "dormitory": 0, "latestGPA": 4.25, "isSmoke": False, "sleepingTime": "1:00", "wakeTime": "8:00", "age": 21, "semester": 3, "major": "Mechanical Engineering", "selfIntroduction": "Designing machines that improve lives is my goal.", "trait": ["Decisive", "Positive", "Challenging"]},
        ]
    ]

    for user, info in zip(users, user_info_data):
        print(user, info)
        print(user["uid"]) 

        new_user = User(
            uid=user["uid"],
            email=user["email"],
            passkey=user["passkey"],
            username=user["username"],
            similarity=user["similarity"]
        )
        await new_user.insert()

        user_info = UserInfo(
            isMale=info["isMale"],
            dormitory=info["dormitory"],
            latestGPA=info["latestGPA"],
            isSmoke=info["isSmoke"],
            sleepingTime=info["sleepingTime"],
            wakeTime=info["wakeTime"],
            age=info["age"],
            semester=info["semester"],
            major=info["major"],
            selfIntroduction=info["selfIntroduction"],
            userId=new_user.id  # MongoDB의 User ID
        )
        await user_info.insert()

    # 더미용
    new_user = User(
        # id=1,
        uid="abc123",
        email="test@skku.edu",
        passkey="123456789",
        username="test_user",
        similarity=None
    )
    await new_user.insert()  # MongoDB에 저장

    user_info = UserInfo(
        isMale=True, 
        dormitory=101, 
        latestGPA=3.8, 
        isSmoke=False, 
        sleepingTime="23:00", 
        wakeTime="07:00", 
        age=20, 
        semester=3, 
        major="Computer Science", 
        selfIntroduction="Hi, I love programming!",
        userId=ObjectId(new_user.id)
    )
    await user_info.insert()

    new_user2 = User(
        # id=1,
        uid="xyz123",
        email="test@g.skku.edu",
        passkey="123456789",
        username="test_user",
        similarity=None
    )
    await new_user2.insert()  # MongoDB에 저장

    user_info2 = UserInfo(
        isMale=True, 
        dormitory=101, 
        latestGPA=3.8, 
        isSmoke=False, 
        sleepingTime="23:00", 
        wakeTime="07:00", 
        age=20, 
        semester=3, 
        major="Computer Science", 
        selfIntroduction="Hi, I Hate programming!",
        userId=ObjectId(new_user2.id)
    )
    await user_info2.insert()

    # UserSettings 데이터 삽입
    user_settings = UserSettings(
        is_open_age=True, 
        is_open_major=False, 
        is_basic_info_entered=True,
        userId=ObjectId(new_user.id)
    )
    await user_settings.insert()

    # ChatRoom 데이터 삽입
    chatroom = ChatRoom() # ChatRoom(id=1, name="General")
    await chatroom.insert()

    # Chat 데이터 삽입
    chat = Chat(userId1=str(new_user.id), userId2=str(new_user2.id), chatRoomId=str(chatroom.id))
    await chat.insert()

    # Messages 데이터 삽입
    message = Messages(writerId=new_user.id, text="Hello!", chatId=str(chat.id))
    await message.insert()

    # Messages 데이터 삽입
    message2 = Messages(writerId=new_user.id, text="Hello!2", chatId=str(chat.id))
    await message2.insert()

    # Messages 데이터 삽입
    message3 = Messages(writerId=new_user.id, text="Hello!3", chatId=str(chat.id))
    await message3.insert()

