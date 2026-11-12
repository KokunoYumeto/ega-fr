import io
D=r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
R=r"user/Documents/ega_scan_check_20261101/run_IV4/"
src17=open(D+"ega4-17-fr.tex",encoding='utf-8',newline='').read()
src18=open(D+"ega4-18-fr.tex",encoding='utf-8',newline='').read()
for n in range(105,110):
    t=open(R+f"page_{n}.tex",encoding='utf-8',newline='').read().replace('\r\n','\n')
    first,rest=t.split('\n',1)
    parts=rest.split('% (continued in ega4-18-fr.tex, before its first page marker)\n')
    a=parts[0]
    print(n, first, 'part17 len',len(a), 'in src17:', a in src17, 'count', src17.count(a))
    if len(parts)>1:
        b=parts[1]
        print('   part18 len',len(b),'in src18:', b in src18, 'startswith:', src18.startswith(b))
