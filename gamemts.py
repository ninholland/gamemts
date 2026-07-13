import streamlit as st

# Mengatur tampilan halaman
st.set_page_config(page_title="Game Sortir Komentar", page_icon="📱", layout="centered")

# Judul Aplikasi
st.title("🎮 Detektif Digital: Kritik vs Bullying")
st.write("Sosialisasi Literasi Digital & Anti-Cyberbullying - MTs Takhasus Al-Muhibbin[span_1](start_span)[span_1](end_span)")
st.markdown("---")

# Basis data 8 komentar beserta analisis logikanya
daftar_komentar = [
    {
        "teks": "Suaramu di video agak kekecilan, besok volumenya dibesarkan sedikit ya biar lebih enak didengar.", 
        "kategori": "Kritik Sehat",
        "alasan": "Fokus pada hal teknis (volume) dan memberikan solusi agar karya selanjutnya lebih baik, tanpa menyerang pribadi."
    },
    {
        "teks": "Muka pas-pasan aja gaya-gayaan difoto, udah gitu jerawatan lagi. Sadar diri dong.", 
        "kategori": "Cyberbullying",
        "alasan": "Ini adalah body shaming. Komentar ini murni menyerang fisik (ranah personal) yang bisa merusak benteng emosional korban[span_2](start_span)[span_2](end_span)."
    },
    {
        "teks": "Idenya bagus, tapi sumber informasinya sepertinya kurang pas. Coba cek lagi di buku paket halaman 20.", 
        "kategori": "Kritik Sehat",
        "alasan": "Komentar ini objektif. Menunjukkan letak kesalahan secara sopan dan mengarahkan ke sumber informasi yang benar."
    },
    {
        "teks": "Dasar caper! Mentang-mentang orang tuanya baru kirim uang, semua aja dipamerin. Norak!", 
        "kategori": "Cyberbullying",
        "alasan": "Menyerang latar belakang keluarga dan melabeli dengan kata-kata kasar (caper, norak) dengan tujuan mempermalukan."
    },
    {
        "teks": "Tulisannya terlalu panjang dan tidak ada spasinya, mataku jadi pusing membacanya. Mungkin bisa dipisah per paragraf.", 
        "kategori": "Kritik Sehat",
        "alasan": "Mengevaluasi hasil karya (tulisan) agar lebih mudah dibaca oleh orang lain, bukan menjatuhkan mental penulisnya."
    },
    {
        "teks": "Gak usah sok asik komen di sini deh, gak ada yang mau temenan sama anak aneh kayak kamu.", 
        "kategori": "Cyberbullying",
        "alasan": "Komentar ini bertujuan untuk mengucilkan secara sosial (social exclusion), yang merupakan bentuk perundungan psikologis parah[span_3](start_span)[span_3](end_span)."
    },
    {
        "teks": "Fotonya agak gelap, kalau ambil gambar pas siang hari di luar ruangan pasti hasilnya jauh lebih keren.", 
        "kategori": "Kritik Sehat",
        "alasan": "Memberikan saran konstruktif mengenai pencahayaan tanpa menggunakan kata-kata yang merendahkan."
    },
    {
        "teks": "Udah salah ketik, sok tahu pula. Hapus aja postingannya bikin malu sekolah kita aja.", 
        "kategori": "Cyberbullying",
        "alasan": "Menggunakan rasa malu (shaming) sebagai senjata untuk menjatuhkan mental, bukan untuk memperbaiki kesalahan[span_4](start_span)[span_4](end_span)."
    }
]

# Inisialisasi variabel di session_state agar data tidak hilang saat layar direfresh
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'sudah_dijawab' not in st.session_state:
    st.session_state.sudah_dijawab = False
if 'jawaban_terakhir' not in st.session_state:
    st.session_state.jawaban_terakhir = ""

# Menjalankan game selama masih ada komentar tersisa
if st.session_state.index < len(daftar_komentar):
    komentar_sekarang = daftar_komentar[st.session_state.index]
    
    st.write(f"### Kasus {st.session_state.index + 1} dari {len(daftar_komentar)}")
    
    # Menampilkan kotak komentar
    st.info(f"💬 *Komentar:\n\n{komentar_sekarang['teks']}*")
    
    # Layout tombol
    col1, col2 = st.columns(2)
    
    # Hanya aktifkan tombol jika belum dijawab
    if not st.session_state.sudah_dijawab:
        with col1:
            if st.button("🟢 Kritik Sehat", use_container_width=True):
                st.session_state.jawaban_terakhir = "Kritik Sehat"
                st.session_state.sudah_dijawab = True
                st.rerun()
        with col2:
            if st.button("🔴 Cyberbullying", use_container_width=True):
                st.session_state.jawaban_terakhir = "Cyberbullying"
                st.session_state.sudah_dijawab = True
                st.rerun()
                
    # Bagian evaluasi logika (muncul setelah tombol diklik)
    if st.session_state.sudah_dijawab:
        st.markdown("---")
        # Audit logika: Apakah pilihan siswa benar?
        if st.session_state.jawaban_terakhir == komentar_sekarang["kategori"]:
            st.success("✅ *ANALISIS BENAR!*")
            # Tambah skor hanya jika baru pertama kali menebak benar (opsional)
            st.session_state.skor += 1
        else:
            st.error(f"❌ *ANALISIS KELIRU.* Jawaban yang tepat adalah *{komentar_sekarang['kategori']}*.")
            
        # Penjelasan mendalam per langkah logika
        st.write("*Penjelasan Logika:*")
        st.write(komentar_sekarang['alasan'])
        
        # Tombol untuk lanjut ke komentar berikutnya
        if st.button("Lanjut ke Kasus Berikutnya ➡️"):
            st.session_state.index += 1
            st.session_state.sudah_dijawab = False
            st.session_state.jawaban_terakhir = ""
            st.rerun()

# Layar penutup jika semua komentar sudah dianalisis
else:
    st.balloons()
    st.success("🏁 *SESI SOSIALISASI SELESAI!*")
    st.write(f"Skor Akhir Kelompok: *{st.session_state.skor} dari {len(daftar_komentar)}*")
    
    st.write("Ingat, kedewasaan digital dibuktikan dengan kemampuan menahan diri dari mengetik komentar yang menyakiti orang lain[span_5](start_span)[span_5](end_span).")
    
    # Tombol reset
    if st.button("🔄 Ulangi Game"):
        st.session_state.index = 0
        st.session_state.skor = 0
        st.session_state.sudah_dijawab = False
        st.session_state.jawaban_terakhir = ""
        st.rerun()
