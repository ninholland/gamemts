import streamlit as st
import random

st.set_page_config(page_title="Anti-Narkoba Puzzle", layout="centered")

st.title("🧩 Game Susun Kata: Edukasi Anti-Narkoba & Rokok")

# Bank Soal: Kumpulan slogan edukasi yang masing-masing terdiri dari tepat 9 kata
SOAL_LIST = [
    ["Katakan", "tidak", "pada", "narkoba", "demi", "masa", "depan", "yang", "cerah"],
    ["Hindari", "rokok", "dan", "narkoba", "sekarang", "demi", "tubuh", "yang", "sehat"],
    ["Hidup", "menjadi", "lebih", "sehat", "tanpa", "asap", "rokok", "dan", "narkoba"],
    ["Jagalah", "tubuh", "sehat", "kita", "dari", "bahaya", "rokok", "dan", "narkoba"]
]

# Inisialisasi State Game
if 'q_idx' not in st.session_state:
    st.session_state.q_idx = 0
    target = SOAL_LIST[st.session_state.q_idx].copy()
    scramble = target.copy()
    while scramble == target:
        random.shuffle(scramble)
    st.session_state.grid = scramble
    st.session_state.selected = None
    st.session_state.moves = 0
    st.session_state.done = False

# Fungsi untuk ganti soal atau acak ulang
def ganti_soal_atau_reset():
    st.session_state.q_idx = (st.session_state.q_idx + 1) % len(SOAL_LIST)
    target = SOAL_LIST[st.session_state.q_idx].copy()
    scramble = target.copy()
    while scramble == target:
        random.shuffle(scramble)
    st.session_state.grid = scramble
    st.session_state.selected = None
    st.session_state.moves = 0
    st.session_state.done = False

# Tampilan Header Informasi Soal
st.write(f"### 📋 Tantangan Ke: {st.session_state.q_idx + 1} dari {len(SOAL_LIST)}")
st.button("🔄 Lanjut Soal Berikutnya / Reset", on_click=ganti_soal_atau_reset)

# Gabungkan list menjadi kalimat utuh untuk petunjuk target
target_kalimat = " ".join(SOAL_LIST[st.session_state.q_idx])
st.info(f"💡 *Misi Kasih:* Susun ubin kata acak di bawah agar menjadi kalimat utuh:\n\n*\"{target_kalimat}\"*")

st.write(f"🔢 Jumlah Langkah: *{st.session_state.moves}*")

# Notifikasi ketika berhasil menyelesaikan puzzle
if st.session_state.done:
    st.balloons()
    st.success("🎉 LUAR BIASA! Kalimat berhasil tersusun dengan sempurna. Klik tombol di atas untuk lanjut ke tantangan berikutnya!")

st.write("---")

# Render Grid Ubin 3x3
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        idx = row * 3 + col
        word = st.session_state.grid[idx]
        
        # Penanda warna ubin yang sedang dipilih aktif
        is_selected = (st.session_state.selected == idx)
        btn_type = "primary" if is_selected else "secondary"
        
        # Kunci tombol jika puzzle sudah selesai disusun dengan benar
        disabled = st.session_state.done
        
        if cols[col].button(word, key=f"tile_{idx}", type=btn_type, disabled=disabled, use_container_width=True):
            if st.session_state.selected is None:
                st.session_state.selected = idx
                st.rerun()
            else:
                prev_idx = st.session_state.selected
                # Eksekusi pertukaran kata di dalam array grid
                st.session_state.grid[prev_idx], st.session_state.grid[idx] = st.session_state.grid[idx], st.session_state.grid[prev_idx]
                st.session_state.moves += 1
                st.session_state.selected = None
                
                # Validasi kesamaan array grid dengan target kebenaran soal
                if st.session_state.grid == SOAL_LIST[st.session_state.q_idx]:
                    st.session_state.done = True
                st.rerun()
