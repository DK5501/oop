from calendar import c
from django.forms import SelectDateWidget

class assemble:
    
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def assemble(self):
        print(f'พนังงาน JIB:สวัสดีครับผม')

class customer:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def customer(self):
        print(f'ลูกค้า:สวัสดีครับผมชื่อ {self.name} ผมอยากได้คอมราคา {self.price} บาทครับ')

class computer:
    def __init__(self,cpu,ram,gpu,mb,ssd,psu):
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu
        self.mb = mb
        self.ssd = ssd
        self.psu = psu

    def computer(self):
        print(f'กำลังประกอบคอมสเปค:')
        print(f'cpu:{self.cpu}')
        print(f'ram:{self.ram}')
        print(f'gpu:{self.gpu}')
        print(f'mb:{self.mb}')
        print(f'ssd:{self.ssd}')
        print(f'psu:{self.psu}')

customer1 = customer('Top','48000')
customer2 = customer('Pond','7800')
assemble1 = assemble('Arm','1')
assemble2 = assemble('Got','2')
computer1 = computer('INTEL Core i5-12400','Gigabyte AORUS RGB DDR4 16GB (8GBx2) 3200 x 1','GIGABYTE RTX 2080 SUPER GAMING OC 8GB x 1','GIGABYTE B660M DS3H','Western Digital Black SN750 SE 1TB NVMe x 1','GIGABYTE P850GM')
computer2 = computer('INTEL Core i7-12700K','CORSAIR Vengeance PRO RGB DDR4 16GB (8GBx2) 2666 White x 1','ASUS RTX 3060 Rog Strix Gaming OC 12GB x 1','GIGABYTE Z690 Aorus Elite','Western Digital Black SN750 SE 1TB NVMe x 1','COOLERMASTER MWE 1050 Gold V2')
print('----------ร้าน JIB----------')
assemble1.assemble()
customer1.customer()
print('พนังงาน JIB:ได้ครับผม')
computer1.computer()
print('---------------------------')
assemble2.assemble()
customer2.customer()
print('พนังงาน JIB:ได้ครับผม')
computer2.computer()
print('---------------------------')
