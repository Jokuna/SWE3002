import json
from scipy.spatial.distance import cosine

def load_processed_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_and_sort_similarities_for_target_user(processed_file, output_file, target_userId):
    # JSON 데이터 로드
    data = load_processed_data(processed_file)

    # 첫 번째 유저의 userId가 target_userId와 같은지 확인
    if data[0]['userId'] != target_userId:
        raise ValueError(f"첫 번째 유저의 userId({data[0]['userId']})가 target_userId({target_userId})와 일치하지 않습니다.")

    # 유저별 임베딩 추출
    embeddings = {user['userId']: user['embedding'] for user in data if 'embedding' in user and len(user['embedding']) > 0}

    # 타겟 유저의 임베딩 가져오기
    if target_userId not in embeddings:
        raise ValueError(f"Target userId '{target_userId}' not found in the data.")

    # 타겟 유저의 trait 가져오기
    target_trait = []
    for user in data:
        if user["userId"] == target_userId:
            target_trait = user["trait"]
            break
    print(f"Trait of target: {target_trait}")

    target_embedding = embeddings[target_userId]

    # 유사도 결과 저장용 리스트
    similarities = []

    # 다른 유저들과의 유사도 계산
    for other_userId, other_embedding in embeddings.items():
        if target_userId == other_userId:
            continue  # 자기 자신 제외

        # 코사인 유사도 계산
        similarity = 1 - cosine(target_embedding, other_embedding)
        similarities.append({
            "other_userId": other_userId,
            "similarity": similarity
        })

    # 유사도 높은 순서대로 정렬
    similarities = sorted(similarities, key=lambda x: x['similarity'], reverse=True)

    # 결과 저장
    result = {
        "userId": target_userId,
        "similarities": similarities
    }

    # JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Sorted similarities for user '{target_userId}' saved to {output_file}")

# 실행
processed_file = "userdb/userdb_filtered.json"
output_file = "userdb/sorted_similarities_for_target_user.json"
target_userId = 255  # 실제 타겟 유저 ID로 변경

calculate_and_sort_similarities_for_target_user(processed_file, output_file, target_userId)
