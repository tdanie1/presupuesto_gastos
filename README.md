# 📊 Presupuesto y Control de Gastos

Aplicación en **Streamlit** para el registro, control y conciliación de gastos personales.  
Permite ingresar gastos mediante un formulario, almacenarlos en un archivo CSV, compararlos con un presupuesto definido en JSON y visualizar informes con gráficos interactivos.

---

## 🚀 Características
- Registro de gastos con:
  - Fecha
  - Categoría
  - Detalle del gasto
  - Monto
  - Forma de pago (Efectivo, Tarjeta de crédito, Débito, Transferencia, Nequi, Daviplata, Bre-B)
- Presupuesto por categoría definido en `presupuesto.json`.
- Informe con:
  - Tabla detallada de gastos
  - Resumen por categoría (% del total y comparación con presupuesto)
  - Gráficos de barras y circulares
  - Distribución por forma de pago
- Menú lateral para alternar entre **Ingresar gasto** y **Ver informe**.

---

## 📂 Estructura del proyecto
```
presupuesto_gastos/
│
├── app.py              # Script principal de Streamlit
├── gastos.csv          # Archivo de gastos (se crea automáticamente)
├── presupuesto.json    # Archivo de presupuesto inicial
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación del proyecto
```

## ⚙️ Instalación y uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/presupuesto_gastos.git
cd presupuesto_gastos
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar en local
```bash
streamlit run app.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`.

---

## 🌐 Despliegue en Streamlit Cloud
1. Sube tu repositorio a GitHub.
2. Ve a [Streamlit Cloud](https://share.streamlit.io).
3. Conecta tu cuenta de GitHub y selecciona el repositorio.
4. Publica la aplicación.  
   Streamlit detectará automáticamente `app.py` y `requirements.txt`.

---

## 📊 Ejemplo de archivos

### `presupuesto.json`
```json
{
  "Alimentación": 1500000,
  "Transporte": 700000,
  "Vivienda": 2000000,
  "Entretenimiento": 500000,
  "Otros": 400000
}
```

### `gastos.csv`
```csv
fecha,categoria,detalle,monto,forma_pago
2026-05-01,Alimentación,Almuerzo en restaurante,200000,Efectivo
2026-05-02,Transporte,Pasaje de bus,3000,Nequi
2026-05-03,Vivienda,Pago de arriendo,2000000,Transferencia
2026-05-04,Entretenimiento,Cine,25000,Tarjeta de credito
2026-05-05,Otros,Compra útiles escolares,45000,Daviplata
```

---

## 📦 requirements.txt
```
streamlit
pandas
openpyxl
```

