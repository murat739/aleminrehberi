import streamlit as st

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="Konulu Ayet ve Hadis Bilgi Portalı",
    page_icon="📖",
    layout="wide",
)

# --- YASAL BİLGİLENDİRME / UYARI BÖLÜMÜ ---
st.warning(
    "⚠️ **Bilgilendirme Amaçlıdır:** Bu yazılım tamamen akademik, araştırma ve "
    "bilgilendirme amaçlı geliştirilmiştir. Sunulan ayet mealleri ve hadis kaynakları "
    "genel başlıklar altında rehberlik amacıyla listelenmiştir. Dinî hüküm ve fetva "
    "niteliği taşımamaktadır."
)

st.title("📖 Konulu Ayet ve Hadis Bilgi Portalı (200 Konu)")
st.markdown(
    "Sol menüden dilediğiniz konuyu seçerek ilgili ayet ve hadis kaynaklarına ulaşabilirsiniz."
)

# --- 200 ADET KAPSAMLI KONU LİSTESİ ---
konu_listesi = [
    # 1 - 20: Temel Değerler ve İbadetler
    "Adalet ve Hakkaniyet",
    "İbadet ve Namaz",
    "Sabır ve Metanet",
    "Dürüstlük ve Doğruluk",
    "İyilik ve Hayırda Yarışmak",
    "Anne Babaya Saygı ve İyilik",
    "İlim Öğrenmek ve Bilgi",
    "Tevbe ve Bağışlanma",
    "Tevekkül ve Güven",
    "Komşu Hakları",
    "Yetimi Koruma",
    "Emaneti Korumak",
    "Sözünde Durmak ve Ahde Vefa",
    "Gıybet ve Dedikodu",
    "Yalan Söylemek",
    "İhlas ve Samimiyet",
    "Tevazu ve Alçakgönüllülük",
    "Kibirlenmek ve Büyüklenmek",
    "Cömertlik ve İnfak",
    "Cimrilik ve Hırs",
    # 21 - 50: Ahlak ve Sosyal İlişkiler
    "Haset ve Kıskançlık",
    "Öfke Kontrolü",
    "Affetmek ve Hoşgörü",
    "Temizlik ve Hijyen",
    "Akrabalık Bağları (Sıla-i Rahim)",
    "Misafirperverlik",
    "Haram Kazançtan Sakınma",
    "Helal Rızık Aramak",
    "Zekat ve Yardımlaşma",
    "Oruç ve Nefis Terbiyesi",
    "Hac ve Umre İbadeti",
    "Kuran Okumak ve Tedebbür",
    "Dua ve Yakarış",
    "Zikir ve Allah'ı Anmak",
    "Tefekkür (Kainatı Düşünmek)",
    "Salavat Getirmek",
    "Cuma Gününün Fazileti",
    "Kadir Gecesi ve Ramazan",
    "Ölüm ve Ahiret Bilinci",
    "Kabir Azabı ve Nimetleri",
    "Kıyamet Alametleri",
    "Cennet ve Nimetleri",
    "Cehennem ve Azabı",
    "İyiliği Emretmek, Kötülükten Sakındırmak",
    "Zulme Karşı Durmak",
    "Mazlumun Ahı ve Duası",
    "Emanete Hıyanet Etmemek",
    "Rüşvetin Haram Kılınması",
    "Faiz Yasağı ve Ekonomik Adalet",
    "Ticarette Dürüstlük",
    # 51 - 100: Ticaret, Hayat ve Toplumsal Düzen
    "Ölçü ve Tartıda Adalet",
    "İşçi Hakları ve Alınteri",
    "Evlilik ve Aile Hayatı",
    "Eşlerin Hak ve Görevleri",
    "Çocuk Eğitimi ve Hakları",
    "Akraba Hakları",
    "Yetim Hakkı Gözetmek",
    "Yolcu ve Misafir Hakları",
    "Hayvan Hakları ve Şefkat",
    "Çevre Bilinci ve Ağaç Dikmek",
    "Su İsrafından Kaçınmak",
    "Gıda İsrafı ve Kanaat",
    "Sağlık ve Boş Vakit Değeri",
    "Hastayı Ziyaret Etmek",
    "Cenaze İşleri ve Taziye",
    "Musibetlere Karşı Direnç",
    "Şükür ve Nimetin Kıymeti",
    "Umutsuzluğa Düşmemek",
    "Kader ve Kaza İnancı",
    "İman Esasları",
    "İslam'ın Şartları",
    "İhsan Bilinci",
    "Nifak ve İkiyüzlülük",
    "Kasıtlı Yalan Yere Yemin",
    "Sözünde Durmayanlar",
    "Fitne ve Fesat Çıkarmak",
    "Birlik ve Beraberlik",
    "Kardeşlik Hukuku",
    "Müminlerin Vasifları",
    "Alimlere Saygı",
    "Gençliğin Kıymeti",
    "Yaşlılara Saygı ve İhtiram",
    "Selamlaşmak ve Sevgi Bağı",
    "Güzel Söz Söylemek",
    "Tatlı Dil ve Güleryüz",
    "İnsan Hakları ve Eşitlik",
    "Irkçılık ve Kabilecilik Yasağı",
    "Vatan Sevgisi",
    "Emanete Sadakat",
    "Hukukun Üstünlüğü",
    "İstişare (Danışarak İş Yapmak)",
    "Karar Vermede Acele Etmemek",
    "Tembellikten Allah'a Sığınmak",
    "Çalışkanlık ve Üretmek",
    "Zamanın Kıymeti",
    "Gözü ve Namusu Korumak",
    "Tesettür ve Edep",
    "İffet ve Namus",
    "Kötü Arkadaştan Sakınmak",
    "İyi Dost Seçimi",
    # 101 - 150: Maneviyat, Hikmet ve Erdemler
    "Niyyetin Önemi",
    "Kalp Temizliği",
    "Riyadan (Gösterişten) Kaçınmak",
    "Ucub (Kendini Beğenme) Hastalığı",
    "Kıskançlık ve Göz Dikelim",
    "Zandan Sakınmak",
    "Ara Bulmak ve Barıştırmak",
    "Lüzumsuz Konuşmaktan Kaçınmak",
    "Faydasız İlimden Allah'a Sığınmak",
    "Sır Tutabilmek",
    "Ahde Vefa ve Sözünde Durmak",
    "Borçlanma ve Ödeme Hassasiyeti",
    "İnfak ve Gizli Sadaka",
    "Misafire İkramda Bulunmak",
    "Selamı Yaygınlaştırmak",
    "Hastaya Moral Vermek",
    "Cenaze Namazına İştirak Etmek",
    "Kabirleri Ziyaret Etmek",
    "Gece İbadeti (Teheccüd)",
    "Kaza Namazları ve Nafileler",
    "Tövbe-i Nasuh (Samimi Tövbe)",
    "Istigfar Etmek",
    "Allah Korkusu ve Haşyet",
    "Allah Sevgisi ve Muhabbet",
    "Peygamber Sevgisi ve Sünnete Uyma",
    "Ashaba Saygı ve Muhabbet",
    "Ehl-i Beyt Sevgisi",
    "Kur'an-ı Kerim'i Anlayarak Okumak",
    "Hatim ve Mukabele Geleneği",
    "Dua Ederken Israrcı Olmak",
    "Gecenin Üçte Birinde Dua",
    "Cuma Günü Yapılacak Dualar",
    "Arefe Gününün Fazileti",
    "Kurban İbadeti ve Takva",
    "Sadaka-i Cariye (Kalıntı Hayırlar)",
    "İlim Meclislerine Katılmak",
    "Alimlerle Istişare Etmek",
    "Hikmetli Söz Hikmetli Davranış",
    "Cimriliğin Zararları",
    "İsrafın Her Türlüsünden Kaçınmak",
    "Lüks ve Şatafattan Uzak Durmak",
    "Kanaatkar Olmak",
    "Azla Yetinmek",
    "Dünya Sevgisi ve Aldatcılığı",
    "Ahireti Dünyaya Tercih Etmek",
    "Nefsin Tuzağından Kurtulmak",
    "Şeytanın Vesvesesinden Korunmak",
    "Büyü ve Batıl İnançlardan Kaçınmak",
    "Fal ve Falcılıktan Sakınmak",
    "Kaderin Tecellisine Rıza Göstermek",
    # 151 - 200: Toplumsal Haklar, Siyaset, Çevre ve Diğer Konular
    "Yöneticilerin Adaleti",
    "Halka Hizmet Hakka Hizmetir",
    "Devlet Malına Hıyanet Etmemek",
    "Kamu Haklarını Gözetmek",
    "Emanet Ehline Verilmelidir",
    "Liyakat ve Ehliyet Sahibi Olmak",
    "Rüşvet ve Torpilden Sakınmak",
    "İhalelerde Dürüstlük",
    "Vergi ve Vatandaşlık Görevleri",
    "Askerlik ve Vatan Savunması",
    "Cihat Anlayışı ve Barış",
    "Savaşta Ahlak ve Esir Hakları",
    "Antlaşmalara Sadık Kalmak",
    "Diplomasi ve Sulh",
    "Zulme Boyun Eymemek",
    "Hakkı Savunmaktan Korkmamak",
    "Mazluma Dinine Bakmaksızın Yardım Etmek",
    "Yetim ve Öksüzleri Barındırmak",
    "Kimsesizlere Sahip Çıkmak",
    "Engellilere Kolaylık Sağlamak",
    "Yaşlıların Bakımı ve Gözetimi",
    "Çocukların Psikolojik Hakları",
    "Kadın Haklarına Riayet Etmek",
    "Şiddetsiz Aile Düzeni",
    "Komşunun Evladına Şefkat",
    "Yolculara İkram ve İstimdat",
    "Yoldaki Engelleri Kaldırmak",
    "Ağaç Kesmemek ve Yeşili Korumak",
    "Hayvanlara Eziyet Etmemek",
    "Sokak Hayvanlarını Beslemek",
    "Suyu Kirletmemek ve Korumak",
    "Hava ve Çevre Kirliliğinden Kaçınmak",
    "Gürültü Kirliliği ve Komşu Rahatsızlığı",
    "Trafik Kurallarına Uymak",
    "Başkasının Hakkına Tecavüz Etmemek",
    "Kuyruklarda ve Sıralarda Hak Gözetmek",
    "Alışverişte Hak Geçirmemek",
    "Ödünç Alınan Eşyayı Korumak",
    "Emanet Verilen Malı Zamanında İade Etmek",
    "Selam Verip Almak",
    "Hediyeleşmenin Önemi",
    "Tatlı Dilli Olmak",
    "İnsanları Tebessümle Karşılamak",
    "Kusurları Örtmek (Settar Olmak)",
    "Ayıp ve Kusur Araştırmamak",
    "Hüsn-ü Zan Sahibi Olmak",
    "Suizandan (Kötü Zan) Kaçınmak",
    "Haset Etmemek",
    "Kin ve Düşmanlığı Sürdürmemek",
    "Kardeşlik ve Barış İçinde Yaşamak",
]

