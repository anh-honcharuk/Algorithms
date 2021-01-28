from random import randint


class Sorting:

    @staticmethod
    def __direction(res, descending):
        if descending == True:
            return res
        else:
            return res[::-1]

    @staticmethod
    def __check_type(l, descending):
        ar = True
        if not type(l) == list:
            raise TypeError("first argument must be 'list'")
            ar = False
        if not type(descending) == bool:
            raise TypeError("second argument must be 'boolean'")
            ar = False
        return ar

    @staticmethod
    def __swap(el1, el2):
        temp = el1
        el1 = el2
        el2 = temp
        return el1, el2

    @staticmethod
    def merge_sort(l, descending):
        if Sorting.__check_type( l, descending ) == True:
            res = Sorting.__merge_sort_rec(l)
            return Sorting.__direction(res, descending)

    @staticmethod
    def __merge_sort_rec(l):
        if len(l) < 2:
            return l
        else:
            div = len(l) // 2
            left = Sorting.__merge_sort_rec(l[0:div])
            right = Sorting.__merge_sort_rec(l[div:len(l)])
            return Sorting.__merge(left, right)

    @staticmethod
    def __merge(left, right):
        result = []
        l = 0
        r = 0
        if len(left) == 1 and len(right) == 1:
            return [min(left[0], right[0]), max(left[0], right[0])]

        for item in range(len(left) + len(right)):
            if l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            elif l >= len(left):

                s = r
                for i in range(s, len(right)):
                    result.append(right[r])
                    r += 1
            elif r >= len(right):
                s = l
                for i in range(s, len(left)):
                    result.append(left[l])
                    l += 1
            else:
                 return result

        return result

    @staticmethod
    def insertion_sort(l, descending):
        if Sorting.__(l, descending) == True:
            count = 0
            for i in range(len(l)):
                for j in range(i, 0, -1):
                     if j > 0 and l[j - 1] > l[j]:
                        count += 1
                        l[j - 1], l[j] = Sorting.__swap(l[j - 1], l[j])
                     else:
                         break
            return Sorting.__direction(l, descending)

    @staticmethod
    def quick_sort(l, descending):
        return Sorting.__direction(Sorting.__rec_quick_sort(l, descending), descending)

    @staticmethod
    def __rec_quick_sort(l, descending):
        if Sorting.__check_type(l, descending ) == True:
            if len(l) < 2:
                return l
            else:
                pivot = l[randint(0, len(l) - 1)]
                # less = [x for x in l if x < pivot]
                # eq = [x for x in l if x == pivot]
                # bigger = [x for x in l if x > pivot]
                less = []
                eq = []
                bigger = []
                for x in l:
                    if x < pivot:
                        less.append(x)
                    elif x == pivot:
                        eq.append(x)
                    else:
                        bigger.append(x)

                return Sorting.__rec_quick_sort(less, descending) + eq + Sorting.__rec_quick_sort(bigger, descending)