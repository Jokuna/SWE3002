import json

class CircularLinkedList:
    def __init__(self, size=24):
        self.nodes = [0] * size  # 24개의 노드를 0으로 초기화
        self.size = size

    def mark_sleep_time(self, start_time, end_time):
        """수면 시간을 나타내는 노드 표시"""
        start_hour = self._time_to_nearest_hour(start_time)
        end_hour = self._time_to_nearest_hour(end_time)

        # 자정을 넘는 경우 수면 시간 처리
        current = start_hour
        while True:
            self.nodes[current] = 1  # 수면 시간 노드를 1로 표시
            if current == end_hour:
                break
            current = (current + 1) % self.size

    def calculate_intersection(self, other):
        """다른 CircularLinkedList와의 교집합 계산"""
        intersection_count = sum(
            1 for a, b in zip(self.nodes, other.nodes) if a == b == 1
        )
        return intersection_count

    @staticmethod
    def _time_to_nearest_hour(time_string):
        """'HH:MM' 형식의 시간을 가장 가까운 정수 시각으로 변환"""
        hours, minutes = map(int, time_string.split(":"))
        if minutes >= 30:
            hours = (hours + 1) % 24  # 23시 이후는 0시로 순환 처리
        return hours


def calculate_sleep_time_iou(target_user, other_user):
    # 대상 사용자와 비교 대상 사용자의 수면 시간을 Circular Linked List로 생성
    target_list = CircularLinkedList()
    other_list = CircularLinkedList()

    # 두 사용자의 수면 시간을 노드에 표시
    target_list.mark_sleep_time(target_user['sleepingTime'], target_user['wakeTime'])
    other_list.mark_sleep_time(other_user['sleepingTime'], other_user['wakeTime'])

    # 교집합 및 합집합 계산
    intersection = target_list.calculate_intersection(other_list)
    union = sum(target_list.nodes) + sum(other_list.nodes) - intersection

    return intersection / union if union > 0 else 0


def filter_users(target_user, users, iou_threshold=0.5):
    """성별, 기숙사, 흡연 여부, 수면 시간 IoU를 기준으로 사용자 필터링"""
    filtered_users = []
    for user in users:
        if user['userId'] == target_user['userId']:
            continue  # 대상 사용자 자신은 제외

        # 성별, 기숙사, 흡연 여부 확인
        if (
            user['isMale'] == target_user['isMale'] and
            user['dormitory'] == target_user['dormitory'] and
            user['isSmoke'] == target_user['isSmoke']
        ):
            # 수면 시간 IoU 계산
            iou = calculate_sleep_time_iou(target_user, user)
            if iou >= iou_threshold:
                filtered_users.append(user)

    return filtered_users


# 필터링된 사용자를 JSON 파일로 저장
def save_filtered_users(target_user, filtered_users, output_file_path):
    # 대상 사용자를 필터링된 사용자 목록의 맨 앞에 추가
    filtered_users_with_target = [target_user] + filtered_users

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(filtered_users_with_target, file, ensure_ascii=False, indent=4)
    print(f"필터링된 사용자 데이터가 {output_file_path}에 저장되었습니다.")


# 메인 함수 실행
def main():
    # JSON 파일 경로 설정
    input_file_path = "userdb/userdb_processed.json"
    output_file_path = "userdb/userdb_filtered.json"

    # 데이터 로드
    with open(input_file_path, 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    # 대상 사용자 지정 (예: userId = 255)
    target_userId = 255
    print(f"대상 사용자: user {target_userId}")
    target_user = next(user for user in user_data if user['userId'] == target_userId)

    # 조건에 따라 사용자 필터링
    filtered_users = filter_users(target_user, user_data)

    # 필터링된 사용자 저장 (대상 사용자를 맨 앞에 추가)
    save_filtered_users(target_user, filtered_users, output_file_path)


# 메인 함수 실행
if __name__ == "__main__":
    main()
