#Muhammad Furqon (13519184)
#Decrease and conquer (Topological Sort)
#13519184.py
#MatkulDecider
import os

#class untuk simpul terdiri dari kode dan prereq
class Simpul:
    #prereq:derajat masuk ; kode:kode matkul
    def __init__(self,kode,prereq):
        self.kode=kode
        self.prereq=int(prereq)

#Dari list kurangi graph yang sudah diproses
def kurangiPrereq(List, Simpul, Graph):
    sisi=Graph[Simpul.kode]
    #hilangkan sisi ke simpul lain dan kurangi prereq
    for x in sisi:
        for elemen in List:
            if(elemen.kode==x):
                elemen.prereq-=1
    #hilangkan dari dictionary
    Graph.pop(Simpul.kode)

    
#Print isi list objek, debugging purpose
def printListObj(List):
    first=True
    for obj in List:
        print("Kode matkul: "+ obj.kode)
        print("Jumlah prereq: "+ str(obj.prereq))
        first=False
    print("-"*10)

#Menggunakan topological sort
def topologicalSort(ListObj,ListResult,Graph):
    for matkul in ListObj:
        #mengecek adakah matkul yang prereq 0    
        if matkul.prereq==0:
            #list hasil dari satu loop
            indeks=ListObj.index(matkul)
            ListResult.append(ListObj[indeks])

    for matkul_hasil in ListResult:
        #panggil fungsi mengurangi prereq yang membutuhkan matkul tersebut
        kurangiPrereq(ListObj,matkul_hasil,Graph)
        #buang dari list objek
        indeks=ListObj.index(matkul_hasil)
        ListObj.pop(indeks)

def inisialisasiFile(list1,dictionary):
    list_main=[]
    # List setiap barisnya
    os.chdir("..")
    cur_dir=os.getcwd()
    os.chdir(cur_dir+"\\test")
    nama_file = input("Masukkan nama file masukan: ")
    cur_dir=os.getcwd()
    path=cur_dir+ "\\" + nama_file
    file = open(path,"r") 
    #membaca dari file lalu mengubah menjadi bentuk array
    for line in file:
        line=line.strip()
        line=line.replace(" ","")
        line=line.strip(".")
        line.split(",")
        list_main.append(line)

    for x in list_main:
        x= list(x.split(","))
        #bagian head(depan) nama, tail berisi prereq 
        head=x[0]
        tail=x[1:]
        temp_obj = Simpul(head,len(tail))
        list1.append(temp_obj)
        #dimasukkan ke dalam dictionary temporary yang akan digunakan untuk graph
        dictionary.update({head:tail})

def buatGraph(dictionary):
    #format key=simpul lalu value=sisi
    #contoh {'IF1': [], 'IF2': ['IF1', 'IF5'], 'IF4': ['IF2', 'IF5'], 'IF5': []}
    temp_dict={}
    for key in dictionary:
        temp_arr=[]
        for key2 in dictionary:
            temp=dictionary[key2]
            if(key in temp):
                temp_arr.append(key2)
        temp_dict[key]=temp_arr
    return temp_dict

#MAIN PROGRAM
#list objek Simpul
list_objek=[]
#list menyimpan hasil pada semester tersebut
list_hasil=[]
#list hasil total, debugging purpose
list_hasil_all=[]
#list nama semester
list_semester=["I","II","III","IV","V","VI","VII","VIII"]
#temporary dictionary untuk membuat graph
dict_awal={}
#graph yang digunakan dalam memilih matkul
graph={}

#inisialisasi dari file
inisialisasiFile(list_objek,dict_awal)

#buat graph
graph = buatGraph(dict_awal)

semester=0
while(len(list_objek)!=0 and semester<=7):
    #Melakukan topological sort
    topologicalSort(list_objek,list_hasil,graph)
    print("Semester "+ list_semester[semester]+" :",end=" ")
    first=True
    for matkul_diambil in list_hasil:
        if(first):
            print(matkul_diambil.kode,end="")
            first=False
        else:
            print(", "+matkul_diambil.kode,end="")
    print()
    list_hasil_all.append(list_hasil)
    list_hasil=[]    
    semester+=1
input("Tekan enter untuk mengakhiri program")    


