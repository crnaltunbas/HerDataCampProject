#  Sayılar(Numbers) ve Karakter Dizileri(Strings)
#  String tırnak işareti ile gösterdiğimiz ifadelerdir.
#  İnteger 0,1,2,3,4,5,6,7,8,9... gibi sayılardır.
#  Float ondalıklı sayılardır. 9.2 gibi
print(9)
type(9.5)
print("Hello world!")
print("Hello AI Ero")
type("naber cano?")
#  type() foksiyonu değişkenimizin, verimizin hangi veri tipinde olduğunu gösterir.

#  Atamalar ve Değişkenler (Assignments & Variables)

a=15
a
b="Hello ai cano"
b
c=10
a*c
a*20
a-c

#  Virtual Environment (Sanal Ortam) ve Paket Yönetimi (Package Manager)
#  Conda hem sanal ortam aracı hem de paket yönetimi aracıdır.
#  Bilgisayardaki sanal ortamın listelenmesi için aşağıdaki komut kullanılır.
#  conda env list
#  Bu komutlar terminalde kullanılır.Sanal ortam oluşturmak için aşağıdaki komut kullanılır.
#  conda create -n kendi sanal ortamımızın ismi yazılır.
#  Oluşturduğumuz sanal ortama gitmek yani aktif etmek için aşğıdaki komut kullanılır.
#  conda activate mynenv
#  Girdiğimiz sanal ortamdan çıkmak için aşağıdaki komut kullanılır.
#  conda deactivate
#  Ortam içerisindeki paketleri görmek için aşağıdaki komut kullanılır.
#  conda list
#  Paket Yüklemek için aşağıdaki komut kullanılır.
#  conda install numpy
#  Aynı anda birden fazla paket yüklemek için paketler arasında bir boşluk bırakarak yazılır.
#  Bunun için aşağıdaki komut kullanılır.
#  conda install numpy scipy pandas
#  Paket silmek için aşağıdaki komut kullanılır.
#  conda remove paket ismi
#  Belirli bir versiyona göre paket yüklemek için aşağıdaki komut kullanılır.
#  conda install numpy=1.26.3
#  Paket yükseltmek için aşağıdaki komut kullanılır.
#  conda upgrade conda
#  Tüm paketlerin yükseltilmesi için aşağıdaki komut kullanılır.
#  conda upgrade -all
#  Oluşturulan sanal ortamın silinmesi için aşağıdaki komut kullanılır.
#  conda env remove -n silinmek istenen sanal ortamın ismi yazılır.


#  pip: pypi (python package index) paket yönetim aracı
#  Paket yüklemek için aşağıdaki komut kullanılır.
#  pip install  paket adı
#  Versiyona göre paket yüklemek için aşağıdaki komut kullanılır.
#  pip install pandas==2.2.0
#  Eğer bir başka çalışmaya veya bir arkadaşınıza versiyon olarak paketleri aktabilmek istiyorsanız bunun iki yolu
#  vardır. İlk olarak pip dünyasında requirements.txt komutu ile conda dünyasında environment.yaml komutu ile bunu
#  gerçekleştirebilirsiniz. Biz condada conda env export > environment.yaml komutunu kullandık. yaml uzantısı yml
#  uzantılı olarakta karşımıza çıkar.
#  Diyelim ki biz bir çalışma yapacağız ve arkadaşımızın yaml dosyasından versiyonları kendimize alarak yeni ama aynı
#  sanal ortamı oluşturmak için conda env create -f environment.yaml komutunu kullanarak aynı sanal ortamı oluşturabilir
#  ve aktif ederek sonrasında paketleri listeleyerek aynı sanal ortamın oluştuğunu görebilirsiniz.







