class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        S = s.split(':')

        start = list(S[0])
        start_num = int(start[1])
        start_letter = start[0]
        stop = list(S[1])
        stop_letter = stop[0]
        stop_number = int(stop[1])

        L = list('abcdefghijklmnopqrstuvwxyz'.upper())
        D1 = dict(zip(range(0,len(L)),L))
        D2 = dict(zip(L,range(0,len(L))))

        print(D2[start_letter])
        print(D2[stop_letter])

        r = []
        for i in range(D2[start_letter],D2[stop_letter]+1):
            letter = D1[i]
            for number in range(start_num,stop_number+1):
                r.append(letter+str(number))
        return r