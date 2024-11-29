data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}



#1
print(data_panen)

#2
print(data_panen ['lokasi2']['hasil_panen']['jagung'])

#3
print(data_panen ['lokasi3']['nama_lokasi'])

#4 & 5
padi1 = (data_panen ['lokasi1']['hasil_panen']['padi'])
padi2 = (data_panen ['lokasi2']['hasil_panen']['padi'])
padi3 = (data_panen ['lokasi3']['hasil_panen']['padi'])
padi4 = (data_panen ['lokasi4']['hasil_panen']['padi'])
padi5 = (data_panen ['lokasi5']['hasil_panen']['padi'])
kedelai1 = (data_panen ['lokasi1']['hasil_panen']['kedelai'])
kedelai2 = (data_panen ['lokasi2']['hasil_panen']['kedelai'])
kedelai3 = (data_panen ['lokasi3']['hasil_panen']['kedelai'])
kedelai4 = (data_panen ['lokasi4']['hasil_panen']['kedelai'])
kedelai5 = (data_panen ['lokasi5']['hasil_panen']['kedelai'])

#6
for i,j in data_panen.items():
    padi = j['hasil_panen']['padi']
    jagung = j['hasil_panen']['jagung']
    lokasi = j['nama_lokasi']

    if padi > 1300 or jagung > 800:
        print(f"{lokasi} memerlukan penanganan khusus")
    else:
        print(f"{lokasi} dalam kondisi baik")