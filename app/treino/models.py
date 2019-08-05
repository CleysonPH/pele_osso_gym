from app import db


class Treino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carga = db.Column(db.Float, nullable=True)
    repeticao = db.Column(db.Integer, nullable=True)
    secao = db.Column(db.Integer, nullable=True)
    descanso = db.Column(db.Integer, nullable=True)

    exercicio_id = db.Column(db.Integer, db.ForeignKey('exercicio.id'), nullable=False)
    exercicio = db.relationship('Exercicio', backref=db.backref('treinos', lazy=True))

    ficha_id = db.Column(db.Integer, db.ForeignKey('ficha.id'), nullable=False)
    ficha = db.relationship('Ficha', backref=db.backref('treinos', lazy=True))


    def __init__(self, exercicio, carga, repeticao, secao, descanso, ficha):
        self.exercicio = exercicio
        self.carga = carga or None
        self.repeticao = repeticao or None
        self.secao = secao or None
        self.descanso = descanso or None
        self.ficha = ficha


    def __repr__(self):
        return f'<Treino {self.exercicio.nome} in {self.ficha.nome}>'
