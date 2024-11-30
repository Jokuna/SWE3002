import openai
import json
import os
import time

# OpenAI API 키 설정
openai.api_key = "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"

# 파일 이름 변경 함수
def get_unique_filename(file_path):
    base, ext = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{base}_{counter}{ext}"
        counter += 1
    return file_path

# 데이터 로드 함수
def load_user_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# 데이터 추가 저장 함수
def append_user_data(file_path, user):
    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(user)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error appending data to file: {e}")

# 임베딩 함수
def get_embedding(text):
    try:
        response = openai.Embedding.create(
            model="text-embedding-3-small",
            input=text
        )
        embedding = response['data'][0]['embedding']
        if isinstance(embedding, list):  # 임베딩 결과가 리스트인지 확인
            return embedding
        else:
            print(f"Unexpected embedding format: {embedding}")
            return []
    except Exception as e:
        print(f"Embedding error: {e}")
        return []

# 데이터 처리 함수
def process_user_data(user_data, processed_file, compressed_file):
    for user in user_data:
        print(f"Processing user {user['userId']}...")
        try:
            # Embedding 생성
            if user.get('trait'):
                user['embedding'] = get_embedding(", ".join(user['trait']))
                time.sleep(1)
            else:
                user['embedding'] = []

            # 처리된 데이터 저장
            append_user_data(processed_file, user)

            # Compressed 데이터 생성
            compressed_user = user.copy()
            if isinstance(compressed_user.get("embedding"), list):
                compressed_user['embedding'] = compressed_user["embedding"][:3]  # 첫 3개의 값만 가져옴
            else:
                compressed_user['embedding'] = []
            append_user_data(compressed_file, compressed_user)

        except Exception as e:
            print(f"Error processing user {user['userId']}: {e}")

# 메인 함수
def main():
    input_file = "userdb/userdb.json"
    processed_file = get_unique_filename("userdb/userdb_processed.json")
    compressed_file = get_unique_filename("userdb/userdb_compressed.json")

    # JSON 파일 초기화
    with open(processed_file, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

    with open(compressed_file, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False, indent=4)

    # JSON 파일 읽기
    user_data = load_user_data(input_file)
    
    # 임베딩 처리
    process_user_data(user_data, processed_file, compressed_file)

    print(f"Processed data saved to {processed_file}")
    print(f"Compressed data saved to {compressed_file}")

# 실행
if __name__ == "__main__":
    main()
