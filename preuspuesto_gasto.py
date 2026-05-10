import streamlit as st
import pandas as pd
import os
import json
from datetime import date

# Archivos base
CSV_FILE = "gastos.csv"
JSON_FILE = "presupuesto.json"

# Inicializar CSV si no existe
if not os.path.exists(CSV_FILE):
    df_init = pd.DataFrame(columns=["fecha","categoria","detalle","monto","forma_pago"])
    df_init.to_csv(CSV_FILE, index=False)

# Inicializar JSON si no existe
if not os.path.exists(JSON_FILE):
    presupuesto_init = {
        "Alimentación": 1500000,
        "Transporte": 700000,
        "Vivienda": 2000000,
        "Entretenimiento": 500000,
        "Otros": 400000
    }
    with open(JSON_FILE, "w") as f:
        json.dump(presupuesto_init, f, indent=4)

# --- Menú lateral ---
menu = st.sidebar.radio("Menú", ["Ver informe", "Ingresar gasto"])

# --- Ingresar gasto ---
if menu == "Ingresar gasto":
    st.header("✍️ Ingresar nuevo gasto")

    with st.form("form_gasto"):
        fecha = st.date_input("Fecha", value=date.today())
        categoria = st.selectbox("Categoría", ["Alimentación","Transporte","Vivienda","Entretenimiento","Otros"])
        detalle = st.text_input("Detalle del gasto")
        monto = st.number_input("Monto", min_value=0, step=1000)
        forma_pago = st.selectbox("Forma de pago", ["Efectivo","Tarjeta de credito","Debito","Transferencia","Nequi","Daviplata","Bre-B"])
        
        submitted = st.form_submit_button("Guardar gasto")

        if submitted:
            nuevo = pd.DataFrame([[fecha, categoria, detalle, monto, forma_pago]],
                                 columns=["fecha","categoria","detalle","monto","forma_pago"])
            df = pd.read_csv(CSV_FILE)
            df = pd.concat([df, nuevo], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            st.success("✅ Gasto registrado correctamente")

# --- Informe de gastos ---
elif menu == "Ver informe":
    st.header("📊 Informe de gastos")

    # Cargar datos
    df = pd.read_csv(CSV_FILE)
    with open(JSON_FILE) as f:
        presupuesto = json.load(f)

    if df.empty:
        st.warning("No hay gastos registrados aún.")
    else:
        # Mostrar tabla detallada
        st.subheader("📋 Detalle de gastos")
        st.dataframe(df)

        # Resumen por categoría
        total_gastos = df["monto"].sum()
        resumen = df.groupby("categoria")["monto"].sum().reset_index()
        resumen["% del total"] = (resumen["monto"] / total_gastos * 100).round(2)

        def comparar(categoria, gasto):
            if categoria in presupuesto:
                if gasto < presupuesto[categoria]:
                    return "🟡 Por debajo"
                elif gasto == presupuesto[categoria]:
                    return "✅ Dentro"
                else:
                    return "🔴 Por encima"
            else:
                return "⚪ Sin presupuesto"

        resumen["Estado vs Presupuesto"] = resumen.apply(
            lambda row: comparar(row["categoria"], row["monto"]), axis=1
        )

        st.subheader("📊 Resumen por categoría")
        st.dataframe(resumen)

        # Gráfico por categoría
        st.subheader("📈 Distribución de gastos por categoría")
        st.bar_chart(resumen.set_index("categoria")["monto"])

        # Gráfico por forma de pago
        st.subheader("💳 Distribución por forma de pago")
        forma_pago = df.groupby("forma_pago")["monto"].sum().reset_index()
        st.dataframe(forma_pago)
        st.pie_chart(forma_pago.set_index("forma_pago")["monto"])
