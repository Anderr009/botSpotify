from Pages.Spotify import Spotify
from Pages.MailRandom import mailRandom
mailR = mailRandom()
mail = mailR.sendMail()
# -----
spotify = Spotify()
spotify.sendMail(mail)
