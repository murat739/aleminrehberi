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

# --- 200 ADET KAPSAMLI VE BENZERSİZ KONU VERİTABANI ---
VERITABANI = {
    "1. Adalet ve Hakkaniyet": {
        "ayet": "Şüphesiz Allah, adaleti, iyilik yapmayı, yakınlara bakmayı emreder; hayasızlığı, fenalığı ve azgınlığı yasaklar. O, düşünüp tutasınız diye size öğüt verir.",
        "ayet_sure": "Nahl Suresi, 90. Ayet",
        "hadis": "İnsanların adaletle hükmetmesi, Allah katında bir yıllık ibadetten daha hayırlıdır.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Evsat",
    },
    "2. İbadet ve Namaz": {
        "ayet": "Şüphesiz namaz, müminler üzerine vakitleri belli bir farzdır.",
        "ayet_sure": "Nisa Suresi, 103. Ayet",
        "hadis": "Kıyamet gününde kulun ilk hesaba çekileceği şey namazdır.",
        "hadis_kaynak": "Tirmizi, Salat, 305",
    },
    "3. Sabır ve Metanet": {
        "ayet": "Ey iman edenler! Sabır ve namazla yardım isteyin. Şüphesiz Allah sabredenlerle beraberdir.",
        "ayet_sure": "Bakara Suresi, 153. Ayet",
        "hadis": "Hiç kimseye sabırdan daha hayırlı ve daha geniş bir lütuf verilmemiştir.",
        "hadis_kaynak": "Buhari, Zekat, 20",
    },
    "4. Dürüstlük ve Doğruluk": {
        "ayet": "Emrolunduğun gibi dosdoğru ol. Beraberindeki tövbe edenler de dağ gibi dursunlar.",
        "ayet_sure": "Hud Suresi, 112. Ayet",
        "hadis": "Doğruluk insanı iyiliğe, iyilik de cennete götürür.",
        "hadis_kaynak": "Buhari, Edeb, 69",
    },
    "5. İyilik ve Hayırda Yarışmak": {
        "ayet": "Herkesin yöneldiği bir yönü vardır. Hayırlarda yarışın. Nerede olursanız olun, Allah hepinizi bir araya getirir.",
        "ayet_sure": "Bakara Suresi, 148. Ayet",
        "hadis": "İnsanların en hayırlısı, insanlara faydalı olanıdır.",
        "hadis_kaynak": "Darakutni, Sünen",
    },
    "6. Anne Babaya Saygı ve İyilik": {
        "ayet": "Rabbin, kendisinden başkasına asla ibadet etmemenizi, ana-babaya iyi davranmanızı kesin olarak emretti.",
        "ayet_sure": "İsra Suresi, 23. Ayet",
        "hadis": "Cennet annelerin ayakları altındadır.",
        "hadis_kaynak": "Nesai, Cihad, 6",
    },
    "7. İlim Öğrenmek ve Bilgi": {
        "ayet": "De ki: 'Hiç bilenlerle bilmeyenler bir olur mu?' Doğrusu ancak akıl sahipleri öğüt alırlar.",
        "ayet_sure": "Zümer Suresi, 9. Ayet",
        "hadis": "İlim öğrenmek her müslüman erkek ve kadına farzdır.",
        "hadis_kaynak": "İbn Mace, Mukaddime, 17",
    },
    "8. Tevbe ve Bağışlanma": {
        "ayet": "Ey kendi aleyhlerine aşırılık eden kullarım! Allah'ın rahmetinden ümit kesmeyin. Şüphesiz Allah bütün günahları bağışlar.",
        "ayet_sure": "Zümer Suresi, 53. Ayet",
        "hadis": "Günahından tövbe eden, hiç günah işlememiş gibidir.",
        "hadis_kaynak": "İbn Mace, Zühd, 30",
    },
    "9. Tevekkül ve Güven": {
        "ayet": "Kim Allah'a tevekkül ederse, O kendine yetişir.",
        "ayet_sure": "Talak Suresi, 3. Ayet",
        "hadis": "Eğer siz Allah'a gereği gibi tevekkül etseydiniz, kuşları rızıklandırdığı gibi sizi de rızıklandırırdı.",
        "hadis_kaynak": "Tirmizi, Zühd, 33",
    },
    "10. Komşu Hakları": {
        "ayet": "Allah'a ibadet edin ve O'na hiçbir şeyi ortak koşmayın. Ana babaya, akrabaya, yetimlere, yoksullara, yakın komşuya, uzak komşuya iyi davranın.",
        "ayet_sure": "Nisa Suresi, 36. Ayet",
        "hadis": "Cebrail bana komşu hakkında o kadar çok tavsiyede bulundu ki, neredeyse komşuyu komşuya mirasçı kılacak sandım.",
        "hadis_kaynak": "Buhari, Edeb, 28",
    },
    "11. Yetimi Koruma": {
        "ayet": "Sakın yetime haksızlık etme! İsteyeni de azarlama.",
        "ayet_sure": "Duha Suresi, 9-10. Ayetler",
        "hadis": "Ben ve yetime bakan kimse cennette şöylece yan yana olacağız (orta ve işaret parmağını gösterdi).",
        "hadis_kaynak": "Buhari, Talak, 24",
    },
    "12. Emaneti Korumak": {
        "ayet": "Şüphesiz Allah, emanetleri ehline vermenizi ve insanlar arasında hükmettiğiniz zaman adaletle hükmetmenizi emreder.",
        "ayet_sure": "Nisa Suresi, 58. Ayet",
        "hadis": "Emanete riayet olmayanın imanı yoktur, ahdine sadık olmayanın dini yoktur.",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "13. Sözünde Durmak ve Ahde Vefa": {
        "ayet": "Verdiğiniz sözü de yerine getirin. Çünkü verilen söz sorumluluk gerektirir.",
        "ayet_sure": "İsra Suresi, 34. Ayet",
        "hadis": "Münafığın alameti üçtür: Konuştuğunda yalan söyler, söz verdiğinde cayar, emanete hıyanet eder.",
        "hadis_kaynak": "Buhari, İman, 24",
    },
    "14. Gıybet ve Dedikodu": {
        "ayet": "Ey iman edenler! Zannın birçoğundan sakının. Çünkü zannın bir kısmı günahtır. Birbirinizin kusurunu aramayın, kiminiz kiminizin gıybetini yapmasın.",
        "ayet_sure": "Hucurat Suresi, 12. Ayet",
        "hadis": "Gıybet nedir bilir misiniz? 'Allah ve resulü daha iyi bilir' dediler. Hz. Peygamber: 'Kardeşini hoşlanmadığı bir şeyle anmandır' buyurdu.",
        "hadis_kaynak": "Müslim, Birr, 70",
    },
    "15. Yalan Söylemek": {
        "ayet": "...Artık Allah'ın laneti yalancıların üzerine olsun.",
        "ayet_sure": "Al-i İmran Suresi, 61. Ayet",
        "hadis": "Yalandan sakının; çünkü yalan kötülüğe, kötülük de cehenneme götürür.",
        "hadis_kaynak": "Buhari, Edeb, 69",
    },
    "16. İhlas ve Samimiyet": {
        "ayet": "Oysa onlar, dini yalnız kendisine has kılarak, hanifler olarak Allah'a ibadet etmekten başka bir şeyle emrolunmamışlardı.",
        "ayet_sure": "Beyyine Suresi, 5. Ayet",
        "hadis": "Ameller niyetlere göredir. Herkese niyet ettiği şey vardır.",
        "hadis_kaynak": "Buhari, Bed'ü'l-Vahy, 1",
    },
    "17. Tevazu ve Alçakgönüllülük": {
        "ayet": "Rahman'ın kulları, yeryüzünde tevazu ile yürüyen kimselerdir...",
        "ayet_sure": "Furkan Suresi, 63. Ayet",
        "hadis": "Kim Allah için alçakgönüllülük yaparsa, Allah onu yüceltir.",
        "hadis_kaynak": "Müslim, Birr, 69",
    },
    "18. Kibirlenmek ve Büyüklenmek": {
        "ayet": "Yeryüzünde böbürlenerek yürüme! Çünkü sen ne yeri yarıverebilirsin ne de boyca dağlara erişebilirsin.",
        "ayet_sure": "İsra Suresi, 37. Ayet",
        "hadis": "Kalbinde zerre kadar kibir olan kimse cennete giremez.",
        "hadis_kaynak": "Müslim, İman, 147",
    },
    "19. Cömertlik ve İnfak": {
        "ayet": "Sevdiğiniz şeylerden infak edinceye kadar asla iyiliğe eremezsiniz.",
        "ayet_sure": "Al-i İmran Suresi, 92. Ayet",
        "hadis": "Cömertlik Allah'a yakınlık, cennete yakınlık, halka yakınlık ve cehennemden uzaklıktır.",
        "hadis_kaynak": "Tirmizi, Birr, 40",
    },
    "20. Cimrilik ve Hırs": {
        "ayet": "Allah'ın lütfundan kendilerine verdiklerini cimrilik ederek sakınanlar, bunun kendileri için hayırlı olduğunu sanmasınlar...",
        "ayet_sure": "Al-i İmran Suresi, 180. Ayet",
        "hadis": "Cimrilikten sakınınız. Çünkü cimrilik sizden öncekileri helak etmiştir.",
        "hadis_kaynak": "Müslim, Birr, 56",
    },
    "21. Haset ve Kıskançlık": {
        "ayet": "Yoksa onlar, Allah'ın lütfundan insanlara verdiği şeyleri kıskanıyorlar mı?",
        "ayet_sure": "Nisa Suresi, 54. Ayet",
        "hadis": "Hasetten sakınınız. Çünkü ateşte odunun odunu yiyip bitirdiği gibi, haset de iyilikleri yer bitirir.",
        "hadis_kaynak": "Ebu Davud, Edeb, 44",
    },
    "22. Öfke Kontrolü": {
        "ayet": "Onlar bollukta ve darlıkta infak ederler, öfkelerini yutarlar ve insanları affederler. Allah iyilik edenleri sever.",
        "ayet_sure": "Al-i İmran Suresi, 134. Ayet",
        "hadis": "Güçlü kimse güreşte rakibini yenen değil, öfkelendiği an nefsine hakim olabilendir.",
        "hadis_kaynak": "Buhari, Edeb, 76",
    },
    "23. Affetmek ve Hoşgörü": {
        "ayet": "Sen af yolunu tut, iyiliği emret ve cahillerden yüz çevir.",
        "ayet_sure": "A'raf Suresi, 199. Ayet",
        "hadis": "Affedin ki siz de affedilesiniz.",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "24. Temizlik ve Hijyen": {
        "ayet": "...Şüphesiz Allah tövbe edenleri sever, temizlenenleri de sever.",
        "ayet_sure": "Bakara Suresi, 222. Ayet",
        "hadis": "Temizlik imanın yarısıdır.",
        "hadis_kaynak": "Müslim, Taharet, 1",
    },
    "25. Akrabalık Bağları (Sıla-i Rahim)": {
        "ayet": "Allah'tan korkun ve kendisi adına birbirinizden dilekte bulunduğunuz akrabalık bağlarına riayet edin.",
        "ayet_sure": "Nisa Suresi, 1. Ayet",
        "hadis": "Rızkının genişletilmesini veya ömrünün uzatılmasını isteyen kimse akrabasını gözetsin.",
        "hadis_kaynak": "Buhari, Büyü, 12",
    },
    "26. Misafirperverlik": {
        "ayet": "İbrahim'in şerefli misafirlerinin haberi sana geldi mi?",
        "ayet_sure": "Zariyat Suresi, 24. Ayet",
        "hadis": "Allah'a ve ahiret gününe inanan kimse misafirine ikram etsin.",
        "hadis_kaynak": "Buhari, Edeb, 31",
    },
    "27. Haram Kazançtan Sakınma": {
        "ayet": "Ey iman edenler! Mallarınızı aranızda haksızlıkla yemeyin...",
        "ayet_sure": "Nisa Suresi, 29. Ayet",
        "hadis": "Haramla beslenen vücuda cehennem ateşi daha layıktır.",
        "hadis_kaynak": "Beyhaki, Şuabü'l-İman",
    },
    "28. Helal Rızık Aramak": {
        "ayet": "Yeryüzünde bulunanların helal ve temiz olanlarından yiyin...",
        "ayet_sure": "Bakara Suresi, 168. Ayet",
        "hadis": "Helal rızık aramak, farzlardan sonra bir farzdır.",
        "hadis_kaynak": "Beyhaki, Sünen",
    },
    "29. Zekat ve Yardımlaşma": {
        "ayet": "Namazı kılın, zekatı verin; rükû edenlerle birlikte siz de rükû edin.",
        "ayet_sure": "Bakara Suresi, 43. Ayet",
        "hadis": "Mallarınızı zekat ile koruyun, hastalarınızı sadaka ile tedavi edin.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Evsat",
    },
    "30. Oruç ve Nefis Terbiyesi": {
        "ayet": "Ey iman edenler! Oruç, sizden öncekilere farz kılındığı gibi size de farz kılındı. Umulur ki korunursunuz.",
        "ayet_sure": "Bakara Suresi, 183. Ayet",
        "hadis": "Oruç bir kalkandır. Oruçlu kimse kötü söz söylemesin ve cahillik etmesin.",
        "hadis_kaynak": "Buhari, Savm, 2",
    },
    "31. Hac ve Umre İbadeti": {
        "ayet": "Yoluna gücü yetenlerin o evi (Kâbe'yi) ziyaret etmesi, Allah'ın insanlar üzerindeki bir hakkıdır.",
        "ayet_sure": "Al-i İmran Suresi, 97. Ayet",
        "hadis": "Hacc-ı mebrurun (makbul hac) karşılığı ancak cennettir.",
        "hadis_kaynak": "Buhari, Umre, 1",
    },
    "32. Kuran Okumak ve Tedebbür": {
        "ayet": "Kur'an'ı yavaş yavaş, tane tane oku.",
        "ayet_sure": "Müzzemmil Suresi, 4. Ayet",
        "hadis": "Sizin en hayırlınız Kur'an'ı öğrenen ve öğreteninizdir.",
        "hadis_kaynak": "Buhari, Fedailü'l-Kur'an, 21",
    },
    "33. Dua ve Yakarış": {
        "ayet": "Kullarım sana benden sorarsa, şüphesiz ben çok yakınım. Bana dua edince, dua edenin duasına icabet ederim.",
        "ayet_sure": "Bakara Suresi, 186. Ayet",
        "hadis": "Dua ibadetin kendisidir.",
        "hadis_kaynak": "Tirmizi, Dehawat, 1",
    },
    "34. Zikir ve Allah'ı Anmak": {
        "ayet": "Bilin ki kalpler ancak Allah'ı anmakla huzur bulur.",
        "ayet_sure": "Ra'd Suresi, 28. Ayet",
        "hadis": "Allah'ı zikreden ile zikretmeyen kimsenin misali, diri ile ölü gibidir.",
        "hadis_kaynak": "Buhari, Dehawat, 67",
    },
    "35. Tefekkür (Kainatı Düşünmek)": {
        "ayet": "Göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardınca gelip gidişinde akıl sahipleri için gerçekten ibretler vardır.",
        "ayet_sure": "Al-i İmran Suresi, 190. Ayet",
        "hadis": "Bir saatlik tefekkür, bir gece sabaha kadar ibadet etmekten hayırlıdır.",
        "hadis_kaynak": "Acluni, Keşfü'l-Hafa",
    },
    "36. Salavat Getirmek": {
        "ayet": "Şüphesiz Allah ve melekleri Peygamber'e salat ederler. Ey iman edenler! Siz de ona salat edin ve tam bir teslimiyetle selam verin.",
        "ayet_sure": "Ahzab Suresi, 56. Ayet",
        "hadis": "Kıyamet gününde insanların bana en yakın olanı, bana en çok salavat getirendir.",
        "hadis_kaynak": "Tirmizi, Vitir, 21",
    },
    "37. Cuma Gününün Fazileti": {
        "ayet": "Ey iman edenler! Cuma günü namaza çağrıldığı zaman, hemen Allah'ı anmaya koşun...",
        "ayet_sure": "Cuma Suresi, 9. Ayet",
        "hadis": "Üzerine güneşin doğduğu en hayırlı gün Cuma günüdür.",
        "hadis_kaynak": "Müslim, Cuma, 18",
    },
    "38. Kadir Gecesi ve Ramazan": {
        "ayet": "Kadir gecesi bin aydan daha hayırlıdır.",
        "ayet_sure": "Kadir Suresi, 3. Ayet",
        "hadis": "Kim inanarak ve sevabını Allah'tan bekleyerek Kadir gecesini ihya ederse, geçmiş günahları bağışlanır.",
        "hadis_kaynak": "Buhari, İman, 27",
    },
    "39. Ölüm ve Ahiret Bilinci": {
        "ayet": "Her canlı ölümü tadacaktır. Sizi bir imtihan olarak hayır ile de şer ile de sınayacağız. Sonunda bize döndürüleceksiniz.",
        "ayet_sure": "Enbiya Suresi, 35. Ayet",
        "hadis": "Lezzetleri alt üst edip yok edeni (ölümü) çokça hatırlayın.",
        "hadis_kaynak": "Tirmizi, Zühd, 4",
    },
    "40. Kabir Azabı ve Nimetleri": {
        "ayet": "...Kötü azap Firavun hanedanını kuşattı. Onlar sabah akşam ateşine arz olunurlar...",
        "ayet_sure": "Mümin Suresi, 45-46. Ayetler",
        "hadis": "Kabir, ya cennet bahçelerinden bir bahçe veya cehennem çukurlarından bir çukurdur.",
        "hadis_kaynak": "Tirmizi, Kıyamet, 26",
    },
    "41. Kıyamet Alametleri": {
        "ayet": "Onlar ancak kıyamet gününün gelip çatma-sını gözlüyorlar. Şüphesiz onun alametleri gelmiştir...",
        "ayet_sure": "Muhammed Suresi, 18. Ayet",
        "hadis": "Ben ve kıyamet şu iki (parmak) gibi gönderildik.",
        "hadis_kaynak": "Buhari, Rikak, 39",
    },
    "42. Cennet ve Nimetleri": {
        "ayet": "İnanıp salih ameller işleyenler için altından ırmaklar akan cennetler vardır.",
        "ayet_sure": "Buruc Suresi, 11. Ayet",
        "hadis": "Cennette hiçbir gözün görmediği, hiçbir kulağın işitmediği ve insanın kalbinden geçmeyen nimetler vardır.",
        "hadis_kaynak": "Buhari, Bed'ü'l-Halk, 8",
    },
    "43. Cehennem ve Azabı": {
        "ayet": "Korkun o ateşten ki kafirler için hazırlanmıştır.",
        "ayet_sure": "Al-i İmran Suresi, 131. Ayet",
        "hadis": "Bu dünya ateşiniz, cehennem ateşinin yetmişte biridir.",
        "hadis_kaynak": "Buhari, Bed'ü'l-Halk, 10",
    },
    "44. İyiliği Emretmek, Kötülükten Sakındırmak": {
        "ayet": "Sizden, hayra çağıran, iyiliği emreden ve kötülükten sakındıran bir topluluk olsun...",
        "ayet_sure": "Al-i İmran Suresi, 104. Ayet",
        "hadis": "Kim bir kötülük görürse, onu eliyse düzeltsin; gücü yetmezse diliyle düzeltsin; ona da gücü yetmezse kalbiyle buğzedsin.",
        "hadis_kaynak": "Müslim, İman, 78",
    },
    "45. Zulme Karşı Durmak": {
        "ayet": "Zulmedenlere meyletmeyin; sonra size ateş dokunur...",
        "ayet_sure": "Hud Suresi, 113. Ayet",
        "hadis": "İnsanlar zalimi görüp de elini tutmazlarsa, Allah'ın hepsini genel bir azaba uğratması yakındır.",
        "hadis_kaynak": "Ebu Davud, Melahim, 17",
    },
    "46. Mazlumun Ahı ve Duası": {
        "ayet": "Mazlumun bedduasından sakın. Çünkü onunla Allah arasında perde yoktur.",
        "ayet_sure": "Buhari Şerhi (Hadis Kaynaklı Anlam)",
        "hadis_kaynak": "Buhari, Mezalim, 9",
        "hadis": "Mazlumun bedduasından sakının, çünkü onunla Allah arasında hiçbir engel yoktur.",
    },
    "47. Emanete Hıyanet Etmemek": {
        "ayet": "Ey iman edenler! Allah'a ve Resul'e hıyanet etmeyin; bile bile size emanet edilenlere de hıyanet etmeyin.",
        "ayet_sure": "Enfal Suresi, 27. Ayet",
        "hadis": "Sana emanet bırakana emanetini iade et, sana hıyanet edene hıyanet etme.",
        "hadis_kaynak": "Ebu Davud, Buyu, 79",
    },
    "48. Rüşvetin Haram Kılınması": {
        "ayet": "Aranızda mallarınızı haksızlıkla yemeyin ve hakimlere rüşvet vermeyin...",
        "ayet_sure": "Bakara Suresi, 188. Ayet",
        "hadis": "Rüşvet alana da verene de Allah lanet etsin.",
        "hadis_kaynak": "Tirmizi, Ahkam, 9",
    },
    "49. Faiz Yasağı ve Ekonomik Adalet": {
        "ayet": "Allah alıverişi helal, faizi haram kılmıştır.",
        "ayet_sure": "Bakara Suresi, 275. Ayet",
        "hadis": "Faiz yiyene, yedirene, yazıcısına ve iki şahidine Allah lanet etmiştir.",
        "hadis_kaynak": "Müslim, Müsakat, 106",
    },
    "50. Ticarette Dürüstlük": {
        "ayet": "Ölçüyü tam yapın, eksultanlardan olmayın. Dosdoğru terazi ile tartın.",
        "ayet_sure": "Şuara Suresi, 181-182. Ayetler",
        "hadis": "Dürüst ve güvenilir tüccar, peygamberler, sıddıklar ve şehitlerle beraberdir.",
        "hadis_kaynak": "Tirmizi, Buyu, 4",
    },
    "51. Ölçü ve Tartıda Adalet": {
        "ayet": "Eksik ölçüp tartanların vay haline!",
        "ayet_sure": "Mutaffifin Suresi, 1. Ayet",
        "hadis": "Ölçü ve tartıda hile yapan topluluklar kıtlık ve zulümle cezalandırılırlar.",
        "hadis_kaynak": "İbn Mace, Fiten, 22",
    },
    "52. İşçi Hakları ve Alınteri": {
        "ayet": "Kim salih bir amelde bulunursa, ister erkek ister kadın... kesinlikle onlara yaptıklarından daha güzeliyle karşılık veririz.",
        "ayet_sure": "Nahl Suresi, 97. Ayet",
        "hadis": "İşçiye ücretini alın teri kurumadan veriniz.",
        "hadis_kaynak": "İbn Mace, Ruhun, 4",
    },
    "53. Evlilik ve Aile Hayatı": {
        "ayet": "Kendileri ile huzur bulasınız diye sizin için türünüzden eşler yaratması ve aranızda bir sevgi ve merhamet var etmesi de O'nun delillerindendir.",
        "ayet_sure": "Rum Suresi, 21. Ayet",
        "hadis": "Nikah benim sünnetimdir; sünnetimden yüz çeviren benden değildir.",
        "hadis_kaynak": "İbn Mace, Nikah, 1",
    },
    "54. Eşlerin Hak ve Görevleri": {
        "ayet": "...Kadınların hakları gibi erkeklerin de kadınlar üzerinde kurallara uygun hakları vardır...",
        "ayet_sure": "Bakara Suresi, 228. Ayet",
        "hadis": "Sizin en hayırlınız, kadınlarına karşı en hayırlı olanınızdır.",
        "hadis_kaynak": "Tirmizi, Rada, 11",
    },
    "55. Çocuk Eğitimi ve Hakları": {
        "ayet": "Ey iman edenler! Kendinizi ve ailenizi yakıtı insanlar ve taşlar olan ateşten koruyun.",
        "ayet_sure": "Tahrim Suresi, 6. Ayet",
        "hadis": "Hiçbir baba çocuğuna güzel ahlaktan daha üstün bir miras bırakmamıştır.",
        "hadis_kaynak": "Tirmizi, Birr, 33",
    },
    "56. Akraba Hakları": {
        "ayet": "Akrabaya, yoksula ve yolda kalmışa hakkını ver...",
        "ayet_sure": "İsra Suresi, 26. Ayet",
        "hadis": "Sadaka vermenin iki sevabı vardır: Biri sadaka sevabı, diğeri akrabaya yardım etme sevabı.",
        "hadis_kaynak": "Tirmizi, Zekat, 26",
    },
    "57. Yetim Hakkı Gözetmek": {
        "ayet": "Haksızlıkla yetimlerin mallarını yiyenler ancak karınlarına ateş tıkınmış olurlar...",
        "ayet_sure": "Nisa Suresi, 10. Ayet",
        "hadis": "İnsanı helak eden yedi büyük günahtan biri yetim malı yemektir.",
        "hadis_kaynak": "Buhari, Vesaya, 23",
    },
    "58. Yolcu ve Misafir Hakları": {
        "ayet": "Akrabaya, yoksula, yolcuya hakkını ver, fakat malını da saçıp savurma.",
        "ayet_sure": "İsra Suresi, 26. Ayet",
        "hadis": "Yolcuya ikramda bulunmak ve onun ihtiyacını görmek büyük sevaptır.",
        "hadis_kaynak": "Müslim, Hac, 412",
    },
    "59. Hayvan Hakları ve Şefkat": {
        "ayet": "Yeryüzünde yürüyen hiçbir hayvan ve kanatlarıyla uçan hiçbir kuş yoktur ki sizin gibi birer ümmet olmasınlar.",
        "ayet_sure": "En'am Suresi, 38. Ayet",
        "hadis": "Merhamet etmeyene merhamet olunmaz.",
        "hadis_kaynak": "Buhari, Edeb, 18",
    },
    "60. Çevre Bilinci ve Ağaç Dikmek": {
        "ayet": "...Yeryüzünü ıslah ettikten sonra orada bozgunculuk yapmayın...",
        "ayet_sure": "A'raf Suresi, 85. Ayet",
        "hadis": "Herhangi bir müslüman bir ağaç diker veya tohum ekerse, ondan kuş, insan veya hayvan yediği takdirde bu onun için sadaka olur.",
        "hadis_kaynak": "Buhari, Müzaraa, 1",
    },
    "61. Su İsrafından Kaçınmak": {
        "ayet": "Yiyin, için fakat israf etmeyin; çünkü O, israf edenleri sevmez.",
        "ayet_sure": "A'raf Suresi, 31. Ayet",
        "hadis": "Akan bir nehir başında bile olsanız, suyu israf etmeyin.",
        "hadis_kaynak": "İbn Mace, Taharet, 48",
    },
    "62. Gıda İsrafı ve Kanaat": {
        "ayet": "O, çardaklı ve çardaksız bahçeleri, ürünleri, çeşit çeşit hurmaları, tadları farklı ekinleri... yaratandır. Her biri ürün verdiğinde meyvesinden yiyin...",
        "ayet_sure": "En'am Suresi, 141. Ayet",
        "hadis": "Kanaat tükenmeyen bir hazinedir.",
        "hadis_kaynak": "Beyhaki, Şuabü'l-İman",
    },
    "63. Sağlık ve Boş Vakit Değeri": {
        "ayet": "...İnsana az bir şükür verdim...",
        "ayet_sure": "Secde Suresi, 9. Ayet",
        "hadis": "İki nimet vardır ki insanların çoğu onlar hususunda aldanmıştır: Sağlık ve boş vakit.",
        "hadis_kaynak": "Buhari, Rikak, 1",
    },
    "64. Hastayı Ziyaret Etmek": {
        "ayet": "...(İyilik ediniz) şüphesiz Allah iyilik edenleri sever.",
        "ayet_sure": "Bakara Suresi, 195. Ayet",
        "hadis": "Bir müslüman hastayı sabah ziyaret ederse, akşam oluncaya kadar yetmiş bin melek onun için istiğfar eder.",
        "hadis_kaynak": "Tirmizi, Cenaiz, 2",
    },
    "65. Cenaze İşleri ve Taziye": {
        "ayet": "Her nefis ölümü tadacaktır...",
        "ayet_sure": "Ali İmran Suresi, 185. Ayet",
        "hadis": "Ölülerinize yasin suresini okuyun.",
        "hadis_kaynak": "Ebu Davud, Cenaiz, 24",
    },
    "66. Musibetlere Karşı Direnç": {
        "ayet": "Onlar ki, başlarına bir musibet geldiğinde, 'Biz şüphesiz Allah'a aidiz ve şüphesiz O'na döneceğiz' derler.",
        "ayet_sure": "Bakara Suresi, 156. Ayet",
        "hadis": "Müminin durumu ne gariptir! Her işi onun için bir hayırdır...",
        "hadis_kaynak": "Müslim, Zühd, 64",
    },
    "67. Şükür ve Nimetin Kıymeti": {
        "ayet": "Şükrederseniz elbette size nimeti artırırım...",
        "ayet_sure": "İbrahim Suresi, 7. Ayet",
        "hadis": "İnsanlara teşekkür etmeyen, Allah'a şükretmez.",
        "hadis_kaynak": "Tirmizi, Birr, 35",
    },
    "68. Umutsuzluğa Düşmemek": {
        "ayet": "...Allah'ın rahmetinden ümit kesmeyin; çünkü kafirler topluluğundan başkası Allah'ın rahmetinden ümit kesmez.",
        "ayet_sure": "Yusuf Suresi, 87. Ayet",
        "hadis": "Ben kulumun bana olan zannı yanındayım.",
        "hadis_kaynak": "Buhari, Tevhid, 35",
    },
    "69. Kader ve Kaza İnancı": {
        "ayet": "Yeryüzünde musibet veya sizin başınıza bir musibet gelirse, biz onu yaratmadan önce mutlaka bir kitapta yazılmıştır.",
        "ayet_sure": "Hadid Suresi, 22. Ayet",
        "hadis": "Başınıza gelen bir şeyin sizi atlatması, sizi atlayanın da başınıza gelmesi asla mümkün değildir.",
        "hadis_kaynak": "Ebu Davud, Sünnet, 16",
    },
    "70. İman Esasları": {
        "ayet": "Peygamber, Rabbinden kendisine indirilene iman etti, müminler de...",
        "ayet_sure": "Bakara Suresi, 285. Ayet",
        "hadis": "İman; Allah'a, meleklerine, kitaplarına, peygamberlerine, ahiret gününe ve kadere (hayır ve şerrin Allah'tan olduğuna) inanmandır.",
        "hadis_kaynak": "Müslim, İman, 1",
    },
    "71. İslam'ın Şartları": {
        "ayet": "...Kim Allah'a ve ahiret gününe iman ederse...",
        "ayet_sure": "Nisa Suresi, 39. Ayet",
        "hadis": "İslam beş ş üzerine kurulmuştur: Allah'tan başka ilah olmadığına ve Muhammed'in O'nun elçisi olduğuna şehadet etmek, namaz kılmak, zekat vermek, Kabe'yi haccetmek ve Ramazan orucu tutmak.",
        "hadis_kaynak": "Buhari, İman, 1",
    },
    "72. İhsan Bilinci": {
        "ayet": "Şüphesiz Allah, adaleti, iyilik yapmayı (ihsanı) emreder...",
        "ayet_sure": "Nahl Suresi, 90. Ayet",
        "hadis": "İhsan, Allah'ı görüyormuş gibi ibadet etmendir; sen O'nu görmesen de O seni kesinlikle görmektedir.",
        "hadis_kaynak": "Buhari, İman, 37",
    },
    "73. Nifak ve İkiyüzlülük": {
        "ayet": "Münafıklar şüphesiz cehennemin en alt tabakasındadırlar...",
        "ayet_sure": "Nisa Suresi, 145. Ayet",
        "hadis": "Münafığın alameti üçtür: Konuştuğunda yalan söyler, sözünde durmaz, kendisine bir şey emanet edildiğinde hıyanet eder.",
        "hadis_kaynak": "Buhari, İman, 24",
    },
    "74. Kasıtlı Yalan Yere Yemin": {
        "ayet": "Allah'a verdiğiniz sözü ve yeminlerinizi az bir pahaya satmayın...",
        "ayet_sure": "Nahl Suresi, 95. Ayet",
        "hadis": "Kim bir müslümanın hakkını gasp etmek için yalan yere yemin ederse, Allah ona cehennemi vacip, cenneti haram kılar.",
        "hadis_kaynak": "Müslim, İman, 218",
    },
    "75. Sözünde Durmayanlar": {
        "ayet": "Ey iman edenler! Yapamayacağınız şeyleri niçin söylersiniz?",
        "ayet_sure": "Saff Suresi, 2. Ayet",
        "hadis": "Sözünde durmayanlar kıyamet günü her birinin arkasında dikilen bir bayrakla tanınacaklar.",
        "hadis_kaynak": "Müslim, Cihad, 13",
    },
    "76. Fitne ve Fesat Çıkarmak": {
        "ayet": "Fitne çıkarmak, adam öldürmekten daha büyüktür.",
        "ayet_sure": "Bakara Suresi, 191. Ayet",
        "hadis": "Fitne uykudadır, onu uyandirana Allah lanet etsin.",
        "hadis_kaynak": "Acluni, Keşfü'l-Hafa",
    },
    "77. Birlik ve Beraberlik": {
        "ayet": "Hep birlikte Allah'ın ipine sımsıkı sarılın; parça parça olmayın.",
        "ayet_sure": "Al-i İmran Suresi, 103. Ayet",
        "hadis": "Cemaat rahmettir, ayrılık ise azaptır.",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "78. Kardeşlik Hukuku": {
        "ayet": "Müminler ancak kardeştirler. Öyleyse kardeşlerinizin arasını bulun...",
        "ayet_sure": "Hucurat Suresi, 10. Ayet",
        "hadis": "Müslüman müslümanın kardeşidir; ona zulmetmez, onu düşmanına teslim etmez.",
        "hadis_kaynak": "Buhari, Mezalim, 3",
    },
    "79. Müminlerin Vasifları": {
        "ayet": "Mümin erkekler ve mümin kadınlar birbirlerinin velileridirler...",
        "ayet_sure": "Tevbe Suresi, 71. Ayet",
        "hadis": "Müminler birbirlerini sevmekte, birbirlerine merhamet etmekte ve birbirlerini korumakta tek bir vücut gibidirler.",
        "hadis_kaynak": "Buhari, Edeb, 27",
    },
    "80. Alimlere Saygı": {
        "ayet": "...Kulları içinde ancak alimler, Allah'tan (gerektiği gibi) korkar...",
        "ayet_sure": "Fatır Suresi, 28. Ayet",
        "hadis": "Alimler peygamberlerin varisleridir.",
        "hadis_kaynak": "Ebu Davud, İlim, 1",
    },
    "81. Gençliğin Kıymeti": {
        "ayet": "Biz sana onların kıssalarını gerçek olarak anlatıyoruz. Onlar Rablerine iman etmiş birkaç genç idiler ve biz de onların hidayetlerini artırmıştık.",
        "ayet_sure": "Kehf Suresi, 13. Ayet",
        "hadis": "Hiçbir gölgenin bulunmadığı kıyamet gününde Allah, adaletli devlet başkanını ve gençliğini Allah ibadetiyle geçiren genci kendi arşının gölgesinde gölgelendirecektir.",
        "hadis_kaynak": "Buhari, Ezan, 36",
    },
    "82. Yaşlılara Saygı ve İhtiram": {
        "ayet": "...Anne babaya ve yaşlılara ikram edin...",
        "ayet_sure": "İsra Suresi, 23. Ayet",
        "hadis": "Küçüğümüze merhamet etmeyen, büyüğümüzün hakkını bilmeyen bizden değildir.",
        "hadis_kaynak": "Tirmizi, Birr, 15",
    },
    "83. Selamlaşmak ve Sevgi Bağı": {
        "ayet": "Bir selam ile selamlandığınızda, siz de ondan daha güzeliyle karşılık verin veya aynısını iade edin...",
        "ayet_sure": "Nisa Suresi, 86. Ayet",
        "hadis": "İman etmedikçe cennete giremezsiniz; birbirinizi sevmedikçe de iman etmiş olmazsınız. Yaptığınızda birbirinizi seveceğiniz şeyi söyleyeyim mi? Aranızda selamı yaygınlaştırın.",
        "hadis_kaynak": "Müslim, İman, 93",
    },
    "84. Güzel Söz Söylemek": {
        "ayet": "Güzel bir söz ve bağışlama, peşinden gönül kırma gelen bir sadakadan daha hayırlıdır.",
        "ayet_sure": "Bakara Suresi, 263. Ayet",
        "hadis": "Güzel söz sadakadır.",
        "hadis_kaynak": "Buhari, Edeb, 34",
    },
    "85. Tatlı Dil ve Güleryüz": {
        "ayet": "...İnsanlara güzel söz söyleyin...",
        "ayet_sure": "Bakara Suresi, 83. Ayet",
        "hadis": "Din kardeşini güleryüzle karşılaman bile olsa, hiçbir iyiliği hor görme.",
        "hadis_kaynak": "Müslim, Birr, 144",
    },
    "86. İnsan Hakları ve Eşitlik": {
        "ayet": "Ey insanlar! Şüphesiz sizi bir erkek ile bir dişiden yarattık...",
        "ayet_sure": "Hucurat Suresi, 13. Ayet",
        "hadis": "Ey insanlar! Rabbiniz birdir, atanız da birdir. Hepiniz Adem'in çocuklarısınız...",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "87. Irkçılık ve Kabilecilik Yasağı": {
        "ayet": "Tanışasınız diye sizi milletlere ve kabilelere ayırdık...",
        "ayet_sure": "Hucurat Suresi, 13. Ayet",
        "hadis": "Irkçılığa çağıran bizden değildir, ırkçılık dava uğruna ölen bizden değildir.",
        "hadis_kaynak": "Ebu Davud, Edeb, 121",
    },
    "88. Vatan Sevgisi": {
        "ayet": "Eğer onlara, 'Kendinizi öldürün veya yurtlarınızdan çıkın' diye yazsaydık, içlerinden pek azı hariç bunu yapmazlardı...",
        "ayet_sure": "Nisa Suresi, 66. Ayet",
        "hadis": "Vatan sevgisi imandandır.",
        "hadis_kaynak": "Acluni, Keşfü'l-Hafa",
    },
    "89. Emanete Sadakat": {
        "ayet": "...O kimseler ki emanetlerine ve ahitlerine riayet ederler.",
        "ayet_sure": "Mearic Suresi, 32. Ayet",
        "hadis": "Mümin, insanların can ve malları konusunda kendisinden emin oldukları kimsedir.",
        "hadis_kaynak": "Tirmizi, İman, 12",
    },
    "90. Hukukun Üstünlüğü": {
        "ayet": "Ey iman edenler! Adaleti titizlikle ayakta tutan, kendinizin, ana-babanızın ve akrabanızın aleyhine de olsa Allah için şahitlik eden kimseler olun...",
        "ayet_sure": "Nisa Suresi, 135. Ayet",
        "hadis": "Sizden önceki ümmetlerin helak olmasının sebebi şuydu: İçlerinden asil biri hırsızlık yapınca onu bırakırlar, zayıf biri hırsızlık yapınca ona cezayı uygularlardı.",
        "hadis_kaynak": "Buhari, Hudud, 12",
    },
    "91. İstişare (Danışarak İş Yapmak)": {
        "ayet": "...İşlerinde onlarla istişare et...",
        "ayet_sure": "Al-i İmran Suresi, 159. Ayet",
        "hadis": "İstişare eden pişman olmaz.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Evsat",
    },
    "92. Karar Vermede Acele Etmemek": {
        "ayet": "...Acelecilik insandan yaratılmıştır...",
        "ayet_sure": "Enbiya Suresi, 37. Ayet",
        "hadis": "Acele etmek şeytandandır.",
        "hadis_kaynak": "Tirmizi, Birr, 88",
    },
    "93. Tembellikten Allah'a Sığınmak": {
        "ayet": "...Onlar namaza kalktıkları zaman üşene üşene kalkarlar...",
        "ayet_sure": "Nisa Suresi, 142. Ayet",
        "hadis": "Allah'ım! Acizlikten, tembellikten, korkaklıktan ve cimrilikten sana sığınırım.",
        "hadis_kaynak": "Buhari, Daavat, 36",
    },
    "94. Çalışkanlık ve Üretmek": {
        "ayet": "İnsana ancak çalışmasının karşılığı vardır.",
        "ayet_sure": "Necm Suresi, 39. Ayet",
        "hadis": "Hiç kimse asla kendi elinin emeğinden daha hayırlı bir lokma yememiştir.",
        "hadis_kaynak": "Buhari, Buyu, 15",
    },
    "95. Zamanın Kıymeti": {
        "ayet": "Asra yemin ederim ki, insan gerçekten ziyan içindedir.",
        "ayet_sure": "Asr Suresi, 1-2. Ayetler",
        "hadis": "İki nimet vardır ki insanların çoğu onların kıymetini bilmez: Sıhhat ve boş vakit.",
        "hadis_kaynak": "Buhari, Rikak, 1",
    },
    "96. Gözü ve Namusu Korumak": {
        "ayet": "Mümin erkeklere söyle: Gözlerini haramdan sakınsınlar ve namuslarını korusunlar...",
        "ayet_sure": "Nur Suresi, 30. Ayet",
        "hadis": "Bana dilini ve bacakları arasındaki (namusunu) koruma sözü verin, ben de size cenneti söz vereyim.",
        "hadis_kaynak": "Buhari, Rikak, 23",
    },
    "97. Tesettür ve Edep": {
        "ayet": "Ey Peygamber! Eşlerine, kızlarına ve müminlerin kadınlarına söyle, dış elbiselerini üzerlerine alsınlar...",
        "ayet_sure": "Ahzab Suresi, 59. Ayet",
        "hadis": "Hayanın tamamı hayırdır.",
        "hadis_kaynak": "Müslim, İman, 61",
    },
    "98. İffet ve Namus": {
        "ayet": "Namuslu kadınlara zina iftirası atıp da sonra dört şahit getiremeyenlere seksen değnek vurun...",
        "ayet_sure": "Nur Suresi, 4. Ayet",
        "hadis": "İnsanları helak eden yedi büyük günahtan kaçının: ...ve iffetli mümin kadınlara zina isnad etmek...",
        "hadis_kaynak": "Buhari, Vesaya, 23",
    },
    "99. Kötü Arkadaştan Sakınmak": {
        "ayet": "O gün dostlar, Allah'a karşı gelenler dışında birbirine düşmandır.",
        "ayet_sure": "Zuhruf Suresi, 67. Ayet",
        "hadis": "Kişi dostunun dini üzeredir. Öyleyse her biriniz kiminle arkadaşlık ettiğine baksın.",
        "hadis_kaynak": "Ebu Davud, Edeb, 16",
    },
    "100. İyi Dost Seçimi": {
        "ayet": "Mümin erkekler ve mümin kadınlar birbirlerinin velileridirler...",
        "ayet_sure": "Tevbe Suresi, 71. Ayet",
        "hadis": "İyi arkadaş ile kötü arkadaşın misali, misk taşıyan kimse ile körük üfleyen kimse gibidir...",
        "hadis_kaynak": "Buhari, Zebaih, 31",
    },
    "101. Niyyetin Önemi": {
        "ayet": "...Kalplerinizde olanı Allah bilir...",
        "ayet_sure": "Ahzab Suresi, 51. Ayet",
        "hadis": "Ameller ancak niyetlere göredir. Herkese niyet ettiği şey vardır.",
        "hadis_kaynak": "Buhari, Bed'ü'l-Vahy, 1",
    },
    "102. Kalp Temizliği": {
        "ayet": "O gün ki, ne mal fayda verir ne de oğullar. Ancak Allah'a salim (temiz) bir kalple gelenler müstesna.",
        "ayet_sure": "Şuara Suresi, 88-89. Ayetler",
        "hadis": "Şüphesiz Allah sizin bedenlerinize ve suretlerinize bakmaz, ancak kalplerinize ve amellerinize bakar.",
        "hadis_kaynak": "Müslim, Birr, 34",
    },
    "103. Riyadan (Gösterişten) Kaçınmak": {
        "ayet": "Ey iman edenler! Sadakalarınızı başa kakmak ve eziyet etmek suretiyle boşa çıkarmayın; tıpkı malını halka gösteriş yapmak için harcayan... kimse gibi.",
        "ayet_sure": "Bakara Suresi, 264. Ayet",
        "hadis": "Sizin adınıza en çok korktuğum şey küçük şirk yani riyadır.",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "104. Ucub (Kendini Beğenme) Hastalığı": {
        "ayet": "Kendi kendinizi övmeyin; O, kimin sakındığını çok iyi bilir.",
        "ayet_sure": "Necm Suresi, 32. Ayet",
        "hadis": "Üç şey helak edicidir: Kendisine uyulan aşırı cimrilik, peşinden gidilen heva ve kişinin kendisini beğenmesi (ucub).",
        "hadis_kaynak": "Beyhaki, Şuabü'l-İman",
    },
    "105. Kıskançlık ve Göz Dikelim": {
        "ayet": "Sakın kendilerini sınamak için onlardan bir kesime verdiğimiz dünya hayatının süslerine göz dikme...",
        "ayet_sure": "Taha Suresi, 131. Ayet",
        "hadis": "Sizden biriniz mal ve yaratılış bakımından kendisinden üstün olan birine baktığı zaman, hemen kendisinden aşağıda olana baksın.",
        "hadis_kaynak": "Müslim, Zühd, 9",
    },
    "106. Zandan Sakınmak": {
        "ayet": "Ey iman edenler! Zannın birçoğundan sakının; çünkü zannın bir kısmı günahtır...",
        "ayet_sure": "Hucurat Suresi, 12. Ayet",
        "hadis": "Zandan sakının; çünkü zan sözlerin en yalanıdır.",
        "hadis_kaynak": "Buhari, Edeb, 57",
    },
    "107. Ara Bulmak ve Barıştırmak": {
        "ayet": "Müminler ancak kardeştirler. Öyleyse kardeşlerinizin arasını bulun...",
        "ayet_sure": "Hucurat Suresi, 10. Ayet",
        "hadis": "İki kişinin arasını düzeltmek, namaz, oruç ve sadakadan daha faziletlidir.",
        "hadis_kaynak": "Ebu Davud, Edeb, 50",
    },
    "108. Lüzumsuz Konuşmaktan Kaçınmak": {
        "ayet": "Onlar ki, boş ve faydasız şeylerden yüz çevirirler.",
        "ayet_sure": "Müminun Suresi, 3. Ayet",
        "hadis": "Kişinin malayani (faydasız) şeyleri terk etmesi İslam'ının güzelliğindendir.",
        "hadis_kaynak": "Tirmizi, Zühd, 11",
    },
    "109. Faydasız İlimden Allah'a Sığınmak": {
        "ayet": "Rabbim! ilmimi artır.",
        "ayet_sure": "Taha Suresi, 114. Ayet",
        "hadis": "Allah'ım! Fayda vermeyen ilimden, ürpermeyen kalpten, doymayan nefsekten ve kabul olunmayan duadan sana sığınırım.",
        "hadis_kaynak": "Müslim, Zikir, 73",
    },
    "110. Sır Tutabilmek": {
        "ayet": "...Ve ahitlerini ve sırlarını korurlar.",
        "ayet_sure": "Mearic Suresi, 32. Ayet",
        "hadis": "Bir kimse bir söz söyler de sağa sola bakınırsa o söz emanettir.",
        "hadis_kaynak": "Ebu Davud, Edeb, 37",
    },
    "111. Ahde Vefa ve Sözünde Durmak": {
        "ayet": "...Ahdinizi yerine getirin; çünkü ahitten sorumlusunuz.",
        "ayet_sure": "İsra Suresi, 34. Ayet",
        "hadis": "Ahde vefası olmayanın dini yoktur.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Evsat",
    },
    "112. Borçlanma ve Ödeme Hassasiyeti": {
        "ayet": "Ey iman edenler! Belirlenmiş bir vade ile birbirinize borçlandığınız zaman bunu yazın...",
        "ayet_sure": "Bakara Suresi, 282. Ayet",
        "hadis": "Ödeme imkanı olan zenginin borcunu geciktirmesi zulümdür.",
        "hadis_kaynak": "Buhari, Hibe, 23",
    },
    "113. İnfak ve Gizli Sadaka": {
        "ayet": "Sadakaları açıktan verirseniz ne güzel; fakat onları gizler ve yoksullara öyle verirseniz bu sizin için daha hayırlıdır...",
        "ayet_sure": "Bakara Suresi, 271. Ayet",
        "hadis": "Sağ elin verdiğini sol el görmeyecek kadar gizli sadaka veren kimseyi Allah arşın gölgesinde gölgelendirir.",
        "hadis_kaynak": "Buhari, Zekat, 16",
    },
    "114. Misafire İkramda Bulunmak": {
        "ayet": "İbrahim'in şerefli misafirlerinin haberi sana geldi mi?",
        "ayet_sure": "Zariyat Suresi, 24. Ayet",
        "hadis": "Misafir ilk gün ve gecede ağırlanmayı hak eder...",
        "hadis_kaynak": "Buhari, Edeb, 31",
    },
    "115. Selamı Yaygınlaştırmak": {
        "ayet": "...Evlere girdiğinizde birbirinize Allah katından mübarek ve tertip edilmiş bir esenlikle (selamla) selam verin.",
        "ayet_sure": "Nur Suresi, 61. Ayet",
        "hadis": "İman etmedikçe cennete giremezsiniz; birbirinizi sevmedikçe de iman etmiş olmazsınız. Aranızda selamı yayınız.",
        "hadis_kaynak": "Müslim, İman, 93",
    },
    "116. Hastaya Moral Vermek": {
        "ayet": "...Biz insanı en güzel biçimde yarattık...",
        "ayet_sure": "Tin Suresi, 4. Ayet",
        "hadis": "Bir hastanın yanına girdiğinizde ona uzun ömürlü olacağını söyleyerek moral verin...",
        "hadis_kaynak": "Tirmizi, Tıp, 35",
    },
    "117. Cenaze Namazına İştirak Etmek": {
        "ayet": "Onlardan biri ölürse asla namazını kılma ve kabri başında durma...",
        "ayet_sure": "Tevbe Suresi, 84. Ayet",
        "hadis": "Kim bir cenaze namazını kılarsa ona bir kırat, defin edilinceye kadar bulunursa iki kırat sevap vardır.",
        "hadis_kaynak": "Buhari, Cenaiz, 58",
    },
    "118. Kabirleri Ziyaret Etmek": {
        "ayet": "...Hayır, yakında bileceksiniz! Yine hayır, yakında bileceksiniz! Eğer kesin olarak bilseniz...",
        "ayet_sure": "Tekasür Suresi, 3-5. Ayetler",
        "hadis": "Kabirleri ziyaret edin; çünkü kabir ziyareti size ahireti hatırlatır.",
        "hadis_kaynak": "Müslim, Cenaiz, 108",
    },
    "119. Gece İbadeti (Teheccüd)": {
        "ayet": "Gecenin bir kısmında uyanıp sana mahsus bir nafile olarak namaz kıl. Umulur ki Rabbin seni övülen bir makama çıkarır.",
        "ayet_sure": "İsra Suresi, 79. Ayet",
        "hadis": "Farz namazlardan sonra en faziletli namaz gece (teheccüd) namazıdır.",
        "hadis_kaynak": "Müslim, Siyam, 203",
    },
    "120. Kaza Namazları ve Nafileler": {
        "ayet": "...Namazı kılın, zekatı verin ve Allah'a sıkı sarılın...",
        "ayet_sure": "Hac Suresi, 78. Ayet",
        "hadis": "Kim unuttuğu bir namazı kılmayı unutursa veya uyuyakalırsa, hatırladığı an onu kilsin.",
        "hadis_kaynak": "Buhari, M مواقيت, 37",
    },
    "121. Tövbe-i Nasuh (Samimi Tövbe)": {
        "ayet": "Ey iman edenler! Samimi bir tövbe ile Allah'a dönün...",
        "ayet_sure": "Tahrim Suresi, 8. Ayet",
        "hadis": "Samimi tövbe eden, tıpkı hiç günahı olmayan kimse gibidir.",
        "hadis_kaynak": "İbn Mace, Zühd, 30",
    },
    "122. Istigfar Etmek": {
        "ayet": "...Rabbinizden bağışlanma dileyin, sonra O'na tövbe edin. Şüphesiz Rabbin çok merhametlidir, çok sevgi doludur.",
        "ayet_sure": "Hud Suresi, 90. Ayet",
        "hadis": "Kim istiğfara devam ederse, Allah onu her sıkıntıdan çıkarır ve hiç ummadığı yerden rızıklandırır.",
        "hadis_kaynak": "Ebu Davud, Vitir, 26",
    },
    "123. Allah Korkusu ve Haşyet": {
        "ayet": "...Kulları içinde ancak alimler Allah'tan hakkıyla korkarlar...",
        "ayet_sure": "Fatır Suresi, 28. Ayet",
        "hadis": "Allah korkusundan ağlayan kimse, sağılan süt memeye dönmedikçe cehenneme girmez.",
        "hadis_kaynak": "Tirmizi, Zühd, 53",
    },
    "124. Allah Sevgisi ve Muhabbet": {
        "ayet": "İnsanlardan öylesini vardır ki, Allah'tan başkasını O'na denkler edinirler de onları Allah'ı sever gibi severler. İman edenlerin Allah'a sevgisi ise kat kat fazladır.",
        "ayet_sure": "Bakara Suresi, 165. Ayet",
        "hadis": "Üç şey kimde bulunursa o imanın tadını alır: Allah ve Resulü'nü her şeyden çok sevmek...",
        "hadis_kaynak": "Buhari, İman, 9",
    },
    "125. Peygamber Sevgisi ve Sünnete Uyma": {
        "ayet": "De ki: 'Eğer Allah'ı seviyorsanız bana uyun ki Allah da sizi sevsin ve günahlarınızı bağışlasın...'",
        "ayet_sure": "Al-i İmran Suresi, 31. Ayet",
        "hadis": "Hiçbiriniz beni, çocuğundan, anasından ve bütün insanlardan daha çok sevmedikçe gerçek anlamda iman etmiş olamaz.",
        "hadis_kaynak": "Buhari, İman, 8",
    },
    "126. Ashaba Saygı ve Muhabbet": {
        "ayet": "Muhacir ve Ensar'dan (İslam'a girmekte) ilk öncüler ile onlara güzellikle uyanlar var ya, Allah onlardan razı olmuştur, onlar da O'ndan razı olmuşlardır...",
        "ayet_sure": "Tevbe Suresi, 100. Ayet",
        "hadis": "Ashabım hakkında kötü konuşmayın; haklarında kötü konuşmaktan sakının.",
        "hadis_kaynak": "Tirmizi, Menakıb, 58",
    },
    "127. Ehl-i Beyt Sevgisi": {
        "ayet": "Ey Ehl-i Beyt! Allah sizden ancak kirliğii gidermek ve sizi tertemiz yapmak ister.",
        "ayet_sure": "Ahzab Suresi, 33. Ayet",
        "hadis": "Size aranızda bıraktığım iki şeyi hatırlatırım: Biri Allah'ın kitabı, diğeri Ehl-i Beyt'im.",
        "hadis_kaynak": "Müslim, Fedailü's-Sahabe, 36",
    },
    "128. Kur'an-ı Kerim'i Anlayarak Okumak": {
        "ayet": "Bu Kur'an, ayetlerini düşünsünler ve akıl sahipleri öğüt alsınlar diye sana indirdiğimiz mübarek bir kitaptır.",
        "ayet_sure": "Sad Suresi, 29. Ayet",
        "hadis": "Sizin en hayırlınız Kur'an'ı öğrenen ve öğreteninizdir.",
        "hadis_kaynak": "Buhari, Fedailü'l-Kur'an, 21",
    },
    "129. Hatim ve Mukabele Geleneği": {
        "ayet": "...Kur'an okunduğu zaman onu dinleyin ve susun ki merhamet olunasınız.",
        "ayet_sure": "A'raf Suresi, 204. Ayet",
        "hadis": "Kim Kur'an'ı baştan sona okursa (hatim yaparsa), onun kabul olunmuş bir duası vardır.",
        "hadis_kaynak": "Darimi, Fezailü'l-Kur'an, 20",
    },
    "130. Dua Ederken Israrcı Olmak": {
        "ayet": "Rabbinize alçak gönüllü olarak ve gizlice dua edin...",
        "ayet_sure": "A'raf Suresi, 55. Ayet",
        "hadis": "Allah, ısrarla dua edenleri sever.",
        "hadis_kaynak": "Beyhaki, Şuabü'l-İman",
    },
    "131. Gecenin Üçte Birinde Dua": {
        "ayet": "...Gecenin bir kısmında ve seher vakitlerinde istiğfar ederlerdi.",
        "ayet_sure": "Zariyat Suresi, 18. Ayet",
        "hadis": "Yüce Rabbimiz, her gece dünyanın en yakın gökyüzüne iner ve gecenin son üçte biri kalınca 'Bana dua eden yok mu, duasına icabet edeyim' buyurur.",
        "hadis_kaynak": "Buhari, Teheccüd, 14",
    },
    "132. Cuma Günü Yapılacak Dualar": {
        "ayet": "...Cuma günü namaza çağrıldığınızda hemen Allah'ın zikrine koşun...",
        "ayet_sure": "Cuma Suresi, 9. Ayet",
        "hadis": "Cuma gününde öyle bir saat vardır ki, müslüman bir kul o saatte namaz kılarken Allah'tan bir şey isterse Allah ona dilediğini mutlaka verir.",
        "hadis_kaynak": "Buhari, Cuma, 37",
    },
    "133. Arefe Gününün Fazileti": {
        "ayet": "...Arafat'tan akın edip inerken Meşar-i Haram yanında Allah'ı zikredin...",
        "ayet_sure": "Bakara Suresi, 198. Ayet",
        "hadis": "Arefe gününden daha çok cehennem ateşinden azat edilen başka bir gün yoktur.",
        "hadis_kaynak": "Müslim, Hac, 436",
    },
    "134. Kurban İbadeti ve Takva": {
        "ayet": "Onların ne etleri ne de kanları Allah'a ulaşır; fakat O'na ulaşan ancak sizin takvanızdır.",
        "ayet_sure": "Hac Suresi, 37. Ayet",
        "hadis": "Kurban kesen kimse için kanının ilk damlası yere düştüğü anda bütün günahları bağışlanır.",
        "hadis_kaynak": "Tirmizi, Edahi, 1",
    },
    "135. Sadaka-i Cariye (Kalıntı Hayırlar)": {
        "ayet": "...Önceden yaptıklarını ve geride bıraktıkları eserleri yazarız.",
        "ayet_sure": "Yasin Suresi, 12. Ayet",
        "hadis": "İnsan öldüğü zaman amel defteri kapanır. Ancak üç şey hariç: Sadaka-i cariye (faydası süren hayır), kendisinden yararlanılan ilim veya kendisine dua eden hayırlı evlat.",
        "hadis_kaynak": "Müslim, Vasiyyet, 14",
    },
    "136. İlim Meclislerine Katılmak": {
        "ayet": "Ey iman edenler! Meclislerde size 'Yer açın' denildiği zaman yer açın ki Allah da size genişlik versin...",
        "ayet_sure": "Mücadele Suresi, 11. Ayet",
        "hadis": "Bir topluluk Allah'ın evlerinden birinde toplanıp Allah'ın kitabını okursa ve onu aralarında müzakere ederse üzerlerine secine (huzur ve rahmet) iner.",
        "hadis_kaynak": "Müslim, Zikir, 38",
    },
    "137. Alimlerle Istişare Etmek": {
        "ayet": "...Eğer bilmiyorsanız zikir ehline (bilenlere) sorun.",
        "ayet_sure": "Nahl Suresi, 43. Ayet",
        "hadis": "Alimlerle oturun, hikmet sahipleriyle konuşun.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Kebir",
    },
    "138. Hikmetli Söz ve Davranış": {
        "ayet": "Kime hikmet verilmişse, ona pek çok hayır verilmiş demektir.",
        "ayet_sure": "Bakara Suresi, 269. Ayet",
        "hadis": "Hikmet müminin yitik malıdır; onu nerede bulursa alsın.",
        "hadis_kaynak": "Tirmizi, İlim, 19",
    },
    "139. Cimriliğin Zararları": {
        "ayet": "...Kim cimrilik ederse, ancak kendi nehyine cimrilik etmiş olur.",
        "ayet_sure": "Muhammed Suresi, 38. Ayet",
        "hadis": "Cimrilikten sakının; çünkü cimrilik sizden öncekileri helak etmiştir.",
        "hadis_kaynak": "Müslim, Birr, 56",
    },
    "140. İsrafın Her Türlüsünden Kaçınmak": {
        "ayet": "Yiyin, için fakat israf etmeyin...",
        "ayet_sure": "A'raf Suresi, 31. Ayet",
        "hadis": "Yiyiniz, sadaka veriniz ve giyininiz; ancak kibirlenmeden ve israf etmeden.",
        "hadis_kaynak": "Buhari, Libas, 1",
    },
    "141. Lüks ve Şatafattan Uzak Durmak": {
        "ayet": "Dünya hayatı ancak bir oyun ve eğlencedir...",
        "ayet_sure": "Muhammed Suresi, 36. Ayet",
        "hadis": "Sadeliğe özen göstermek imandandır.",
        "hadis_kaynak": "Ebu Davud, Tereccül, 1",
    },
    "142. Kanaatkar Olmak": {
        "ayet": "...Şükrederseniz nimetimi artırırım...",
        "ayet_sure": "İbrahim Suresi, 7. Ayet",
        "hadis": "Kanaat bitmez tükenmez bir maldır.",
        "hadis_kaynak": "Taberani, Mu'cemü'l-Evsat",
    },
    "143. Azla Yetinmek": {
        "ayet": "Müslüman olarak canımı al ve beni salihlere kat.",
        "ayet_sure": "Yusuf Suresi, 101. Ayet",
        "hadis": "İslam ile şereflendirilen ve geçimi yetecek kadar (azla) rızıklandırılan kimse kurtuluşa ermiştir.",
        "hadis_kaynak": "Müslim, Zekat, 125",
    },
    "144. Dünya Sevgisi ve Aldatcılığı": {
        "ayet": "Bilin ki dünya hayatı ancak bir oyun, bir eğlence, bir süs, aranızda bir övünme ve mal ve evlat çoğaltma yarışından ibarettir...",
        "ayet_sure": "Hadid Suresi, 20. Ayet",
        "hadis": "Dünya tatlı ve yeşildir. Şüphesiz Allah onu sizin tasarrufunuza verecek ve nasıl davranacağınıza bakacaktır.",
        "hadis_kaynak": "Müslim, Zikir, 99",
    },
    "145. Ahireti Dünyaya Tercih Etmek": {
        "ayet": "Fakat siz dünya hayatını tercih ediyorsunuz. Oysa ahiret daha hayırlı ve daha kalıcıdır.",
        "ayet_sure": "A'la Suresi, 16-17. Ayetler",
        "hadis": "Dünya ahirete göre ancak birinizin denize batırdığı parmağının sudan ne kadar alabileceğine benzer.",
        "hadis_kaynak": "Müslim, Cennet, 55",
    },
    "146. Nefsin Tuzağından Kurtulmak": {
        "ayet": "...Şüphesiz nefis aşırı şekilde kötülüğü emreder...",
        "ayet_sure": "Yusuf Suresi, 53. Ayet",
        "hadis": "Asıl mücahit, Allah yolunda nefsiyle cihad edendir.",
        "hadis_kaynak": "Tirmizi, Fedailü'l-Cihad, 2",
    },
    "147. Şeytanın Vesvesesinden Korunmak": {
        "ayet": "Şeytan size düşmandır, siz de onu düşman edinin...",
        "ayet_sure": "Fatır Suresi, 6. Ayet",
        "hadis": "Şeytan insan damarlarında kan gibi dolaşır.",
        "hadis_kaynak": "Buhari, Ahkâm, 21",
    },
    "148. Büyü ve Batıl İnançlardan Kaçınmak": {
        "ayet": "...Onlar ancak bir büyücünün hilesini yapmışlardır. Büyücü ise nereye varsa asla felaha eremez.",
        "ayet_sure": "Taha Suresi, 69. Ayet",
        "hadis": "Helak edici yedi büyük günahtan kaçının: Allah'a ortak koşmak, büyü yapmak...",
        "hadis_kaynak": "Buhari, Vesaya, 23",
    },
    "149. Fal ve Falcılıktan Sakınmak": {
        "ayet": "Ey iman edenler! Şarap, kumar, dikili taşlar (putlar), fal okları ancak şeytan işi pisliklerdir; bunlardan kaçının ki kurtuluşa eresiniz.",
        "ayet_sure": "Maide Suresi, 90. Ayet",
        "hadis": "Kim bir falcıya gider ve ona bir şey sorarsa, kırk gün namazı kabul olmaz.",
        "hadis_kaynak": "Müslim, Selam, 125",
    },
    "150. Kaderin Tecellisine Rıza Göstermek": {
        "ayet": "...Allah'ın izni olmadan hiçbir musibet isabet etmez...",
        "ayet_sure": "Teğabün Suresi, 11. Ayet",
        "hadis": "Kaza ve kadere rıza göstermek, insanın saadettindendir.",
        "hadis_kaynak": "Tirmizi, Kader, 15",
    },
    "151. Yöneticilerin Adaleti": {
        "ayet": "Şüphesiz Allah size emanetleri ehline vermenizi ve insanlar arasında hükmettiğiniz zaman adaletle hükmetmenizi emreder.",
        "ayet_sure": "Nisa Suresi, 58. Ayet",
        "hadis": "Adaletli yöneticiler, kıyamet gününde Rahman'ın katında nurdan minberler üzerinde olacaklardır.",
        "hadis_kaynak": "Müslim, İmare, 18",
    },
    "152. Halka Hizmet Hakka Hizmettir": {
        "ayet": "İyilik ederseniz kendinize iyilik etmiş olursunuz...",
        "ayet_sure": "İsra Suresi, 7. Ayet",
        "hadis": "Kavmin efendisi, onlara hizmet edendir.",
        "hadis_kaynak": "Acluni, Keşfü'l-Hafa",
    },
    "153. Devlet Malına Hıyanet Etmemek": {
        "ayet": "Hiçbir peygamberin emanete hıyanet etmesi (ganimet malından gizlemesi) düşünülemez...",
        "ayet_sure": "Al-i İmran Suresi, 161. Ayet",
        "hadis": "Kimin üzerinde devlet malından veya ganimetten en küçük bir hıyanet kalmışsa, o kıyamet günü bunu sırtında taşır.",
        "hadis_kaynak": "Buhari, Cihad, 190",
    },
    "154. Kamu Haklarını Gözetmek": {
        "ayet": "...Yeryüzünde fesat çıkararak bozgunculuk yapmayın.",
        "ayet_sure": "Bakara Suresi, 60. Ayet",
        "hadis": "Haksız yere bir karış toprağa (kamu malına) tecavüz eden kimse, kıyamet günü yedi kat yere kadar batırılır.",
        "hadis_kaynak": "Buhari, Mezalim, 13",
    },
    "155. Emanet Ehline Verilmelidir": {
        "ayet": "...Emanetleri ehline vermenizi emreder...",
        "ayet_sure": "Nisa Suresi, 58. Ayet",
        "hadis": "İş ehil olmayana verildiği zaman kıyameti bekleyin.",
        "hadis_kaynak": "Buhari, İlim, 2",
    },
    "156. Liyakat ve Ehliyet Sahibi Olmak": {
        "ayet": "Şüphesiz aralarındaki en hayırlı işçi, güçlü ve güvenilir olandır.",
        "ayet_sure": "Kasas Suresi, 26. Ayet",
        "hadis": "Kim bir topluluğa yönetici tayin eder de aralarında o işe daha layık (ehil) biri varken başkasını seçerse, Allah'a ve Resulü'ne hıyanet etmiş olur.",
        "hadis_kaynak": "Hakim, Müstedrek",
    },
    "157. Rüşvet ve Torpilden Sakınmak": {
        "ayet": "Aranızda mallarınızı haksız yere yemeyin...",
        "ayet_sure": "Bakara Suresi, 188. Ayet",
        "hadis": "Rüşvet alana da verene de Allah lanet etsin.",
        "hadis_kaynak": "Tirmizi, Ahkam, 9",
    },
    "158. İhalelerde Dürüstlük": {
        "ayet": "Ölçüyü ve tartıyı tam yapın, insanların haklarını kısmayın...",
        "ayet_sure": "A'raf Suresi, 85. Ayet",
        "hadis": "Bizi aldatan bizden değildir.",
        "hadis_kaynak": "Müslim, İman, 164",
    },
    "159. Vergi ve Vatandaşlık Görevleri": {
        "ayet": "Ey iman edenler! Akitlerinizi yerine getirin...",
        "ayet_sure": "Maide Suresi, 1. Ayet",
        "hadis": "Müslümanlar şartlarına ve kanunlarına uymak zorundadır.",
        "hadis_kaynak": "Tirmizi, Ahkam, 17",
    },
    "160. Askerlik ve Vatan Savunması": {
        "ayet": "Ey iman edenler! Sabredin, sebat edin, (cihad için) hazırlıklı olun ve Allah'ın koruması altında bulunun ki kurtuluşa eresiniz.",
        "ayet_sure": "Al-i İmran Suresi, 200. Ayet",
        "hadis": "Allah yolunda bir gün nöbet tutmak, dünyadan ve üzerindeki her şeyden hayırlıdır.",
        "hadis_kaynak": "Buhari, Cihad, 73",
    },
    "161. Cihat Anlayışı ve Barış": {
        "ayet": "Eğer onlar barışa yanaşırlarsa sen de ona yanaş ve Allah'a tevekkül et...",
        "ayet_sure": "Enfal Suresi, 61. Ayet",
        "hadis": "Asıl mücahit, Allah'a itaat konusunda nefsiyle cihad edendir.",
        "hadis_kaynak": "Tirmizi, Fedailü'l-Cihad, 2",
    },
    "162. Savaşta Ahlak ve Esir Hakları": {
        "ayet": "...Size karşı savaşanlarla Allah yolunda savaşın, ancak aşırı gitmeyin. Çünkü Allah aşırı gidenleri sevmez.",
        "ayet_sure": "Bakara Suresi, 190. Ayet",
        "hadis": "Savaşa çıktığınızda çocukları, kadınları, yaşlıları öldürmeyin, ibadethanelere ve ağaçlara zarar vermeyin.",
        "hadis_kaynak": "Ebu Davud, Cihad, 82",
    },
    "163. Antlaşmalara Sadık Kalmak": {
        "ayet": "Kendileriyle antlaşma yaptığınız müşriklerden size karşı hiçbir eksiklik yapmamış ve kimseye yardım etmemiş olanlar müstesna; antlaşmalarınızı süresine kadar tam tamamlayın.",
        "ayet_sure": "Tevbe Suresi, 4. Ayet",
        "hadis": "Ahdine ve sözleşmesine sadık kalmayan kimse güvenilir değildir.",
        "hadis_kaynak": "Ahmed bin Hanbel, Müsned",
    },
    "164. Diplomasi ve Sulh": {
        "ayet": "Sulh (barış) en hayırlısıdır.",
        "ayet_sure": "Nisa Suresi, 128. Ayet",
        "hadis": "İnsanların arasını düzeltmek sadakadır.",
        "hadis_kaynak": "Buhari, Sulh, 11",
    },
    "165. Zulme Boyun Eymemek": {
        "ayet": "Zulmedenlere meyletmeyin; sonra size ateş dokunur...",
        "ayet_sure": "Hud Suresi, 113. Ayet",
        "hadis": "Haksızlığa karşı susan dilsiz şeytandandır.",
        "hadis_kaynak": "Deylemi, Müsned",
    },
    "166. Hakkı Savunmaktan Korkmamak": {
        "ayet": "Nerede olursanız olun hakikati savunmaktan çekinmeyin...",
        "ayet_sure": "Nisa Suresi, 135. Ayet",
        "hadis": "İnsanların korkusu, hakikati söylemekten sizi alıkoymasın.",
        "hadis_kaynak": "Tirmizi, Fiten, 26",
    },
    "167. Mazluma Dinine Bakmaksızın Yardım Etmek": {
        "ayet": "...Kim bir insanı (haksız yere) kurtarırsa, bütün insanları kurtarmış gibi olur.",
        "ayet_sure": "Maide Suresi, 32. Ayet",
        "hadis": "Mazluma dinine bakılmaksızın yardım ediniz.",
        "hadis_kaynak": "Beyhaki, Sünen",
    },
    "168. Yetim ve Öksüzleri Barındırmak": {
        "ayet": "...Sana yetimler hakkında soruyorlar. De ki: 'Onların işlerini düzeltmek hayırlıdır.'",
        "ayet_sure": "Bakara Suresi, 220. Ayet",
        "hadis": "Evinde bir yetime bakıp onu yedirip içiren kimseyi Allah cennetine koyar.",
        "hadis_kaynak": "Tirmizi, Birr, 14",
    },
    "169. Kimsesizlere Sahip Çıkmak": {
        "ayet": "Yetime katiyen kahretme (ezme); isteyen kimseyi de azarlama.",
        "ayet_sure": "Duha Suresi, 9-10. Ayetler",
        "hadis": "Dul ve kimsesizlere yardım eden kimse, Allah yolunda cihad eden veya gündüz oruç tutup gece namaz kılan gibidir.",
        "hadis_kaynak": "Buhari, Nafakat, 1",
    },
    "170. Engellilere Kolaylık Sağlamak": {
        "ayet": "Kör için güçlük yoktur, topal için güçlük yoktur, hasta için de güçlük yoktur...",
        "ayet_sure": "Nur Suresi, 61. Ayet",
        "hadis": "Gözleri görmeyen birine rehberlik etmen, yoldan taşı dikenin kaldırılması sadakadır.",
        "hadis_kaynak": "Buhari, Edeb, 34",
    },
    "171. Yaşlıların Bakımı ve Gözetimi": {
        "ayet": "...Ana babaya iyi davranın...",
        "ayet_sure": "İsra Suresi, 23. Ayet",
        "hadis": "İhtiyarlamış ana babasına yetişip de onların rızasını kazanarak cenneti hak edemeyen kimsenin burnu sürtülsün.",
        "hadis_kaynak": "Müslim, Birr, 9",
    },
    "172. Çocukların Psikolojik Hakları": {
        "ayet": "Çocuklarınızı fakirlik korkusuyla öldürmeyin; onlara da bize de rızık veren biziz...",
        "ayet_sure": "En'am Suresi, 151. Ayet",
        "hadis": "Çocuklarınıza ikram edin ve onların ahlakını güzelleştirin.",
        "hadis_kaynak": "İbn Mace, Edeb, 3",
    },
    "173. Kadın Haklarına Riayet Etmek": {
        "ayet": "...Kadınlarla iyi geçinin...",
        "ayet_sure": "Nisa Suresi, 19. Ayet",
        "hadis": "Kadınlara ancak asil kimseler değer verir; onlara ancak kötü kimseler horgörür.",
        "hadis_kaynak": "Tirmizi, Rada, 11",
    },
    "174. Şiddetsiz Aile Düzeni": {
        "ayet": "Onlarla güzellikle geçinin...",
        "ayet_sure": "Nisa Suresi, 19. Ayet",
        "hadis": "Sakın hanımlarınızı köle döver gibi dövmeyin.",
        "hadis_kaynak": "Buhari, Nikah, 93",
    },
    "175. Komşunun Evladına Şefkat": {
        "ayet": "Yakın komşuya ve uzak komşuya iyi davranın...",
        "ayet_sure": "Nisa Suresi, 36. Ayet",
        "hadis": "Komşusu açken tok yatan bizden değildir.",
        "hadis_kaynak": "Hakim, Müstedrek",
    },
    "176. Yolculara İkram ve İstimdat": {
        "ayet": "Yolcuya, yoksula hakkını ver...",
        "ayet_sure": "İsra Suresi, 26. Ayet",
        "hadis": "Yolcuya yardım etmek ve onun sıkıntısını gidermek sadakadır.",
        "hadis_kaynak": "Müslim, Hac, 412",
    },
    "177. Yoldaki Engelleri Kaldırmak": {
        "ayet": "...Her ne hayır işlerseniz Allah onu bilir.",
        "ayet_sure": "Bakara Suresi, 197. Ayet",
        "hadis": "Yoldan rahatsız edici bir şeyi (taş, diken vb.) kaldırmak sadakadır.",
        "hadis_kaynak": "Buhari, Edeb, 34",
    },
    "178. Ağaç Kesmemek ve Yeşili Korumak": {
        "ayet": "O, gökten su indirendir... Çeşitli bitkiler bitirdik...",
        "ayet_sure": "En'am Suresi, 99. Ayet",
        "hadis": "Haksız yere meyveli bir ağacı kesenin Allah başını ateşe eğsin.",
        "hadis_kaynak": "Ebu Davud, Edeb, 158",
    },
    "179. Hayvanlara Eziyet Etmemek": {
        "ayet": "...Yeryüzünde yürüyen her hayvan bir ümmettir.",
        "ayet_sure": "En'am Suresi, 38. Ayet",
        "hadis": "Bir kedi yüzünden cehenneme giren bir kadın vardır; onu hapsetmiş, ne yedirmiş ne de yerdeki haşaratı yemesine izin vermiştir.",
        "hadis_kaynak": "Buhari, Enbiya, 54",
    },
    "180. Sokak Hayvanlarını Beslemek": {
        "ayet": "Yeryüzünde hiçbir canlı yoktur ki rızkı Allah'a ait olmasın.",
        "ayet_sure": "Hud Suresi, 6. Ayet",
        "hadis": "Her canlıya yapılan iyilikte (yaş ciğere yapılan yardımda) sevap vardır.",
        "hadis_kaynak": "Buhari, Müsakat, 9",
    },
    "181. Suyu Kirletmemek ve Korumak": {
        "ayet": "...Her canlı şeyi sudan yarattık...",
        "ayet_sure": "Enbiya Suresi, 30. Ayet",
        "hadis": "Sakın durgun veya akarsuya idrar etmeyin, sonra oradan abdest alırsınız (hastalık kaparsınız).",
        "hadis_kaynak": "Nesai, Taharet, 44",
    },
    "182. Hava ve Çevre Kirliliğinden Kaçınmak": {
        "ayet": "Yeryüzünü ıslah ettikten sonra orada bozgunculuk yapmayın...",
        "ayet_sure": "A'raf Suresi, 85. Ayet",
        "hadis": "Lanete sebep olan iki şeyden sakının: İnsanların yollarına veya gölgelendikleri yerlere defhdetmek (kirletmek).",
        "hadis_kaynak": "Müslim, Taharet, 68",
    },
    "183. Gürültü Kirliliği ve Komşu Rahatsızlığı": {
        "ayet": "...Yürüyüşünde orta yolu tut, sesini alçalt...",
        "ayet_sure": "Lokman Suresi, 19. Ayet",
        "hadis": "Komşusu zararından emin olmayan kimse cennete giremez.",
        "hadis_kaynak": "Müslim, İman, 73",
    },
    "184. Trafik Kurallarına Uymak": {
        "ayet": "...Kendi ellerinizle kendinizi tehlikeye atmayın...",
        "ayet_sure": "Bakara Suresi, 195. Ayet",
        "hadis": "Yolun hakkını verin! Yolun hakkı: Gözü sakınmak, insanları rahatsız etmekten kaçınmak, selam almak ve iyiliği emretmektir.",
        "hadis_kaynak": "Buhari, Mezalim, 22",
    },
    "185. Başkasının Hakkına Tecavüz Etmemek": {
        "ayet": "Aranızda mallarınızı haksızlıkla yemeyin...",
        "ayet_sure": "Bakara Suresi, 188. Ayet",
        "hadis": "Kim birinin hakkını gasbederse, kıyamet gününde boynuna yedi kat yerin vebalı dolandırılır.",
        "hadis_kaynak": "Buhari, Mezalim, 13",
    },
    "186. Kuyruklarda ve Sıralarda Hak Gözetmek": {
        "ayet": "Şüphesiz Allah adaletle davranmayı sever.",
        "ayet_sure": "Hucurat Suresi, 9. Ayet",
        "hadis": "İnsanların haklarına saygı göstermek ve sıraya riayet etmek ahlaktandır.",
        "hadis_kaynak": "Tirmizi, Birr, 62",
    },
    "187. Alışverişte Hak Geçirmemek": {
        "ayet": "Ölçüyü tam yapın, eksultanlardan olmayın.",
        "ayet_sure": "Şuara Suresi, 181. Ayet",
        "hadis": "Alışverişte dürüst olan kimse bol rızıkla mükafatlandırılır.",
        "hadis_kaynak": "İbn Mace, Ticaret, 5",
    },
    "188. Ödünç Alınan Eşyayı Korumak": {
        "ayet": "Allah size emanetleri ehline vermenizi emreder...",
        "ayet_sure": "Nisa Suresi, 58. Ayet",
        "hadis": "Emanet edilen malın korunması ve sahibine eksiksiz iadesi gerekir.",
        "hadis_kaynak": "Ebu Davud, Buyu, 82",
    },
    "189. Emanet Verilen Malı Zamanında İade Etmek": {
        "ayet": "...Sana emanet bırakılan malı koru.",
        "ayet_sure": "Nisa Suresi, 58. Ayet",
        "hadis": "Sana emanet verene ihanet etme, seni aldatanı sen aldatma.",
        "hadis_kaynak": "Tirmizi, Buyu, 38",
    },
    "190. Selam Verip Almak": {
        "ayet": "Bir selam ile selamlandığınızda, siz de ondan daha güzeliyle karşılık verin...",
        "ayet_sure": "Nisa Suresi, 86. Ayet",
        "hadis": "Binene yürüyen, yürüyen oturana, az olan çok olan kişiye selam versin.",
        "hadis_kaynak": "Buhari, İsti'zan, 4",
    },
    "191. Hediyeleşmenin Önemi": {
        "ayet": "...Sevdiğiniz şeylerden infak edinceye kadar iyiliğe eremezsiniz...",
        "ayet_sure": "Al-i İmran Suresi, 92. Ayet",
        "hadis": "Hediyeleşin; çünkü hediye kalpteki kinleri giderir.",
        "hadis_kaynak": "Tirmizi, Velâ ve Hibe, 6",
    },
    "192. Tatlı Dilli Olmak": {
        "ayet": "...İnsanlara güzel söz söyleyin...",
        "ayet_sure": "Bakara Suresi, 83. Ayet",
        "hadis": "Yarım hurma ile de olsa cehennem ateşinden korunun; onu da bulamazsanız tatlı bir sözle korunun.",
        "hadis_kaynak": "Buhari, Zekat, 9",
    },
    "193. İnsanları Tebessümle Karşılamak": {
        "ayet": "...Rahmetinden dolayı onları yumuşak huylu kıldın...",
        "ayet_sure": "Al-i İmran Suresi, 159. Ayet",
        "hadis": "Din kardeşini tebessümle karşılaman sadakadır.",
        "hadis_kaynak": "Tirmizi, Birr, 36",
    },
    "194. Kusurları Örtmek (Settar Olmak)": {
        "ayet": "Kim bir müminin ayıbını örterse, Allah da dünya ve ahirette onun ayıplarını örter.",
        "ayet_sure": "Müslim Şerhi (Hadis Kaynağı)",
        "hadis_kaynak": "Müslim, Birr, 72",
        "hadis": "Kim dünyada bir kulun ayıbını örterse, Allah da kıyamet günü onun ayıbını örter.",
    },
    "195. Ayıp ve Kusur Araştırmamak": {
        "ayet": "...Birbirinizin kusurunu aramayın...",
        "ayet_sure": "Hucurat Suresi, 12. Ayet",
        "hadis": "Ey diliyle iman edip kalbine iman girmemiş olanlar! Müslümanların gıybetini yapmayın ve onların kusurlarını araştırmayın.",
        "hadis_kaynak": "Ebu Davud, Edeb, 35",
    },
    "196. Hüsn-ü Zan Sahibi Olmak": {
        "ayet": "Ey iman edenler! Zannın birçoğundan sakının; çünkü zannın bir kısmı günahtır...",
        "ayet_sure": "Hucurat Suresi, 12. Ayet",
        "hadis": "Hüsn-ü zan (iyi düşünmek) güzel bir ibadettir.",
        "hadis_kaynak": "Ebu Davud, Edeb, 81",
    },
    "197. Suizandan (Kötü Zan) Kaçınmak": {
        "ayet": "...Zannın bir kısmı günahtır...",
        "ayet_sure": "Hucurat Suresi, 12. Ayet",
        "hadis": "Zandan sakının; çünkü zan sözlerin en yalanıdır. İnsanların gizli hallerini araştırmayın.",
        "hadis_kaynak": "Buhari, Edeb, 57",
    },
    "198. Haset Etmemek": {
        "ayet": "...Yoksa onlar, Allah'ın lütfundan insanlara verdiği şeyleri kıskanıyorlar mı?",
        "ayet_sure": "Nisa Suresi, 54. Ayet",
        "hadis": "Birbirinize haset etmeyin, birbirinize kin beslemeyin, birbirinize sırt çevirmeyin. Allah'ın kulları kardeşler olun.",
        "hadis_kaynak": "Buhari, Edeb, 57",
    },
    "199. Kin ve Düşmanlığı Sürdürmemek": {
        "ayet": "İyilikle kötülük bir olmaz. Sen kötülüğü en güzel olanla sav; o zaman seninle aranızda düşmanlık bulunan kişinin sanki sıcak bir dost olduğunu görürsün.",
        "ayet_sure": "Fussilet Suresi, 34. Ayet",
        "hadis": "Bir müslümanın din kardeşine üç günden fazla küs durması helal değildir.",
        "hadis_kaynak": "Buhari, Edeb, 62",
    },
    "200. Kardeşlik ve Barış İçinde Yaşamak": {
        "ayet": "Müminler ancak kardeştirler. Öyleyse kardeşlerinizin arasını bulun ve Allah'tan sakının ki rahmete nail olasınız.",
        "ayet_sure": "Hucurat Suresi, 10. Ayet",
        "hadis": "Ey Allah'ın kulları, kardeş olun!",
        "hadis_kaynak": "Müslim, Birr, 30",
    }
}

# Konu başlıkları listesi
konu_listesi = list(VERITABANI.keys())

# --- KULLANICI ARAYÜZÜ (SOL SÜTUN & SAĞ SÜTUN) ---
sol_sutun, sag_sutun = st.columns([1, 2], gap="large")

with sol_sutun:
    st.subheader("📌 Konu Seçim Menüsü")
    st.markdown(
        f"Toplam **{len(VERITABANI)}** adet konu arasından seçim yapabilirsiniz:"
    )

    arama_terimi = st.text_input("🔍 200 Konu İçinde Ara:", "")

    filtrelenmis_konular = [
        k for k in konu_listesi if arama_terimi.lower() in k.lower()
    ]

    if not filtrelenmis_konular:
        st.warning("Aradığınız kriterlere uygun konu bulunamadı.")
        secilen_konu = konu_listesi[0]
    else:
        secilen_konu = st.selectbox(
            "Listeden Konu Seçiniz:", filtrelenmis_konular, index=0
        )

with sag_sutun:
    st.subheader("📑 Seçilen Konu Detayları")

    with st.container(border=True):
        st.markdown(f"### 🎯 Seçilen Konu: **{secilen_konu}**")
        st.markdown("---")

        veri = VERITABANI[secilen_konu]

        st.markdown("#### 📜 İlgili Ayet")
        st.info(f"\"{veri['ayet']}\"")
        st.caption(f"📌 **Kaynak / Sure:** {veri['ayet_sure']}")

        st.markdown("")

        st.markdown("#### 💡 İlgili Hadis")
        st.success(f"\"{veri['hadis']}\"")
        st.caption(f"📌 **Kaynak / Hadis Kitabı:** {veri['hadis_kaynak']}")

# --- SAYFA ALT BİLGİSİ ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2026 Konulu Ayet ve Hadis Bilgi Portalı (200 Konu) | Açık Kaynak Kodlu Bilgilendirme Yazılımı</div>",
    unsafe_allow_html=True,
)