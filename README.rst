Documentações dos sistemas da UFU
=======================================

Contribuir
**********


Instalar Anaconda
**********

Para contribuir com o projeto basta configurar o ambiente, criar um branch e fazer um pull request.


https://docs.conda.io/projects/conda/en/latest/user-guide/install/

Criar ambiente
**********

- Importar via interface: https://docs.anaconda.com/free/navigator/tutorials/manage-environments/#importing-an-environment

- Importar via console:

.. code-block:: bash

    conda env create -f conda-environment.yml


Ativar ambiente
**********


.. code-block:: bash

    conda activate docsUfu

Compilar ambiente
**********


.. code-block:: bash

    make html


Ao compilar, uma pasta chamada build será gerada no diretório contendo um arquivo index.html, contendo a documentação.


Acesso à Documentação
********************

Após compilada, a documentação ficará disponível em: https://documentacao-sistemas-ufu.readthedocs.io/en/latest/

Criar Gifs e imagens
*********************

Para criar GIFs e imagens, utilize a ferramenta Captura Chrome: https://chrome.google.com/webstore/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe

Para contribuir com este projeto leia os tutoriais:

- https://docs.readthedocs.io/en/stable/tutorial/
- https://www.sphinx-doc.org/en/master/

