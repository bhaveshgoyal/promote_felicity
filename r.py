
def compress(s_str):
    dic = {}
    res = ""
    dic[s_str[0]] = 1
    prev = 0
    for each in s_str[1:]:
        try:
            dic[each] += 1
        except KeyError as e:
            dic[each] = 1
            if (dic[s_str[prev]] == 1):
                print "%%" + s_str[prev]
                dic.pop(s_str[prev])
                res += s_str[prev]
            else:
                print "%%##" + s_str[prev]
                res += s_str[prev] + str(dic.pop(s_str[prev]))
        prev += 1
    if (dic[s_str[prev]] == 1):
        res += s_str[prev]
    else:
        res += s_str[prev] + str(dic.pop(s_str[prev]))
    print res
