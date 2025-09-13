import streamlit as st
import time

# ============================
# Configuración
# ============================
RESPUESTA_CORRECTA = "seguridad"
MENSAJE_EXITO = "🔓 Información recuperada: Los Yakuza se mueven a Nagasaki."
MENSAJE_FRACASO = "❌ Se perdió la información."
TEXTO_CIFRADO = "5314"  # ejemplo (Murciélago)
TIEMPO_TOTAL = 30  # segundos

# ============================
# Estados
# ============================
if "resultado" not in st.session_state:
    st.session_state.resultado = ""
if "activo" not in st.session_state:
    st.session_state.activo = False
if "tiempo_inicio" not in st.session_state:
    st.session_state.tiempo_inicio = None

# ============================
# Interfaz
# ============================
st.title("🕵️ Crisis de Descifrado - Centro de Mando")

st.markdown(
    "### Desencripta la clave antes de que el tiempo termine ⏳\n"
    "Inicia el reto y tendrás un **temporizador en vivo**. "
    "Si logras descifrar, ganarás información clave. "
    "Si no, toda la información se perderá."
)

st.markdown(f"## 🔐 Clave cifrada: **{TEXTO_CIFRADO}**")

entrada = st.text_input("✍️ Ingresa tu respuesta:", "")

col1, col2 = st.columns([1, 1])
with col1:
    if st.button("▶️ Iniciar Reto"):
        st.session_state.tiempo_inicio = time.time()
        st.session_state.activo = True
        st.session_state.resultado = ""

with col2:
    if st.button("✅ Verificar") and st.session_state.activo:
        if entrada.lower() == RESPUESTA_CORRECTA:
            st.session_state.resultado = MENSAJE_EXITO
        else:
            st.session_state.resultado = MENSAJE_FRACASO
        st.session_state.activo = False

# ============================
# Temporizador dinámico
# ============================
if st.session_state.activo and st.session_state.tiempo_inicio:
    placeholder = st.empty()
    for i in range(TIEMPO_TOTAL, -1, -1):
        if not st.session_state.activo:  # si ya verificaron
            break
        placeholder.markdown(f"### ⏱️ Tiempo restante: **{i} s**")
        time.sleep(1)
    else:
        # Si llega a 0 sin verificar
        if st.session_state.resultado == "":
            st.session_state.resultado = MENSAJE_FRACASO
            st.session_state.activo = False
    st.rerun()

# ============================
# Resultado final
# ============================
if st.session_state.resultado:
    if "recuperada" in st.session_state.resultado:
        st.success(st.session_state.resultado)
    else:
        st.error(st.session_state.resultado)
