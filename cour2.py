nom =("riad")
print (nom)
print (type(nom))
print (nom)
nom2 =["riad"]
print (nom2)
print (type(nom2))
nom2[0]="walid"
print (nom2)
num = (1,2,3,4,5,6,7,7,7,8)
print (num.count(7),end="|")
print (num.index(7),end="|")
print (sum(num))
riad = { "nom":"riad","age":19,"email":"riadbendraoua@gmail.com"}
ip = dict (ip1="192.168.1.10",ip2="154.165.25.100")
print (riad,end="|")
print (ip)
print (riad["nom"])
print (riad["email"])
print (ip["ip1"])
riad["datedenaissance"]="2007/02/01"
ip.update({"ip3":"192.168.0.0","ip4":"168.255.255.0"})
print (ip)
print (riad)
del ip["ip4"]
ip3=ip.pop("ip3")
print(ip3)
print (ip)
ip["ipprev"]="127.0.0.0"
ip["ip5"]="41.0.0.0"
print (ip)
ip.pop("ip5")
print (ip)
