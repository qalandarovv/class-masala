# #masala
#
# class Xodim:
#     def init(self, ism, lavozim, maosh):
#         self.ism = ism
#         self.lavozim = lavozim
#         self.maosh = maosh
#
#     def info(self):
#         return f"{self.ism} - {self.lavozim}, {self.maosh} so'm"
# xodimlar = [
#     Xodim("Ali", "Dasturchi", 5000000),
#     Xodim("Vali", "Dizayner", 4000000),
#     Xodim("Hasan", "Menejer", 7000000),
#     Xodim("Husan", "Tester", 3500000),
#     Xodim("Olim", "DevOps", 6000000)
# ]
#
#
# print("=== XODIMLAR RO‘YXATI ===")
# for x in xodimlar:
#     print(x.info())
#
# eng_katta = xodimlar[0]
# for x in xodimlar:
#     if x.maosh > eng_katta.maosh:
#         eng_katta = x
#
# print("\n=== ENG KATTA MAOSHLI XODIM ===")
# print(f"Ismi: {eng_katta.ism}")
# print(f"Lavozimi: {eng_katta.lavozim}")
# print(f"Maoshi: {eng_katta.maosh} so'm")

#7-masala
class Mahsulot:
    def init(self, nomi, miqdori, narxi):
        self.nomi = nomi
        self.miqdori = miqdori
        self.narxi = narxi

    def qiymat(self):
        return self.miqdori * self.narxi

mahsulotlar = [
    Mahsulot("Kompyuter", 10, 8000000),
    Mahsulot("Monitor", 5, 2000000),
    Mahsulot("Klaviatura", 20, 200000),
    Mahsulot("Sichqoncha", 25, 100000),
    Mahsulot("Printer", 5, 3000000)
]
print("=== MAHSULOTLAR OMBORI ===")
umumiy_qiymat = 0

for m in mahsulotlar:
    qiymat = m.qiymat()
    umumiy_qiymat += qiymat
    print(f"{m.nomi}: {m.miqdori} dona x {m.narxi} = {qiymat} so'm")
print("\nUMUMIY QIYMAT:", umumiy_qiymat, "so'm")

