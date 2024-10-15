def ienakumi_izdevumi_info():
    total_ienakumi = 0
    total_izdevumi = 0
    more = 'ja'

    while more == 'ja':
      
        ienakumi = float(input("Ievadi ienākumus: "))
        izdevumi = float(input("Ievadi izdevumus: "))
        
       
        total_ienakumi += ienakumi
        total_izdevumi += izdevumi

    
        more = input("Vai tev ir vel ienākumi un izdevumi? (ja/ne): ").lower()

        if more == 'ne':
            
            more = 'ne'
        else:
          
            more = 'ja'

    return total_ienakumi, total_izdevumi

def pelna(ienakumi, izdevumi):

    return ienakumi - izdevumi


total_ienakumi, total_izdevumi = ienakumi_izdevumi_info()
profit = pelna(total_ienakumi, total_izdevumi)


print(f"Peļņa: {profit}")
