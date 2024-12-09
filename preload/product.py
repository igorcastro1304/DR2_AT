from .services.reader import stock_reader

def initialize(ProductController):
    opening_stock = "Ozempic;201;15;1200.00#Victoza;202;10;700.00#Trulicity;203;50;800.00#Byetta;204;40;500.00#Bydureon;205;10;550.00#Rybelsus;206;8;600.00#Metformina;207;30;100.00#Jardiance;208;25;400.00#Farxiga;209;5;450.00#Invokana;210;3;400.00#Amaryl;211;12;150.00#Glifage;212;7;100.00"
    
    stock_reader(opening_stock, ProductController)