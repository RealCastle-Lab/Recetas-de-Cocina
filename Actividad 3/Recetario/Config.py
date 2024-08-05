engine = create_engine('mysql+pymysql://usuario:contraseña@localhost/recetario')
Session = sessionmaker(bind=engine)
