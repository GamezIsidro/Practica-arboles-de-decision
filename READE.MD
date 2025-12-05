# **Clasificación con Árbol de Decisión — Wine Dataset**

Este proyecto implementa un modelo de clasificación utilizando un **Árbol de Decisión** aplicado al conjunto de datos *Wine* de Scikit-Learn.  
El objetivo es comparar distintos niveles de profundidad del árbol y analizar cómo cambian la precisión y las reglas generadas.

---

# **Resultados del Modelo**

A continuación se muestran los resultados obtenidos en tres configuraciones distintas del parámetro max_depth.

---

# **1. Árbol con max_depth = 2 (modelo final solicitado)**

Este es el modelo principal de la práctica, ya que un árbol limitado facilita la explicación y genera reglas simples.

### **Precisión obtenida**

0.8611111111111112


### **Reglas generadas**

|--- proline <= 755.00
| |--- flavanoids <= 1.24
| | |--- class: 2
| |--- flavanoids > 1.24
| | |--- class: 1
|--- proline > 755.00
| |--- flavanoids <= 2.17
| | |--- class: 2
| |--- flavanoids > 2.17
| | |--- class: 0


### **Interpretación**
Este árbol es muy compacto y utiliza solo dos características principales:

**proline**  
**flavanoids**

Con solo estas variables es capaz de separar las 3 clases.  
Aunque su precisión es inferior a los árboles más profundos, es **muy interpretables**.

---

# **Árbol con max_depth = 500 (árbol muy profundo — prueba)**

Este modelo fue una prueba usando un árbol casi sin restricciones.

### **Precisión obtenida**

0.8888888888888888


### **Reglas generadas**

|--- proline <= 755.00
| |--- flavanoids <= 1.24
| | |--- color_intensity <= 3.56
| | | |--- class: 1
| | |--- color_intensity > 3.56
| | | |--- class: 2
| |--- flavanoids > 1.24
| | |--- color_intensity <= 7.30
| | | |--- malic_acid <= 3.92
| | | | |--- class: 1
| | | |--- malic_acid > 3.92
| | | | |--- color_intensity <= 3.58
| | | | | |--- class: 1
| | | | |--- color_intensity > 3.58
| | | | | |--- class: 0
| | |--- color_intensity > 7.30
| | | |--- class: 2
|--- proline > 755.00
| |--- flavanoids <= 2.17
| | |--- malic_acid <= 2.08
| | | |--- class: 1
| | |--- malic_acid > 2.08
| | | |--- class: 2
| |--- flavanoids > 2.17
| | |--- color_intensity <= 3.06
| | | |--- class: 1
| | |--- color_intensity > 3.06
| | | |--- class: 0


### **Interpretación**
El árbol profundo usa muchas más condiciones y variables.  
Aunque identifica más detalles, no mejora demasiado la precisión, lo que indica que el dataset es fácil de separar.

---

# 3. Árbol con max_depth = None (sin límite)**

Este modelo permite que el árbol crezca completamente.

### **Precisión obtenida**

0.9166666666666666


### **Reglas generadas**

|--- proline <= 755.00
| |--- flavanoids <= 1.24
| | |--- hue <= 0.93
| | | |--- class: 2
| | |--- hue > 0.93
| | | |--- class: 1
| |--- flavanoids > 1.24
| | |--- hue <= 0.64
| | | |--- class: 2
| | |--- hue > 0.64
| | | |--- alcohol <= 13.17
| | | | |--- class: 1
| | | |--- alcohol > 13.17
| | | | |--- color_intensity <= 4.08
| | | | | |--- class: 1
| | | | |--- color_intensity > 4.08
| | | | | |--- class: 0
|--- proline > 755.00
| |--- flavanoids <= 2.17
| | |--- flavanoids <= 0.90
| | | |--- class: 2
| | |--- flavanoids > 0.90
| | | |--- class: 1
| |--- flavanoids > 2.17
| | |--- magnesium <= 147.00
| | | |--- class: 0
| | |--- magnesium > 147.00
| | | |--- class: 1


### **Interpretación**
Este árbol toma en cuenta aún más atributos como:

- **hue**
- **alcohol**
- **magnesium**

y genera muchas más decisiones.  
Sin embargo, el aumento en precisión respecto al árbol pequeño es solo moderado.

---

# **Opiniones sobre los resultados**

- Un árbol pequeño (max_depth=2) es muy fácil de interpretar, aunque su precisión es menor.  
- Árboles más grandes identifican más detalles, pero no necesariamente mejoran mucho la exactitud.  
- El dataset parece separarse con pocas reglas, lo que significa que sus clases están bien definidas.  
- Los resultados son consistentes y muestran un buen equilibrio entre interpretabilidad y rendimiento.

---

# **¿El dataset Wine cumple con los requisitos para utilizar un Árbol de Decisión?**

### **Sí, cumple completamente.**

---

# **Justificación**

El dataset Wine es ideal para este tipo de modelo porque:

- Sus características son numéricas, claras y comparables.  
- Contiene tres clases bien definidas.  
- No presenta datos faltantes.  
- Las relaciones entre variables son reconocibles por un árbol.  
- Es un ejemplo clásico para clasificación supervisada.

---

# **Características **

### **Características:**
El árbol utiliza las 13 propiedades químicas del vino, tales como:

- alcohol  
- malic_acid  
- ash  
- alcalinidad de cenizas  
- magnesio  
- total_phenols  
- flavanoids  
- color_intensity  
- hue  
- prolina  
- od280/od315  


# **Conclusión**

El conjunto de datos Wine se ajusta perfectamente al uso de Árboles de Decisión.  
La profundidad del árbol influye en la complejidad de las reglas, pero incluso modelos poco profundos logran buen rendimiento.  
Esto demuestra que es un dataset bien estructurado y adecuado para problemas de clasificación.