# Viz 


Como as diferentes bibliotecas de python se relacionam atualmente?

<img src='https://www.anaconda.com/wp-content/uploads/2019/01/PythonVisLandscape.jpg'>
(grafico produzido por Jake VanderPlas, 2018)

## Familia OpenGL (1992)

Oferecem visualizações intensivas de gráficos de processos físicos em três ou quatro dimensões (3D ao longo do tempo), para dados com grade regular ou irregular. Essas bibliotecas são anteriores ao suporte do HTML5 a aplicativos da Web avançados, geralmente com foco em aplicativos GUI de desktop de alto desempenho em contextos de engenharia ou científicos.

## Familia MatploLib (2003)

Uma das mais antigas e, de longe, a mais popular das bibliotecas, lançada em 2003, com uma extensa gama de tipos de plotagem 2D e formatos de saída. O Matplotlib também antecedeu o suporte do HTML5 a aplicativos da Web avançados , concentrando-se em imagens estáticas para publicação junto com figuras interativas usando kits de ferramentas de GUI de desktop como o Qt e o GTK. O Matplotlib inclui algum suporte 3D, mas muito mais limitado do que as bibliotecas SciVis fornecem.

## Familia Javascript

Uma vez que HTML5 permitia rica interatividade em navegadores, muitas bibliotecas surgiram para fornecer gráficos 2D interativos para páginas da web e em notebooks Jupyter, usando JS customizado ( Bokeh , Toyplot ) ou envolvendo principalmente bibliotecas JS existentes como D3 ( Plotly , bqplot ). Encapsular o JS existente facilita a adição de novos gráficos criados para o grande mercado JS (como Plotly), enquanto o JS customizado permite definir primitivas JS de nível inferior que podem ser combinadas em novos tipos de plotagem dentro do Python (como no Bokeh).

### Javascript -> Json -> WebGL / D3

Assim como o HTML5 fez para a plotagem de JavaScript 2D, o padrão WebGL tornou a interatividade 3D no navegador e no Jupyter viável, levando à plotagem 3D no navegador construída em tree.js ( pythreejs , ipyvolume ), vtk.js ( itk-jupyter-widgets ) ou regl ( Plotly ). Nenhuma dessas novas abordagens 3D baseadas na Web aborda a amplitude e a profundidade das bibliotecas SciVis 3D de desktop, mas elas permitem total integração com os notebooks Jupyter, fácil compartilhamento e uso remoto via web. Portanto, embora as ferramentas WebGL tenham alguns aplicativos em comum com as ferramentas SciVis, elas provavelmente estão mais ligadas às outras ferramentas InfoVis.

