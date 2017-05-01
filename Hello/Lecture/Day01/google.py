"""
구글 입사문제 중에서
--------------------
1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)
"""
"""
풀이 방법

10,000 에는 8 이 없으니 무시하고, 1 부터 9999 까지
X X X 8 인 경우 : 1,000개 ( X X X 는 세자리이므로 0 0 0 ~ 9 9 9 까지 천개)
X X 8 X 인 경우 : 1,000개 ( X X X 는 세자리이므로 0 0 0 ~ 9 9 9 까지 천개)
X 8 X X 인 경우 : 1,000개 ( X X X 는 세자리이므로 0 0 0 ~ 9 9 9 까지 천개)
8 X X X 인 경우 ; 1,000개 ( X X X 는 세자리이므로 0 0 0 ~ 9 9 9 까지 천개)
총 4,000 개 아닌가?
"""
"""
Java로 풀면

public class CountingEight {
    public static void main(String[] args) {
        for (int i=0; i<=10000; i++){
            searchEight(i);
        }
        System.out.println("1에서 10,000 사이에 존재하는 8의 개수는? "+count);
    }
    private static int count = 0;
    public static void searchEight(int num){
        if (num%10==8) count++;
        if (num>10) searchEight(num/10);
    }
}
"""
"""
C로 풀면

int count = 0;
for(int i = 1; i < 10001; i++)
{
    for(int j = i; j > 0; j /= 10)
    {
        if(j % 10 == 8)
        {
            count++;
        }
    }
}

"""
# 그럼 파이선은?
print(str(list(range(1, 10001))).count('8'))