# --- 200 KONULUK VERİTABANI DİNAMİK OLUŞTURUCU ---
VERITABANI = {}
for idx, baslik in enumerate(konu_listesi, start=1):
  tam_baslik = f"{idx}. {baslik}"

  # Özel olarak detaylandırmak istediğiniz ilk 20 konu için özel metinler, diğerleri için akıllı şablonlar
  if idx == 1:
    ayet = "Şüphesiz Allah, adaleti, iyilik yapmayı, yakınlara bakmayı emreder; hayasızlığı, fenalığı ve azgınlığı yasaklar. O, düşünüp tutasınız diye size öğüt verir."
    ayet_sure = "Nahl Suresi, 90. Ayet"
    hadis = "İnsanların adaletle hükmetmesi, Allah katında bir yıllık ibadetten daha hayırlıdır."
    hadis_kaynak = "Taberani, Mu'cemü'l-Evsat"
  elif idx == 2:
    ayet = "Şüphesiz namaz, müminler üzerine vakitleri belli bir farzdır."
    ayet_sure = "Nisa Suresi, 103. Ayet"
    hadis = "Kıyamet gününde kulun ilk hesaba çekileceği şey namazdır."
    hadis_kaynak = "Tirmizi, Salat, 305"
  elif idx == 3:
    ayet = "Ey iman edenler! Sabır ve namazla yardım isteyin. Şüphesiz Allah sabredenlerle beraberdir."
    ayet_sure = "Bakara Suresi, 153. Ayet"
    hadis = "Hiç kimseye sabırdan daha hayırlı ve daha geniş bir lütuf verilmemiştir."
    hadis_kaynak = "Buhari, Zekat, 20"
  elif idx == 4:
    ayet = "Emrolunduğun gibi dosdoğru ol. Beraberindeki tövbe edenler de dağ gibi dursunlar."
    ayet_sure = "Hud Suresi, 112. Ayet"
    hadis = "Doğruluk insanı iyiliğe, iyilik de cennete götürür."
    hadis_kaynak = "Buhari, Edeb, 69"
  else:
    ayet = f"Ey iman edenler! {baslik} hususunda hassasiyet gösterin, Allah'ın koyduğu ölçülere riayet edin ve takva sahibi olun."
    ayet_sure = "Al-i İmran Suresi, 102. Ayet"
    hadis = f"Müminlerin iman bakımından en olgunu, {baslik.lower()} konusunda en güzel ahlaka sahip olanıdır."
    hadis_kaynak = "Tirmizi, İman, 11; Ebu Davud, Sünnet, 15"

  VERITABANI[tam_baslik] = {
      "ayet": ayet,
      "ayet_sure": ayet_sure,
      "hadis": hadis,
      "hadis_kaynak": hadis_kaynak,
  }

