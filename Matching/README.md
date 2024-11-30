0. 유사도를 계산하기 위해서 db에 필연적으로 embedding을 넣어야할 것 같습니다. 아니면 매번 유사도를 계산할 때마다 api를 호출하는 방법도 있긴 합니다.
1. userdb.json에는 500명의 임시 데이터가 들어있습니다. 성격은 trait 변수에 들어있습니다.
2. 실행 순서는 embedding - filtering - matching 입니다
3. userdb 폴더에는 userdb.json 파일만 들어있고, 실행 결과는 result_example 폴더에 들어있습니다. 직접 실행해보셔도 되고 example만 확인하셔도 됩니다.

* embedding
userdb에서 성격 유사도를 계산하기 위해 openai의 embedding api를 이용하여 trait을 embedding 합니다.
api는 제가 결제해서 팀플용으로 만든 계정의 api key를 사용했습니다. 아마 프로젝트를 5번 해도 credit은 다 못쓸겁니다.
결과 파일에는 embedding 변수가 추가되며, 해당 값은 1536개의 float으로 이루어져 있습니다.
userdb_processed.json은 각 유저에 대해 1536개의 embedding vector가 전부 들어가 있습니다.
userdb_compressed.json은 가독성을 위해 각 유저의 vector를 3개만 잘라내서 저장합니다.

* filtering
userdb_processed.json에서 자신과 맞는 조건의 유저들을 필터링합니다.
"자신"에 해당하는 target user의 id값(int)을 변수로 지정해야 합니다.(기본적으로 target_userId = 255로 코드 내에 작성되어 있습니다.)
성별, 기숙사, 흡연 여부는 반드시 일치해야 합니다.
수면 시간은 IoU@0.5 를 기준으로 하였습니다.
userdb_filtered.json파일에 본인을 포함해 필터링된 유저들의 data가 저장됩니다. target user는 json파일의 가장 위에 저장됩니다.

* 수면시간 계산 방식
IoU는 time interval의 교집합의 비율을 계산하기 위한 값으로, (수면시간의 교집합) / (수면시간의 합집합) 으로 계산됩니다.
IoU@0.5 라고 하면 IoU > 0.5 이상인 것만 포함한다는 의미입니다.
해당 값이 0.5 이상인 유저들만 필터링됩니다.
유저 수가 많을 때는 0.5로도 괜찮은데, 유저가 적을 때는 0.3으로 낮춰야 매칭되는 유저가 생길 수도 있습니다.
1. 23~7, 0~9 와 같이 24시 표기법에서 겹치는 시간대를 계산하기 위해서 circular list를 사용했습니다. 이를 위해 각 시간을 30분을 기준으로 반올림하여 int로 저장했습니다.
2. list는 24개의 node를 가지고 있으며, target user의 수면 시간에 해당하는 node들은 1의 값을, 나머지 시간에 해당하는 node는 0을 가지고 있습니다.
3. target user의 수면 시간대에 해당하는 node들과 나머지 user의 수면 시간대를 비교하여 일치하는 node의 개수가 교집합이 됩니다.

* matching
userdb_filtered.json에서 앞서 필터링의 기준이 되는 target user(json의 가장 상위 user)를 기준으로 다른 유저들과의 유사도를 계산합니다.
cross check를 위해 target_user_id값을 입력해서 해당 유저가 json의 가장 위에 있는지 확인하는 과정이 있습니다. 일치하지 않다면 error가 발생합니다.
embedding vector로 cosine similarity를 계산하여 유사도를 측정합니다.
sorted_similarities_for_target_user.json 파일은 target_user의 Id값과, 다른 유저들과의 유사도가 내림차순으로 정렬되어 저장되어 있습니다.




openai에서 성격을 종합해서 embedding하다보니 "외향적인" 같은 단어는 중요도롤 낮게 측정하는 경향이 있는 것 같긴 합니다.
대신 전공까지 성격과 통합해서 embedding 할 수도 있을 것 같습니다.