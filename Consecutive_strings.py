def longest_consec(strarr, k):
    cl = []
    fl = []
    gl = []
    s = ''
    if len(strarr) == 0:
        return ""
    elif k <= 0:
        return ""
    elif len(strarr) < k:
        return ""
    else:
        d = k-1
        for i in range(len(strarr)-d):
            for j in range(k):
                cl.append(strarr[i+j])
            fl.append(cl)
            cl = []
        for i in fl:
            s = s.join(i)
            gl.append(s)
            s = ''
        dic = {}
        ll = []
        for i in range(len(gl)):
            ll.append(len(gl[i]))
        for x, y in zip(ll, gl):
            dic[y] = x
        ll.sort()
        for k, v in dic.items():
            if ll[-1] == v:
                return k
        # sorted_list = sorted(gl, key=lambda x: (-len(x), x))
        # print(sorted_list)
        # return sorted_list[0]


print(longest_consec(['uuiiixx', 'lllqqlllvvv', 'xvvqqmmmtt', 'bllcdmm', 'vvkfffookkkttt', 'yggpuuuuutttss', 'jjjblqqqgggjjj', 'xxxvvvpkkk', 'aaaqptxx', 'ttthhhddf', 'ggguuwwuuu', 'phhahw', 'ooobqpp', 'aappaiii', 'iiuuryyj', 'hhhmknnnwwwaaa', 'rjjjzzqvvvfffn', 'xqqqppxxxqqq', 'ffppwqqq', 'lhwwweeeqqq', 'nnnwttrrrl', 'bbacccu', 'ggccsuuubvvvveee', 'wwssj', 'qqqcccjslll', 'jjyhhqddd', 'bbeeevv', 'rrrcckkpaaa', 'mhhkkkaavvvmmm', 'ggka', 'ddddddqnnttt', 'bbkzzzkk', 'neeelll', 'miixpppttt', 'dddyyykkkssaaaxxxuuun', 'ssszrriiaa', 'tnnal', 'yyyiiiyub', 'hhhiiidccqqq', 'cnnnwww', 'zzjjjhhmmmaa', 'izzzmqqqjjj', 'nsssfffbboo', 'yyvvnnnzzznnn', 'zzzfffnnnmmm', 'iioqqdd', 'oooqhhhii', 'mmmmppwwsssaaau', 'svvvvnnyy', 'tttttkfffvvpp', 'ooaaankk', 'eeesssppkkvvwwp', 'hhvvvele', 'vvvlljddnbbbzz', 'gvvvtmbbhh', 'vvvpppxxxssszzzo', 'ffwwgmmaaayyr', 'nntbbf', 'eeygjww', 'ddiiiuupzzz', 'vvvtttbqq', 'bbatmqq', 'cccttov', 'ugaa', 'bhgggoo', 'jclff', 'essooosstttccu', 'hippp', 'wwwggggggboonn', 'vuuttthffq', 'uuuhhhqwa', 'ooqquhhhfffcc', 'eeooett', 'uhpzhsss', 'ppkkkzzzuuunnn', 'kkkuutttqq', 'yyjuiiiyyy', 'jjyyyooozzyybbpsssnnnvvv', 'kmmmjjggii', 'wsssj', 'bbbaaacccu', 'jlllhhhkkk', 'kkxxmmmzzzqqqc', 'nssszzzqqvyy', 'lllwwwdddjjjjjc', 'vvjjjuuuyyyiii', 'viirrgggkkkkk', 'wwwqqppf', 'eeettejjkkszzz', 'ywwwwfffwwnnee', 'vvpmmm', 'gqllbooa', 'ookkqeeennb', 'iippiiingg', 'cczllx', 'qggwwwyffnn', 'fbsqqq', 'jjjqqqkknjj',
      'giisssehd', 'zzzzzzqqqsssgcc', 'iehhppccsss', 'nniiisswyy', 'yyjeekuuqq', 'fffxiiizzzqq', 'mmpppzzz', 'stttmmmm', 'bbbuuukkqqqqtzzh', 'hsssggvvvwddd', 'dddtvvee', 'ycceeezzx', 'nnncccxxxyyy', 'wwnnfffhha', 'eehhbbbeeennnf', 'uuummrrrwwu', 'ziiikuuyyyum', 'ooorrnnfffkkhhhbb', 'hhhnnjjjggoowmk', 'qqqyyyvvveejjjddxxyyy', 'xxxbtssm', 'iiissnnyyyvvzz', 'aaauuwwaa', 'cceeeajj', 'uummmmlll', 'wicccaas', 'yyyccocllg', 'uucfffdd', 'vvnc', 'vllluuqq', 'eevvaapppqtt', 'lllkkkuiiy', 'edkttttkkkjjj', 'wkkkqzzrr', 'qqxxxaahhww', 'rbooocceeefaa', 'vvvnssskkkuuu', 'oiiqsrrrrf', 'nnotttd', 'kttcoooff', 'mcsssz', 'ffkkrrrn', 'qyycvcccbbbcc', 'zzuuuxxxwww', 'tooohhllldd', 'ekkmmm', 'wlllfppv', 'hhhccccnnnzqq', 'ksyiii', 'ccchzzznn', 'vggbjjxxxccc', 'uudjmunll', 'vkkkxxxxxwwxx', 'uulyyhhh', 'rrryynxxnnnr', 'bbbqqigg', 'jjqqkkfffqqqlll', 'aaawwdwww', 'kkkxxxf', 'ooob', 'dddwwwiiizryyyxxx', 'mqqqjjjooohhh', 'qqqvvx', 'hkkccc', 'iiijfffpw', 'bbbjjjp', 'qqqaaamm', 'pppwnnfbbbggglllxx', 'iiivvvccctttt', 'qqqqqqiyyygmm', 'jvvbbbuunnnfffuusss', 'gmwwwtfffyyrjjj', 'lrrrlllkkbbbbggiii', 'tttssccruuueeektt', 'xioppp', 'bbbtttiqq', 'xxbbkoooooffz', 'nnnvmiiijggg', 'mmmsiiinnnzz', 'vhhnnii', 'ndddlllrr', 'tttppoooccc', 'ffiiizzzccmmxkkrrr', 'nnzqqqjjnn', 'xxsssphjj', 'cjmmuuu', 'ddsssooov', 'hhhpppyhhxx', 'kkkzzzqeee', 'kkebbkk', 'eeezzeekkksss', 'zoookkk', 'ccizzzccddd', 'pppvvvkkhhhp', 'zzhhxxbbmm'], 15))
