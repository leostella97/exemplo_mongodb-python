# Exemplo da biblioteca NoSQL MongoDB com a linguagem Python

<ol>
<li> O código acima usa a biblioteca pymongo para se conectar ao banco de dados MongoDB e realizar operações básicas de CRUD (Create, Read, Update, Delete).
<li> As variáveis joao, maria e ana representam documentos JSON que serão armazenados na coleção usuarios.
<li> A função insert_many() insere os documentos na coleção.
<li> A função find({}) busca todos os documentos na coleção.
<li> O loop for itera sobre os resultados da busca e imprime cada documento.
<li> A função update_one() atualiza um documento na coleção.
<li> A função delete_one() exclui um documento da coleção.
<li> A função close() fecha a conexão com o banco de dados.
