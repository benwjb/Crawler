
import requests
import os
 



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
cookies = {'cookie':'usertrack=ezq0pVnkZ8y2gj2BA1gUAg==; _ntes_nnid=b0ae1345131af06989b34a685c82e797,1527681716027; JSESSIONID-WLF-XXD=de1a8ca528e4ede7f9e9ed136594c2790b383a3d55900b7b14d9b9ae051a2cf8ca5400f33da210b026a2916bf1b01c2495e4c81ac430fc510a69824559690a16826e5583bb87115dd368c02ba901d91173c01740fd0049cff3c663b23e31abdf9c80cbec8e24724cfc68da9c235f5e586ae55627c5ecd2669b9ec87f6828e76dd96c17da; __utmz=61349937.1527681717.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; reglogin_doopen=1; _ga=GA1.2.1973314006.1527681717; _gid=GA1.2.995968789.1527681717; fastestuploadproxydomainkey=upload|1527758150296; __utmc=61349937; isguidelayer4phoneregclosed=1; gdxidpyhxdE=1c6z1KaZyAAZfHcqvcNTroLL%2F2jWcxIITXzIV0B8Owvu2vrbqZQHrjccH9Y%2FpyM5VWzIrTKEfQEb5cDbLtRAY%2FsiigUO2s7nXzOmOXlp9IOJluSME4wbyDnymlwiXrdDHPxbUI%5C33WdEfWEy%2BvJDmcYKVTomf3yZxDZUclPcp2Qguumz%3A1527759165151; _9755xjdesxxd_=32; noAdvancedBrowser=0; ANTICSRF=cleared; NTESLOFTSI=C24567977CC06BA92AA1CDF6F0A6A9A0.hzabj-lofter5-8010; firstentry=%2Flogin.do%3FX-From-ISP%3D2|https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D0HU6zx0T374xDFuY_kMrnOGQlxBtLOMn-YHRjdRu_S_%26ck%3D6614.1.86.292.146.292.142.208%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Dc16f956e00037dd7000000035b0fbd44; regtoken=1000; _gat=1; __utma=61349937.1973314006.1527681717.1527758151.1527771611.3; __utmb=61349937.3.8.1527771611; NTES_SESS=efvRalOrCzRtq1mqkY77yWgMQuRvFIw4jTA6Q7Xs9j1YHglxHydKU4THiqIprif11BMLed1WMEyq5eXzwhxEEfYT6fQ79OlumrsON.wZ4SNShQYkKRJILg7mOX7TP41FXwJ744CYmjmoKWy.wu1RgFuhbaFNEFzkCdjBc4RIX9rUfJGX190JokTtEGmorwl3whWqtFqO_Xmt4; NTES_PASSPORT=z9M6Goj9ekZ1iyc8.ecbCIBhC3OVjI7eNVi86AfB0h_kZ2qhZLps8NjZ4GPHm41QQ_Dn7pQyDrLJ0cU8cb9Fgt3E8z5J49mkfJVSiaKF.d7DT_W25XS0qw7cTBhzRTfOAkSPN4DvYjXJ1WdrGx2aXJYaDYGk.4ibn4yPm7Vt.jmnWHQSDBb0_7VZ2tJWgeKu9; S_INFO=1527771636|0|##|396696229@qq.com; P_INFO=396696229@qq.com|1527771636|1|lofter|00&99|null&null&null#shh&null#10#0#0|&0||396696229@qq.com; LOFTER-PHONE-LOGIN-FLAG=0'}
url = 'http://www.lofter.com/view?act=qbview_20130930_01'
r = requests.get(url, cookies=cookies,headers=headers)
r.encoding = 'utf-8'
print(r.text) 
file=open('douban.txt','wb+')
file.write(r.content)
