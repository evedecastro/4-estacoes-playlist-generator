#!/usr/bin/python

import cgitb
import sitefuncs

cgitb.enable()

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

<title>4 Estações - Acessar Sala</title>
<link rel="icon" href="../imagens/favicon.png">
</head>
<body>
""")

sitefuncs.headerform()

sitefuncs.cabecalho()

print("""<div class="limiter">""")

print("""<div class="container-login100">""")

print("""<div class="wrap-login100">""")

print("""<div class="login100-pic js-tilt" data-tilt>""")
print("""<img src="../imagens/img-01.png" alt="IMG">""")
print("""</div>""")

print("""<form class="login100-form validate-form" action=\"handleacessar.py\" methods=\"post\">""")
print("""<span class="login100-form-title">Acessar Sala</span>""")

print("""
<div class="wrap-input100 validate-input" data-validate = "FriedsPlaylistId is required">
<input class="input100" type="text" name="playlist_id" placeholder="Your Friends PlaylistId">
<span class="focus-input100"></span>
<span class="symbol-input100"><i class="fa fa-envelope" aria-hidden="true"></i></span>
</div>""")

print("""
<div class="wrap-input100 validate-input" data-validate = "UserId is required">
<input class="input100" type="text" name="userid" placeholder="UserId">
<span class="focus-input100"></span>
<span class="symbol-input100"><i class="fa fa-envelope" aria-hidden="true"></i></span>
</div>""")

print("""
<div class="wrap-input100 validate-input" data-validate = "PlaylistID is required">
<input class="input100" type="text" name="playlistid" placeholder="PlaylistID">
<span class="focus-input100"></span>
<span class="symbol-input100"><i class="fa fa-lock" aria-hidden="true"></i></span>
</div>""")

print("""
<div class="container-login100-form-btn">
<button class="login100-form-btn">Acessar</button>
</div>""")
print("""</form>""")
print(""""</div>""")
print("""</div>""")
print("""</div>""")

sitefuncs.footer()
print(""" </body>
    </html>]""")
