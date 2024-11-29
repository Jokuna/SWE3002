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

async def init_example(): # 더미 데이터 삽입
    # User, UserInfo 2명 추가 
    new_user = User(
        # id=1,
        uid="abc123",
        email="test@skku.edu",
        passkey="123456789",
        username="test_user"
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
        username="test_user"
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

