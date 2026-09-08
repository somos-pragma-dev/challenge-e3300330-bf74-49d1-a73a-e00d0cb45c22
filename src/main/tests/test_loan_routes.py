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