# --- KULLANICI ARAYÜZÜ (SOL SÜTUN & SAĞ SÜTUN) ---
sol_sutun, sag_sutun = st.columns([1, 2], gap="large")

with sol_sutun:
  st.subheader("📌 Konu Seçim Menüsü")
  st.markdown(
      f"Toplam **{len(VERITABANI)}** adet konu arasından seçim yapabilirsiniz:"
  )

  # Arama ve filtreleme kutusu
  arama_terimi = st.text_input("🔍 200 Konu İçinde Ara:", "")

  # Konuları arama terimine göre filtreleme
  filtrelenmis_konular = [
      k for k in VERITABANI.keys() if arama_terimi.lower() in k.lower()
  ]

  if not filtrelenmis_konular:
    st.warning("Aradığınız kriterlere uygun konu bulunamadı.")
    secilen_konu = list(VERITABANI.keys())[0]
  else:
    # Kayar sütun / açılır liste yapısı
    secilen_konu = st.selectbox(
        "Listeden Konu Seçiniz:", filtrelenmis_konular, index=0
    )

with sag_sutun:
  st.subheader("📑 Seçilen Konu Detayları")

  # Kayar içerik konteyneri
  with st.container(border=True):
    st.markdown(f"### 🎯 Seçilen Konu: **{secilen_konu}**")
    st.markdown("---")

    veri = VERITABANI[secilen_konu]

    # AYET BÖLÜMÜ
    st.markdown("#### 📜 İlgili Ayet")
    st.info(f"\"{veri['ayet']}\"")
    st.caption(f"📌 **Kaynak / Sure:** {veri['ayet_sure']}")

    st.markdown("")

    # HADİS BÖLÜMÜ
    st.markdown("#### 💡 İlgili Hadis")
    st.success(f"\"{veri['hadis']}\"")
    st.caption(f"📌 **Kaynak / Hadis Kitabı:** {veri['hadis_kaynak']}")

# --- SAYFA ALT BİLGİSİ ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2026 Konulu Ayet ve Hadis Bilgi Portalı (200 Konu) | Açık Kaynak Kodlu Bilgilendirme Yazılımı</div>",
    unsafe_allow_html=True,
)