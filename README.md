# Diseño y Desarrollo de una API REST en un Sistema de Gestión de Préstamos

En el contexto de un sistema de gestión de préstamos para una entidad financiera, necesitas desarrollar una API REST que permita a los usuarios autenticados crear, leer, actualizar y eliminar préstamos. La API debe usar autenticación JWT para asegurar que solo usuarios autorizados puedan acceder a las operaciones. Los préstamos tienen atributos como ID, monto, tasa de interés, fecha de vencimiento y estado. La entidad financiera requiere que la API maneje correctamente los errores y validaciones, como préstamos con montos negativos o fechas de vencimiento en el pasado.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Python FastAPI |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del Modelo de Préstamo

**Objetivo:** Definir el modelo de datos para los préstamos, incluyendo sus atributos y validaciones.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica los atributos necesarios para un préstamo.
- Define las validaciones para cada atributo (ej. monto positivo, fecha de vencimiento futura).
- Crea un modelo de datos que represente un préstamo con las validaciones definidas.

**Entregable:** Modelo de datos para préstamos con validaciones.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las restricciones de negocio para los atributos de los préstamos.
- Piensa en cómo representar las validaciones en el modelo de datos.

</details>

### Fase 2: Implementación de la API REST

**Objetivo:** Implementar los endpoints de la API REST para crear, leer, actualizar y eliminar préstamos.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Define los endpoints necesarios para las operaciones CRUD de préstamos.
- Implementa la lógica para cada endpoint, asegurando que se apliquen las validaciones definidas en la fase anterior.
- Integra la autenticación JWT para asegurar que solo usuarios autorizados puedan acceder a los endpoints.

**Entregable:** API REST con endpoints para operaciones CRUD de préstamos y autenticación JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar los errores y validaciones en cada endpoint.
- Piensa en la estructura de la respuesta para cada endpoint.

</details>

### Fase 3: Pruebas y Optimización

**Objetivo:** Realizar pruebas unitarias y de integración para asegurar la funcionalidad y rendimiento de la API.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Crea pruebas unitarias para cada endpoint, asegurando que se cumplan las validaciones y que se manejen correctamente los errores.
- Realiza pruebas de integración para asegurar que los endpoints funcionen correctamente juntos.
- Identifica y optimiza cualquier punto de rendimiento crítico en la API.

**Entregable:** Pruebas unitarias y de integración para la API REST, con optimizaciones de rendimiento identificadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo simular diferentes escenarios de uso para las pruebas.
- Piensa en cómo medir y mejorar el rendimiento de la API.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un préstamo y cuáles son sus atributos principales?
- **paraQueSirve**: ¿Para qué sirve cada atributo de un préstamo y cómo se aplican las validaciones?
- **comoSeUsa**: ¿Cómo se usan los endpoints de la API REST para las operaciones CRUD de préstamos?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir al crear, leer, actualizar o eliminar un préstamo y cómo se manejan?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación de la autenticación JWT y cómo afectan al diseño de la API?

## Criterios de Evaluacion

- Definición correcta del modelo de datos para préstamos con validaciones.
- Implementación funcional de los endpoints de la API REST con autenticación JWT.
- Pruebas unitarias y de integración que demuestren la funcionalidad y rendimiento de la API.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
