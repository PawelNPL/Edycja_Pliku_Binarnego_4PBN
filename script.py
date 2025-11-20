import argparse
import struct
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

                if chunk_type == b'STUS':
                    print(f"chunk STUS, długość: {chunk_length} bajtów")
                    f_out.write(chunk_header)
                    f_out.write(payload)
                    f_out.write(pad)


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