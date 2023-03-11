import csv
import datetime



# Menü listesini txt'den okur.
def read_menu_list():
    try:
        with open('Menu.txt', 'r') as menu_file:
            print(menu_file.read())
        except:
            print("Menu.txt dosyası bulunamadı, dosyanın bulunduğu konumu kontrol edip tekrar deneyiniz. ")
            exit()
            
# read_menu_list'i çağıraram menüyü yazdırır.
def main():
    read_menu_list()


# pizza süper sınıfı.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # Pizza açıklaması
    def get_description(self):
        return self.description

    # Pizza fiyatı
    def get_cost(self):
        return self.cost


# Pizza alt sınıfları ve çeşitleri.
class klasikPizza(Pizza):
    def __init__(self):
        super().__init__('Klasik Pizza', 85)


class margaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 98)


class turkPizza(Pizza):
    def __init__(self):
        super().__init__('Türk Pizza', 105)


class sadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Pizza', 85)


# Sos süper sınıfı pizzanın alt sınıfı
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        super().__init__(description, cost)
        self.component = component

    # seçilen sos ve pizzanın açıklamasının döndürülmesi
    def get_description(self):
        return super().get_description() + ' ' + self.component.get_description()

    # seçilen sos ve pizzanın fiyatının döndürülmesi
    def get_cost(self):
        return self.component.get_cost() + super().get_cost()


# Sos çeşitleri, Decoratorun alt sınıfı
class Olive(Decorator):
    def __init__(self, component):
        super().__init__(component,'Zeytinli', 5.0)


class Mushroom(Decorator):
    def __init__(self, component):
        super().__init__(component,'Mantarlı', 8.0)


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component,'Etli', 16)


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component,'Keçi Peynirli', 10)


class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component,'Soğanlı', 5)


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component,"Mısırlı", 7)


# Main fonksiyonunu çağırı menüyü yazdırmak
if __name__ == "__main__":
    main()

#Sipariş tarihini al ve csv dosyasına yazdır.
def Time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#Kredi kartı kontrol
def CC_check(ccnum):
    ccnum = str(ccnum)
    if not len(ccnum) == 16:
        return False
    if not ccnum.isdigit():
        return False
    else:
        return True
#CC_cvv kontrol
def CC_cvv(cvv):
    cvv = str(cvv)
    if not len(cvv) == 3:
        return False
    if not cvv.isdigit():
        return False
    else:
        return True

#TC numarası kontrolü
def TC_check(tcnum):
    tcnum = str(tcnum)
    if not len(tcnum) == 11:
        return False
    if not tcnum.isdigit():
        return False
    else:
        return True



# Kullanıcı için pizza seçimi
while True:
    try:
        pizzaChoice = int(input("1-4 Arasında bir pizza seçin."))
    except:
        print("Lütfen doğru bir giriş yapın. ")
    if pizzaChoice == 1:
        pizza = klasikPizza()
        break
    elif pizzaChoice == 2:
        pizza = margaritaPizza()
        break
    elif pizzaChoice == 3:
        pizza = turkPizza()
        break
    elif pizzaChoice == 4:
        pizza = sadePizza()
        break
    else:
        print("Geçersiz pizz seçimi!")

while True:

    sauceChoice = int(input("11-16 Arasında bir sos seçiniz."))

    if sauceChoice == 11:
        sauce = Olive(pizza)
        break
    elif sauceChoice == 12:
        sauce = Mushroom(pizza)
        break
    elif sauceChoice == 13:
        sauce = Meat(pizza)
        break
    elif sauceChoice == 14:
        sauce = GoatCheese(pizza)
        break
    elif sauceChoice == 15:
        sauce = Onion(pizza)
        break
    elif sauceChoice == 16:
        sauce = Corn(pizza)
        break

total_cost = sauce.get_cost()

print("\nSeçiminiz: " + sauce.get_description() + "\nToplam Tutar: " + str(total_cost) + "TL")

#siparişi onaylayıp onaylamadığını sorar
approve = input("Siparişi onaylıyor musunuz?(e/h)")

#e'yi tuşlarsa devam eder h'yi tuşlarsa döngü sonlanır
while True:
    if approve == "e":
        name = input("\nAdınızı giriniz: ")

        #TC kimlik numarası ister ve doğrulamasını yapar
        while True:
            tcnum = input("TC numaranızı giriniz: ")

            if TC_check(tcnum) == True:
                break
            else:
                print("TC numarası doğru değil. ")

        #CC numarası ister ve doğrulamasını yapar
        while True:
            ccnum = input("Kredi Kartı numaranızı giriniz. ")

            if CC_check(ccnum) == True:
                break
            else:
                print("Kredi kartı numarası doğru değil. ")

        #CVV ister ve doğrulamasını yapar
        while True:
            cvv = input("CVV giriniz. ")
            if CC_cvv(cvv) == True:
                break
            else:
                print("CVV numarası doğru değil. ")

    elif approve == "h":
        print("Sipariş iptal edildi.")
        break
    else:
        approve = input("Lütfen e veya h tuşuna basınız.")
        continue
    break

dt_string = Time()

# csv dosyasını aç eğer yok ise oluştur ve kullanıcı bilgilerini, siparişi, tutarı ve zamanı yaz
with open('Orders_Database.csv', 'a') as db_file:
    db_writer = csv.writer(db_file)
    db_writer.writerow([name, tcnum, sauce.get_description(), total_cost, ccnum, cvv, dt_string])

print(f'\nTeşekkürler {name}! {sauce.get_description()} siparişiniz alınmıştır.')
print(f'Toplam tutar: {total_cost:.2f} TL')




