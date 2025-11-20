import argparse
import struct
import io
import BytesIO
def main():



    try:
        with open('input.4pbn' , 'rb') as f_in, \
             open('output.4pbn' , 'wb') as f_out:

            print(f"otwarto plik '{f_in.name}' do odczytu")
            print(f"otwarto plik '{f_out.name}' do zapisu")


            pass

            header = f_in.read(12)  # parsowanie nagłówka
            # logika parsowania do zrobienia
            f_out.write(header)

            while True:
                chunk_header = f_in.read(8)

                if not chunk_header:
                    break

                #rozpakowanie headera
                chunk_type, chunk_length = struct.unpack('>4sI' , chunk_header)

                #czytanie payload chunku
                payload = f_in.read(chunk_length)

                #Jeśli długość jest parzysta, czytamy pad
                pad = b''
                if chunk_length % 2 == 0:
                    pad = f_in.read(1)

                #(nie)logika obsługi typów

                    #typ STUS
                if chunk_type == b'STUS':
                    #wypisujemy typ i ilość bajtów
                    print(f"chunk STUS, długość: {chunk_length} bajtów")
                    #tu tworzy się wirtualna pamięć (ciąg bajtów w ramie) z payload
                    input_stream = io.BytesIO(payload)
                    #tu będzie nowy payload
                    output_stream io.BytesIO()
                    
                    #pętla czytająca rekordy do momentu aż skończą się dane w chunku
                    while input_stream.tell() < len(payload): #tell() to metoda używana w plikach, m.in u.w BytesIO, zwraca obecną pozycję kursora!!!!
                    
                        #odczyt 2 bajtów długości imienia     
                        raw_name_len = input_stream.read(2)
                        #Zmiana bajtów na liczby
                        name_len = struct.unpack('<H' , raw_name_len)[0] # < - little endian H -  ushort (2bajty)  0 na końcu bo struck.unpack zwraca krotkę!!!!!
                        
                        #Odczyt imienia
                        name_bytes = input_stream.read(name_len)

                        # odczyt oceny, roku, reserved
                        #B = Uchar (1bajt) H = ushort(2b)
                        #dla wartości 1 bajtowych endinness jest bez znaczenia
                        #oprócz year
                        
                        #czytanie każdej wartości
                        old_score = struct.unpack('B', input_stream.read(1)[0])
                        raw_year - input_stream.read(2)
                        year = struct.unpack('>H', raw_year)[0] #to wyjątek gdzie pomimo wartości 1 bajtowej endinness ma znaczeie
                        
                        raw_reserved = input_stream.read(1)
                        reserved = struct.unpack('B', raw_reserved)[0]
                        
                        

                elif   chunk_type == b'CR32':
                    print("CR32")
                    pass


                else:
                    f_out.write(chunk_header)
                    f_out.write(payload)
                    f_out.write(pad)


    except FileNotFoundError:
        print("Nie znaleziono pliku wejściowego")
    except Exception as exception123:
        print(f"wystąpił błąd {exception123}")





if __name__ == "__main__":
    main()