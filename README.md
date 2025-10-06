# 🐍 Actividad 5 - Validaciones y bucles

Actividad de Lenguaje de programación I, de la carrera de ingeniería de software, segundo semestre. 

5 ejercicios practicos implementando validaciones, bucles y condicionales

## 📘 Información del Proyecto

- **Autor:** Katherynn Gomez 
- **GitHub:** [@KoShLaBs](https://github.com/KoShLaBs)
- **Profesor:** Ing. Johan Manuel Gordillo Mesa
- **Materia:** Lenguaje de Programación
- **Fecha:** 05 de octubre de 2025
- **Repositorio:** [ProgrammingLanguageKatG]  
- **Rama actual:** `actividadcinco`  

---

## 6️⃣ Cajero automático con PIN y menú

**Objetivo:**  
Simular operaciones básicas de un cajero automático con verificación de PIN.

**Entradas:**  
- PIN correcto predefinido (por ejemplo, 1234).  
- El usuario tiene **3 intentos** (`while`) para ingresar el PIN correctamente.  

**Menú disponible (en bucle):**  
1) Depositar  
2) Retirar  
3) Consultar saldo  
4) Salir  

**Reglas:**  
- Depósitos y retiros deben ser mayores a 0.  
- Solo permitir retiro si el **saldo disponible** lo permite.  
- Si el PIN es incorrecto 3 veces, bloquear el acceso.  

**Salida esperada:**  
- Historial de operaciones realizadas.  
- Saldo final de la cuenta.

---

## 7️⃣ Descuentos en tienda (membresía + cupón)

**Objetivo:**  
Calcular el total a pagar en una tienda aplicando descuentos según condiciones comerciales.

**Entradas:**  
- Precio base del producto.  
- ¿Tiene membresía? (`s/n`)  
- ¿Tiene cupón? (`s/n`)  
- ¿El producto está en oferta? (`s/n`)  

**Reglas de descuento:**  
- Membresía aplica **10%** de descuento.  
- Cupón aplica **15%**, pero **solo si el producto NO está en oferta**.  
- Si tiene cupón y está en oferta, se aplica **solo la oferta** (no se combinan).  
- Si el **total final supera $300.000** y el cliente tiene membresía, se incluye **envío gratis**.  

**Salida esperada:**  
- Precio total a pagar después de descuentos.  
- Mensaje si el pedido incluye envío gratis.

---

## 8️⃣ Consumo eléctrico mensual

**Objetivo:**  
Leer el consumo diario en kWh por **30 días** y calcular el costo total de la factura.

**Entradas:**  
- 30 lecturas diarias (una por día).  
- Cada valor debe ser **mayor o igual a 0**.

**Tarifa según consumo total mensual (en kWh):**  
- Hasta 200 → **$600/kWh**  
- De 201 a 500 → **$700/kWh**  
- Más de 500 → **$850/kWh**

**Extras:**  
- Contar cuántos días tuvieron consumo **mayor a 25 kWh**.  
- Si el consumo total supera **600 kWh** **y** hubo **5 o más días de alto consumo**, mostrar advertencia: `"Recomendación: Auditoría de consumo"`.

**Salida esperada:**  
- Consumo total del mes.  
- Costo total a pagar.  
- Número de días de alto consumo.  
- Mensaje de advertencia si aplica.

---

## 9️⃣ Entregas de paquetería por franja horaria

**Objetivo:**  
Registrar entregas realizadas, con máximo **10 entregas** o hasta una condición de corte anticipado.

**Entradas por entrega:**  
- Hora prometida (entero entre 0 y 23)  
- Hora real de entrega (0 a 23)  
- ¿Cliente VIP? (`s/n`)  

**Reglas:**  
- Una entrega es considerada "a tiempo" si:
  - `hora_real <= hora_prometida`  
  - o si es cliente VIP y entrega es **hasta 1 hora después** de lo prometido.
- Si se alcanzan **10 entregas**, se termina.  
- Si el usuario indica que son las **20:00** y **faltan 2 entregas**, terminar con `break` (no hay tiempo).

**Salida esperada:**  
- Número de entregas **a tiempo**.  
- Número de entregas **tardías**.  
- **Tasa de cumplimiento** (entregas a tiempo / total de entregas).

---

## 🔟 Turnero de banco con saltos

**Objetivo:**  
Emitir turnos numerados del 1 al `N`, omitiendo algunos por reglas de negocio.

**Entradas:**  
- Número final `N` de turnos posibles.  

**Reglas para omitir un turno (usar `continue`):**  
- Si el número es **múltiplo de 13**  
- Si el número **termina en 4**  

**Condiciones de corte (usar `break`):**  
- Si se han emitido **50 turnos válidos**  
- O si se alcanza un turno considerado “de cierre” (por ejemplo, número 100)

**Salida esperada:**  
- Lista de turnos servidos (válidos).  
- Cuántos turnos fueron **omitidos**.
---

## 🔧 Clonar y usar este repositorio

```bash
# Clonar el repositorio
git clone https://github.com/KoShLaBs/ProgrammingLanguageKatG.git

# Entrar al directorio del proyecto
cd ProgrammingLanguageKatG

# Cambiar a la rama de ejercicios
git checkout actividadcinco