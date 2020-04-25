"""
정수 집합 클래스
1. int Set 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 self.vals를 attribute로 가진다.
2. 새로운 정수 e를 추가하는 insert 메쏘드. 해당 요소가 이미 있다면 추가하지 않음.
3. e가 정수집합에 포함되어 있는 지 확인하는 메쏘드인 involve 정의(True, False 반환)
4. e를 제거하는 remove 메소드
5. 단, e가 해당 집합에 없다면 적당한 오류 메시지를 출력
6. 집합 형식의 문자열로 변환시켜주는 __str__메쏘드. 단, 정수들은 정렬되어 반환되어야 한다.
"""
class IntSet:
    def __init__(self):
        """

        self.vals를 초기화
        """
        self.vals = [ ]

    def __str__(self):
        #정렬
        r = sorted(self.vals)
        return str(r)

    # def print(self):
    #     for i in range(0, len(self.vals)):


    def involve(self, e):
        """

        :param e: 요소를 검사
        :return: True or False 반환
        """

        if self.vals.count(e) >= 1:
            return True
        else:
            print("해당 요소 %s는 이 집합에 없습니다." % e)
            return False

    def insert(self, e):
        """

        :param e: 추가할 요소 e
        :return: retrun vals
        """
        if self.involve(e) == True:
            return self.vals
        # 요소가 없으면 추가
        else:

            print("해당 요소 %s를 추가합니다." % e)
            return self.vals.append(e)

    def remove(self, e):
        """

        :param e: 요소 e 제거
        :return:
        """
        if self.involve(e) == True:
            print("해당 요소 %s를 제거합니다." % e)
            return self.vals.remove(e)
        else:
            return self.vals


# L = [ 1,2,3,4,5 ]
s = IntSet()
s.insert(5)
s.insert(3)
s.insert(7)
s.involve(6)
s.remove(3)

print(s)
