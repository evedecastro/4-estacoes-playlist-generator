#!/usr/bin/python

import cgitb
import sitefuncs

cgitb.enable()

print("""<head>
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

    <title>4 Estações - Playlist que agrada todes</title>
    <link rel="icon" href="../imagens/favicon.png">
  </head>
    <body>
""")

sitefuncs.cabecalho()

print("""<section id="home" class="d-flex"><!--home -->
      <div class="container align-self-center"><!--container -->
        <div class="row"><!--row -->
          <div class="col-md-12 capa">

            <div id="carousel-spotify" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner"><!--Inner -->

                <div class="carousel-item active">
                  <h1>Uma playlist para todos os gostos</h1>
                  <a href="criar.py" class="btn btn-lg btn-custom btn-roxo">
                    Crie Uma Sala
                  </a>

                  <a href="acessar.py" class="btn btn-lg btn-custom btn-branco">
                    Acesse Uma Sala
                  </a>
                </div>

                <div class="carousel-item">
                  <h1>Escute as playlist geradas no Spotify</h1>
                  <a href="https://open.spotify.com/?_ga=2.46591781.342293608.1624668279-497195456.1603977817" class="btn btn-lg btn-custom btn-branco">
                    <i class="fas fa-music"></i> Ouça agora
                  </a>
                </div>

              </div><!--/Inner -->

              <!-- Controles -->
              <a href="#carousel-spotify" class="carousel-control-prev" data-slide="prev">
                <i class="fas fa-angle-left fa-3x"></i>
              </a>

              <a href="#carousel-spotify" class="carousel-control-next" data-slide="next">
                <i class="fas fa-angle-right fa-3x"></i>
              </a>

            </div>

          </div>
        </div><!--/row -->
      </div><!--/container -->
    </section><!--/home -->

    <section id="servicos" class="caixa">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="row albuns">
              <div class="col-md-6">
                <img src="../imagens/img1.jpg" class="img-fluid">
              </div>
              <div class="col-md-6">
                <img src="../imagens/img2.jpg" class="img-fluid">
              </div>
            </div>
            <div class="row albuns">
              <div class="col-md-6">
                <img src="../imagens/img3.jpg" class="img-fluid">
              </div>
              <div class="col-md-6">
                <img src="../imagens/img4.jpg" class="img-fluid">
              </div>
            </div>
          </div>
          <div class="col-md-6">

            <h3>Não ta afim de criar uma playlist agora? A gente te ajuda mesmo assim</h3>

            <iframe src="https://open.spotify.com/embed/playlist/4oYUiu5D9pYDqYDOYgmolI" width="100%" height="120" 
            frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>

            <iframe src="https://open.spotify.com/embed/playlist/2x903C6a9xBVMsk8noJbiV" width="100%" height="120" 
            frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>

            <iframe src="https://open.spotify.com/embed/playlist/0QiUvrVH7PgbRZiJhfueYX?theme=0" width="100%" height="120" 
            frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>
            
            <iframe src="https://open.spotify.com/embed/playlist/2ppDxvTVWCoI9dpoGsauhx?theme=0" width="100%" height="120" 
            frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>

          </div>
        </div>
      </div>
    </section>


    <section id="recursos" class="caixa">
      <div class="container">
        <div class="row">
          <div class="col-md-4">

            <h2>Como</h2>
            <h3>Entrar</h3>
            <p>A primeira coisa que você precisa fazer é entrar na sua conta, se você ainda não uma tem clique no botão Inscreva-se e comece essa jornada conosco.
            </p>

            <h3>Criar</h3>
            <p>Abra uma nova sala ou entre em uma já existe, com o código da sala, e crie sozinhe ou junte de sues amigues uma playlist perfeita.
            </p>

            <h3>Descobrir</h3>
            <p>Curta músicas que agradam a todes com uma playlist personalizada pra você abrindo o seu Spotify em seu celular, computador ou pelo Player da Web.
            </p>

          </div>
          <div class="col-md-8">
            <div class="row rotacionar">
              <div class="col-md-6">
                <img src="../imagens/iphone1.png" class="img-fluid">
              </div>
              <div class="col-md-6">
                <img src="../imagens/iphone2.png" class="img-fluid">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
""")

sitefuncs.footer()

print("""<!-- JavaScript (Opcional) -->
        <!-- jQuery primeiro, depois Popper.js, depois Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
      </body>
    </html>]""")
