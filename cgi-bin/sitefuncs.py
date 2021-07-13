from spotifyclient import SpotifyClient

def cabecalho():
    print("""	
    <header><!-- inicio Cabecalho -->
      <nav class="navbar navbar-expand-md navbar-light fixed-top navbar-transparente">
        <div class="container">
          
          <a href="index.py" class="navbar-brand">
            <img src="../imagens/logoicon.png" width="142">
          </a>

          <button class="navbar-toggler" data-toggle="collapse" data-target="#nav-principal">
            <i class="fas fa-bars text-white"></i>
          </button>

          <div class="collapse navbar-collapse" id="nav-principal">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a href="criar.py" class="nav-link">Criar</a>
              </li>
              <li class="nav-item">
                <a href="acessar.py" class="nav-link">Acessar</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header><!--/fim Cabecalho -->""")


def footer():
    print("""    <footer>
          <div class="container">
            <div class="row">
              <div class="col-md-2">
                <img src="../imagens/logoicon.png" width="142">
              </div>
              <div class="col-md-2">
                <h4>quem somos</h4>
                <ul class="navbar-nav">
                  <li><a href="">Sobre</a></li>
                  <li><a href="">Novidades</a></li>
                </ul>
              </div>
              <div class="col-md-2">
                <h4>Indicações</h4>
                <ul class="navbar-nav">
                  <li><a href="">Artistas</a></li>
                  <li><a href="">Playlists</a></li>
                  <li><a> Copyright © 2021, Eve </a></li>
                </ul>
              </div>
              <div class="col-md-2">
                <h4>links uteis</h4>
                <ul class="navbar-nav">
                  <li><a href="">Ajuda</a></li>
                  <li><a href="">Player da web</a></li>
                </ul>
              </div>
              <div class="col-md-4">
                <ul>
                  <li>
                    <a href=""><img src="../imagens/facebook.png"></a>
                  </li>
                  <li>
                    <a href=""><img src="../imagens/twitter.png"></a>
                  </li>
                  <li>
                    <a href=""><img src="../imagens/instagram.png"></a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </footer>
""")


def headerform():
    print("""<head>
    	<title>4 Estações - Forms </title>
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!--===============================================================================================-->	
    	<link rel="icon" href="../imagens/favicon.png"/>
    <!--===============================================================================================-->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <!--===============================================================================================-->
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    <!--===============================================================================================-->
    	<link rel="stylesheet" type="text/css" href="../vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
    	<link rel="stylesheet" type="text/css" href="../fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
    	<link rel="stylesheet" type="text/css" href="../vendor/animate/animate.css">
    <!--===============================================================================================-->	
    	<link rel="stylesheet" type="text/css" href="../vendor/css-hamburgers/hamburgers.min.css">
    <!--===============================================================================================-->
    	<link rel="stylesheet" type="text/css" href="../vendor/select2/select2.min.css">
    <!--===============================================================================================-->
    	<link rel="stylesheet" type="text/css" href="../css/util.css">
    	<link rel="stylesheet" type="text/css" href="../css/main.css">
    <!--===============================================================================================-->
        <!-- HTML5Shiv -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <![endif]-->
    <!--===============================================================================================-->
        <link rel="stylesheet" type="text/css" href="../css/estilo.css">
    </head>
    <body>""")



