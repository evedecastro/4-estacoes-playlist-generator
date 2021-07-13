#!/usr/bin/python

import cgitb
import cgi
import sitefuncs
from spotifyclient import SpotifyClient

cgitb.enable()

form = cgi.FieldStorage()
auth_token = "BQAwMF1idkdWrELMI_odCHAuDxTNMWSuluCa0lbpDqNUrY7nqgc9smI_bNKTo75Be19EcALfhoQj-IfOVFg8CwY_kK4rQQRjMI-Qt-6LRDRt9-dxmYli4866T446xFvVAFcR-PitnvQQKJHv2kbZeyQX8KJiGw5ECkBgmMZpcdsmHAsaaS2kFQvH4Mq5eW9mV2e4Q293L6sn3x0MK0zVjhZQJNwu9q27XlqyZI_8O0GAtwwkCQIzA4_KKQErcAqhLJ9EmfLF1Jbr6t7kvTeu-n6dszTJt0z9pXVh0ITs8t2U"
userid = form.getvalue('userid')
playlistid = form.getvalue('playlistid')
playlist_id = form.getvalue('playlist_id')

spotclient = SpotifyClient(auth_token, userid, playlistid)

#getting recommended tracks
clientplaylist_tracks = spotclient.get_clientplaylist_tracks()
seed_tracks = clientplaylist_tracks
# populate playlist with seed tracks
spotclient.populate_playlist_acess(playlist_id, seed_tracks)
# get recommended tracks based off seed tracks
recommended_tracks = spotclient.get_track_recommendations(seed_tracks)
# populate playlist with recommended tracks
spotclient.populate_playlist_acess(playlist_id, recommended_tracks)

print("""
<head>
<!-- Meta tags Obrigatórias -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">

<!-- HTML5Shiv -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<![endif]-->

<!-- Estilo customizado -->
<link rel="stylesheet" type="text/css" href="../css/estilo.css">

<title>4 Estações - Sala</title>
<link rel="icon" href="../imagens/favicon.png">
</head>
<body>
""")

sitefuncs.headerform()

sitefuncs.cabecalho()

print("""
<div class="limiter">
<div class="container-login100">
<div class="wrap-login100">

<form class="login100-form validate-form">
<span class="login100-form-title">Musicas adicionadas com sucesso.</span>
</form>
</div>
</div>
</div>""")

sitefuncs.footer()
print(""" </body>
    </html>]""")



