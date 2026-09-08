# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Crear una API REST con FastAPI, SQLAlchemy y autenticación JWT

### Reto
- Tema: Python FastAPI
- Seniority: junior-l1
- Tipo: practical
- Título: Diseño y Desarrollo de una API REST en un Sistema de Gestión de Préstamos
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición del Modelo de Préstamo — objetivo: Definir el modelo de datos para los préstamos, incluyendo sus atributos y validaciones. — entregable (NO resolver): Modelo de datos para préstamos con validaciones.
- Fase 2: Implementación de la API REST — objetivo: Implementar los endpoints de la API REST para crear, leer, actualizar y eliminar préstamos. — entregable (NO resolver): API REST con endpoints para operaciones CRUD de préstamos y autenticación JWT.
- Fase 3: Pruebas y Optimización — objetivo: Realizar pruebas unitarias y de integración para asegurar la funcionalidad y rendimiento de la API. — entregable (NO resolver): Pruebas unitarias y de integración para la API REST, con optimizaciones de rendimiento identificadas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional
from.database import get_db
from.security import verify_token
from.loan_model import Loan, LoanCreate, LoanUpdate

app = FastAPI()


@app.post('/loans/', response_model=Loan, dependencies=[Depends(verify_token)])
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    db_loan = Loan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


@app.get('/loans/', response_model=List[Loan], dependencies=[Depends(verify_token)])
def read_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    loans = db.query(Loan).offset(skip).limit(limit).all()
    return loans


@app.get('/loans/{loan_id}', response_model=Loan, dependencies=[Depends(verify_token)])
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    return db_loan


@app.put('/loans/{loan_id}', response_model=Loan, dependencies=[Depends(verify_token)])
def update_loan(loan_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    for key, value in loan.dict(exclude_unset=True).items():
        setattr(db_loan, key, value)
    db.commit()
    db.refresh(db_loan)
    return db_loan


@app.delete('/loans/{loan_id}', dependencies=[Depends(verify_token)])
def delete_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail='Loan not found')
    db.delete(db_loan)
    db.commit()
    return {'detail': 'Loan deleted'}

// === ARCHIVO: src/main/domain/loan_model.py ===
from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, Float, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()


class LoanCreate(BaseModel):
    amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., gt=0)
    due_date: date = Field(..., gt=date.today())
    status: str = Field(..., regex='^(active|inactive)$')


class LoanUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    interest_rate: Optional[float] = Field(None, gt=0)
    due_date: Optional[date] = Field(None, gt=date.today())
    status: Optional[str] = Field(None, regex='^(active|inactive)$')


class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)

// === ARCHIVO: src/main/infrastructure/database.py ===
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from..domain.loan_model import Base

DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

// === ARCHIVO: src/main/security/security_config.py ===
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from..domain.loan_model import Loan

SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oAuth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str = Depends(oAuth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get('sub')
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

// === ARCHIVO: src/main/tests/test_loan_routes.py ===
from fastapi.testclient import TestClient
from..main import app
from..infrastructure.database import SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from..domain.loan_model import Base, Loan

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


def test_create_loan():
    response = client.post('/loans/', json={
        'amount': 1000.0,
        'interest_rate': 5.0,
        'due_date': '2025-12-31',
        'status': 'active'
    })
    assert response.status_code == 200
    loan = response.json()
    assert loan['amount'] == 1000.0
    assert loan['interest_rate'] == 5.0
    assert loan['due_date'] == '2025-12-31'
    assert loan['status'] == 'active'


def test_read_loans():
    response = client.get('/loans/')
    assert response.status_code == 200
    loans = response.json()
    assert isinstance(loans, list)


def test_read_loan():
    response = client.get('/loans/1')
    assert response.status_code == 200
    loan = response.json()
    assert loan['id'] == 1
    assert loan['amount'] == 1000.0
    assert loan['interest_rate'] == 5.0
    assert loan['due_date'] == '2025-12-31'
    assert loan['status'] == 'active'


def test_update_loan():
    response = client.put('/loans/1', json={
        'amount': 1500.0,
        'interest_rate': 6.0,
        'due_date': '2026-12-31',
        'status': 'inactive'
    })
    assert response.status_code == 200
    loan = response.json()
    assert loan['amount'] == 1500.0
    assert loan['interest_rate'] == 6.0
    assert loan['due_date'] == '2026-12-31'
    assert loan['status'] == 'inactive'


def test_delete_loan():
    response = client.delete('/loans/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'Loan deleted'}

// === ARCHIVO: config/settings.py ===
DATABASE_URL = 'sqlite:///./test.db'
SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'

// === ARCHIVO: scripts/run_tests.sh ===
#!/bin/bash
pytest

```
