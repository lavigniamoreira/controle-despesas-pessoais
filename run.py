from app import FRC
frc_um = FRC()
app = frc_um.create_app()
print(app.url_map)

if __name__ == '__main__':
  app.run(debug=True)
