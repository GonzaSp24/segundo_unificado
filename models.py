from app import db

class Marca(db.Model):
    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Marca {self.nombre}>"

class Tipo(db.Model):
    __tablename__ = 'tipo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Tipo {self.nombre}>"

class Vehiculo(db.Model):
    __tablename__ = 'vehiculo'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    # Relaciones con Marca y Tipo
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    # Relación directa con las otras tablas
    marca = db.relationship('Marca', backref=db.backref('vehiculos', lazy=True))
    tipo = db.relationship('Tipo', backref=db.backref('vehiculos', lazy=True))

    def __repr__(self):
        return f"<Vehiculo {self.modelo}, {self.anio_fabricacion}>"

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
