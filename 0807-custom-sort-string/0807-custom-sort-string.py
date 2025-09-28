class Solution:
    def customSortString(self, order: str, s: str) -> str:


        d_order = dict(zip(order,range(len(order))))

        letters_remaining = [j for j in 'abcdefghijklmnopqrstuvwxyz' if j not in order]

        #print(letters_remaining)
        d_other = dict(zip(letters_remaining,range(len(order),26)))
        
        d_order.update(d_other)

        d_reverse = dict(zip(d_order.values(),d_order.keys()))

        p = []
        for l in s:
            p.append(d_order[l])

        p.sort()
        S = ''
        for k in p:
            S+=d_reverse[k]
        return S
