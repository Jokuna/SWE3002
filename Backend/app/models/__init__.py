from app.models.chatrooms import ChatRoom
from app.models.chats import Chat
from app.models.messages import Messages
from app.models.userinfo import UserInfo
from app.models.users import User
from app.models.usersettings import UserSettings

# Beanie에서 사용할 Model 리스트
__all__ = ["ChatRoom", "Chat", "Messages", "UserInfo", "User", "UserSettings"]
models = [ChatRoom, Chat, Messages, UserInfo, User, UserSettings]